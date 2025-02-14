import os

import pandas as pd
from flask import jsonify

#region FUNÇÕES

##função para verificar se as colunas que serão utilizadas existem
def  _verifica_colunas(caminho_arquivo, colunas_utilizadas):
    colunas = pd.read_csv(caminho_arquivo, sep=';', nrows=0)
    col_encontradas = set(colunas.columns)
    if colunas_utilizadas-col_encontradas:
        exit(f"As seguintes colunas não foram encontradas{colunas_utilizadas-col_encontradas}")
    else:
        return True

##Função para encontrar o maior e menor Faturamento do DataFrame passado por parametro
def _menor_maior_faturamento(tabela_agrupada):
    menor_valor_prod = tabela_agrupada.loc[tabela_agrupada["Faturamento_Total"].idxmin()]
    maior_valor_prod = tabela_agrupada.loc[tabela_agrupada["Faturamento_Total"].idxmax()]

    # Retornando um novo DataFrame com os resultados Maior e menor
    # Formata os valores para exibir como monetario
    return pd.DataFrame({
        "Produto": [menor_valor_prod["Produto"], maior_valor_prod["Produto"]],
        "Menor_Faturamento": [f"R${menor_valor_prod['Faturamento_Total']:.2f}", ""],
        "Maior_Faturamento": ["", f"R${maior_valor_prod['Faturamento_Total']:.2f}"]
    })

##Retorna json com os dois resultados solicitados
def _retorna_json(tabela_agrupada):
    try:
        # Chama a função que encontra o maior e menor faturamento
        menor_maior_faturamento = _menor_maior_faturamento(tabela_agrupada)

        # Formata os valores da tabela principal Para exibir como monetario
        tabela_agrupada['Faturamento_Total'] = tabela_agrupada['Faturamento_Total'].apply(lambda x: f"R${x:.2f}")

        # Converte os DataFrames em dicionários
        tabela_agrupada_dict = tabela_agrupada.to_dict(orient='records')
        menor_maior_faturamento_dict = menor_maior_faturamento.to_dict(orient='records')

        # Resposta JSON
        response = {
            "faturamento": tabela_agrupada_dict,
            "menor_e_maior_faturamento": menor_maior_faturamento_dict
        }
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(response)


##Função que retorna o json do resultado com quatidade de produtos vendidos e o valor total do faturamento
def _analisar(caminho_arquivo):

    #Define as colunas que serão utilizadas
    colunas_utilizadas = {"produto", "quantidade", "preco_unitario"}

    if _verifica_colunas(caminho_arquivo, colunas_utilizadas): #verifica se todas as colunas necessarias existem

        # Busca o Arquivo CSV na Pasta do Projeto, define o separador como `;`, define as colunas a serem utilizadas
        # e o adiciona na variavel arquivo
        arquivo = pd.read_csv(caminho_arquivo, sep=';', usecols=list(colunas_utilizadas))

        #Cria a Coluna "valor_total", Realiza o Calculo de Valor de Faturamento por venda e adicona o resultado à nova coluna
        arquivo["valor_total"] = arquivo["quantidade"] * arquivo["preco_unitario"]

        #Agrupa os Itens por Produto, somando a quantidade total vendida e o valor total do faturamento de cada produto
        tabela_agrupada = (arquivo.groupby("produto").agg({
            "quantidade": "sum",
            "valor_total": "sum"
        }).reset_index()
          .rename(columns={"quantidade":"Quantidade_Vendida","valor_total":"Faturamento_Total","produto":"Produto"}))#renomeando as colunas e o agrupamento

        #DELETA O ARQUIVO TEMPORARIO
        os.remove(caminho_arquivo)

        #retorna um json com os resultados
        return _retorna_json(tabela_agrupada)

#endregion

