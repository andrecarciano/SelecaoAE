## 🎯 Apresentação
Este projeto foi desenvolvido para o **Teste do processo seletivo** para a **Vaga de Desenvolvedor Python Jr.** do **Hosp. Albert Einstein**.

A princípio, comecei a desenvolver projetos separados, mas no meio do caminho decidi que seria mais vantajoso incluir todas as funcionalidades em um único projeto, permitindo que eu demonstrasse mais minhas capacidades gerais.

As documentações das questões respondidas neste projeto estão logo abaixo e também nas suas respectivas abas dentro do projeto.

---

## 🚀 Como Usar?
### Opção 1: Executando Localmente
1. Faça o download deste repositório.
2. Execute o arquivo `App.py` com o Python.
3. Certifique-se de ter as bibliotecas **Pandas** e **Flask** instaladas localmente.

### Opção 2: Usando Docker
Você pode executar o projeto dentro de um container Docker. Para isso, siga as instruções da seção "Docker" do arquivo
[README.md](https://github.com/andrecarciano/SelecaoAE/tree/main?tab=readme-ov-file#-docker-file) na raiz deste projeto.

---

## 📄 Questão 2 - Manipulação de CSV com Python

### 🎯 Apresentação
Este script é um exemplo simples de análise e manipulação de um arquivo **CSV** com informações de vendas de produtos.

### 🛠️ Como Usar?
Dentro do projeto, você encontrará o arquivo **"Vendas.csv"** com dados para teste. Você também pode baixá-lo [aqui](https://github.com/andrecarciano/SelecaoAE/blob/main/APIFlask/Vendas.csv).

1. Insira o arquivo "Vendas.csv" no **file upload**.
2. O resultado será exibido em uma nova guia no formato **JSON**.

### 📝 Princípios Básicos
- Calcular e exibir o faturamento total por produto e total de unidades vendidas.
- Encontrar e exibir o produto com **maior faturamento** e o produto com **menor faturamento**.

### 🧑‍💻 Tecnologias Utilizadas
- **pandas**: Para manipulação de dados do arquivo CSV.
- **pathlib**: Para verificação do caminho do arquivo "Vendas.csv".
- **flask**: Para conversão e retorno do JSON.
- **Python**: 3.13.2
- **Bootstrap**: 5.3
- **JavaScript**
- **CSS**

### 🛠️ Funcionamento

#### Verificação do Arquivo
O script recebe o caminho do arquivo `Vendas.csv`, que será salvo pelo endpoint `/csv` da API Flask.

#### Verificação das Colunas
O script verifica se as colunas necessárias (produto, quantidade, preco_unitario) estão presentes no arquivo. Caso alguma delas esteja ausente, o programa exibe uma mensagem de erro.

#### Estrutura do Script
O script foi dividido em 4 funções:

1. **Função `_analisar(caminho_arquivo)`**:
   - Função principal do script.
   - Verifica as colunas necessárias.
   - Lê o arquivo CSV usando o delimitador `;`.
   - Calcula o faturamento total de cada produto.
   - Agrupa os dados por produto, somando quantidades e faturamento total.
   - Retorna os resultados em JSON.

2. **Função `_verifica_colunas(caminho_arquivo, colunas_utilizadas)`**:
   - Confirma se todas as colunas necessárias estão presentes no CSV.
   - Caso alguma esteja ausente, o script exibe uma mensagem de erro.

3. **Função `_retorna_json(tabela_agrupada)`**:
   - Retorna um JSON com os resultados.
   - Formata valores monetários para o formato `R$XX,XX`.
   - Exibe a tabela de vendas e os produtos com menor e maior faturamento.

4. **Função `_menor_maior_faturamento(tabela_agrupada)`**:
   - Encontra o produto com menor e maior faturamento.
   - Retorna os dados formatados como `R$`.

### 🎬 Demonstração

![Demo](https://media.giphy.com/media/l4KbdtYf0IBfGGYac/giphy.gif)

---

## 🔥 Questão 3 - Web Frameworks API com Flask

### 🎯 Apresentação
Esta API foi desenvolvida utilizando o framework **Flask** para Python. Ela tem como objetivo fornecer funcionalidades simples para demonstração.

A API oferece três endpoints principais:
- **Home**: Página inicial da API.
- **Saudação**: Retorna uma saudação personalizada.
- **Soma**: Realiza a soma de dois números fornecidos via JSON.

Além disso, existe o endpoint de **Análise de CSV**.

### 🚀 Endpoints

1. **End Point: Home**
   - **URL**: `/`
   - **Método**: `GET`
   - **Descrição**: Retorna a página inicial.

2. **End Point: Saudação**
   - **URL**: `/saudacao?nome={nome}`
   - **Método**: `GET`
   - **Descrição**: Retorna uma saudação personalizada com o nome enviado como parâmetro na query string.
   - **Exemplo de chamada**: 
     ```bash
     http://localhost:5000/saudacao?nome=Andrezinho
     ```
   - **Resposta**: "Olá, Andrezinho seja muito bem-vindo(a) a minha API Flask"

3. **End Point: Soma**
   - **URL**: `/soma`
   - **Método**: `POST`
   - **Descrição**: Recebe um objeto JSON no corpo da requisição e retorna a soma dos dois números fornecidos.
   - **Exemplo de JSON enviado**:
     ```json
     {
       "operando1": 10,
       "operando2": 5
     }
     ```
   - **Resposta**: "A soma de 10 + 5 é 15"

---

## 🧑‍💻 Conclusão
Com este projeto, pude demonstrar habilidades no uso de diversas tecnologias como: **HTML 5**, **CSS**, **JavaScript**, **Bootstrap**, **Python**, **Flask**, **PathLib**, e **Pandas**.

Além disso, tive a oportunidade de demonstrar conhecimentos em **organização de código**, **lógica de programação**, **documentação**, entre outros.

---

### 🎬 Demonstração

![Demo](https://media.giphy.com/media/l4KbdtYf0IBfGGYac/giphy.gif)

---

