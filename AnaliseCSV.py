import pandas as pd
from pathlib import Path

#section FUNÇÕES

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

##Exibe em tela os dois resultados solicitados
def _exibe_resultados(tabela_agrupada):
    # Chama a função que encontra o maior e menor faturamento
    menor_maior_faturamento = _menor_maior_faturamento(tabela_agrupada)

    # Formata os valores da tabela principal Para exibir como monetario
    tabela_agrupada['Faturamento_Total'] = tabela_agrupada['Faturamento_Total'].apply(lambda x: f"R${x:.2f}")

    # printado os resultados em tela separadamente
    print(f"{"-" * 20}FATURAMENTO{"-" * 20}")
    print(tabela_agrupada)
    print("")
    print(f"{"-" * 15}MENOR E MAIOR FATURAMENTO{"-" * 15}")
    print(menor_maior_faturamento)

##Função que realiza o print do resultado com quatidade de produtos vendidos e o valor total do faturamento
def _main():
    #Define o caminho do arquivo
    caminho_arquivo = Path("Vendas.csv")
    #Define as colunas que serão utilizadas
    colunas_utilizadas = {"produto", "quantidade", "preco_unitario"}

    #Verifica se o Arquivo CSV existe
    if caminho_arquivo.exists():

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

            _exibe_resultados(tabela_agrupada)

    else:
        exit(f"Arquivo {caminho_arquivo} não encontrado")

#endsection


##Inicia o Programa
_main()

