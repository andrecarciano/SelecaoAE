# Manipulação de CSV com Python

Este script é um exemplo simples de análise e manipulação de um arquivo CSV com algumas informações de vendas de produtos.
Dentro do projeto, você encontrará o arquivo **"Vendas.csv"** que contém alguns dados para teste.

## Princípios básicos

- Calcular e exibir o faturamento total por produto e total de unidades vendidas.
- Encontrar e exibir o produto com maior faturamento e o produto com menor faturamento.

## Tecnologias utilizadas

- **pandas**: Para manipulação de dados do arquivo CSV.
- **pathlib**: Para verificação do caminho do arquivo "Vendas.csv".

**Versão do Python:** 3.13.2

## Funcionamento

### Verificação do arquivo

O script verifica se o arquivo **Vendas.csv** existe antes de iniciar a manipulação dos dados.
Caso o arquivo seja deletado ou renomeado, uma mensagem será exibida no console.

### Verificação das colunas

O script verifica se as colunas necessárias (**produto, quantidade, preco_unitario**) estão presentes no arquivo.
Se alguma dessas colunas estiver ausente, o programa é encerrado com uma mensagem de erro.

## Estrutura do script

1. **Função `_main()`**
   - É a função principal do script.
   - Define o caminho do arquivo CSV e verifica se ele existe.
   - Lê o arquivo utilizando o delimitador `;`.
   - Verifica se todas as colunas necessárias estão presentes.
   - Calcula o faturamento total de cada produto (`quantidade * preco_unitario`).
   - Agrupa os dados por produto, somando as quantidades vendidas e o faturamento total.
   - Chama a função `_exibe_resultados()` para exibir os resultados.

2. **Função `_verifica_colunas(caminho_arquivo, colunas_utilizadas)`**
   - Confirma se todas as colunas necessárias estão presentes no arquivo CSV.
   - Caso alguma coluna esteja ausente, o script é encerrado com uma mensagem de erro.

3. **Função `_exibe_resultados(tabela_agrupada)`**
   - Exibe os resultados no console.
   - Chama `_menor_maior_faturamento()` para obter os produtos com menor e maior faturamento.
   - Formata os valores monetários para o formato `R$XX,XX`.
   - Printa a tabela de vendas com a quantidade total vendida e faturamento total por produto.
   - Printa também os produtos com menor e maior faturamento.

4. **Função `_menor_maior_faturamento(tabela_agrupada)`**
   - Recebe um DataFrame com os dados agrupados por produto.
   - Encontra o produto com menor faturamento e o produto com maior faturamento.
   - Retorna um novo DataFrame contendo os nomes desses produtos e seus valores formatados como `R$`.

## Como executar o script

1. Certifique-se de ter o Python 3.13.2 instalado.
2. Instale as dependências necessárias com:
   ```sh
   pip install pandas
   ```
3. Coloque o arquivo **Vendas.csv** na mesma pasta do script.
4. Execute o script:
   ```sh
   python script.py
   ```

## Exemplo de Saída

```
--------------------FATURAMENTO--------------------
  Produto  Quantidade_Vendida  Faturamento_Total
0       A                 10           R$100.00
1       B                 20           R$200.00
2       C                 30           R$300.00

---------------MENOR E MAIOR FATURAMENTO---------------
  Produto Menor_Faturamento Maior_Faturamento
0       A          R$100.00                 
1       C                   R$300.00
```
