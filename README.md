# 📌 O que contém nesse projeto?

Este projeto foi criado com o intuito de demonstrar algumas habilidades e resolver algumas questões do **“Teste para Vaga de Desenvolvedor Python”** do processo seletivo do **Hospital Albert Einstein**.🏥

📌 Todo o código-fonte está devidamente comentado para facilitar a leitura e entendimento da lógica.

---

## 🚀 Função Assíncrona com Python
📂 Na pasta **“FuncaoAssincrona”** contém uma lógica de uso de função assíncrona em Python. 
🔗 Toda as informações que você precisará estão no arquivo [README.md](https://github.com/andrecarciano/SelecaoAE/tree/main/FuncaoAssincrona) dentro da pasta **“FuncaoAssincrona”**.

---

## 🌐 API Flask
📂 Na pasta **“APIFlask”** contém uma API simples que soluciona **2 questões** do teste citado no início deste documento.

### 🔹 1- Análise de Dados em arquivo CSV
📌 Contém uma lógica para analisar dados em um arquivo CSV.

📑 Toda a Documentação detalhada você encontra no arquivo [README.md](https://github.com/andrecarciano/SelecaoAE/tree/main/APIFlask#-quest%C3%A3o-2---manipula%C3%A7%C3%A3o-de-csv-com-python) dentro da pasta **“APIFlask”** e na aba **“Documentação Algorítimo”** com o app em execução.

### 🔹 2- API com Endpoints GET e POST
📌 Contém uma API simples com os Endpoints solicitados:
- **GET(/saudacao)**
- **POST(/soma)**
  
📑 Toda a Documentação detalhada você encontra no arquivo [README.md](https://github.com/andrecarciano/SelecaoAE/tree/main/APIFlask#-quest%C3%A3o-3---web-frameworks-api-com-flask) dentro da pasta **“APIFlask”** e na aba **“Documentação API”** com o app em execução.

---

## 🐳 Docker File
📌 Na raiz do projeto você encontrará um **DockerFile** com os comandos necessários para gerar e iniciar um container Docker rodando o projeto.

### 🚀 Utilizar imagem do projeto para gerar um Container Docker
Este projeto tem uma imagem Docker disponível em: **[DockerHub/andrecarciano](https://hub.docker.com/r/andrecarciano/apiselecaoae)**.
Se você quiser obter a imagem desse projeto para iniciar o seu próprio container, execute as instruções abaixo no seu console:

```sh
# Baixar a imagem Docker
 docker pull andrecarciano/apiselecaoae

# Iniciar o container
 docker run -d -p 5000:5000 andrecarciano/apiselecaoae
```

---

## 🌍 Como acessar a aplicação?
Para acessar a aplicação, utilize o comando correspondente ao seu sistema operacional:

📌 **Windows (cmd ou powershell):**
```sh
start http://localhost:5000
```

📌 **macOS:**
```sh
open http://localhost:5000
```

📌 **Linux/macOS (para distribuições Linux com suporte a xdg-open):**
```sh
xdg-open http://localhost:5000
```

Ou utilize um comando compatível com seu sistema operacional.

---

## 🎯 Conclusão
📌 Os itens presentes neste projeto demonstram algumas **técnicas de desenvolvimento**, respondendo algumas das questões do teste proposto e unificando essas soluções em um único projeto.

✨ **Seja bem-vindo ao projeto e aproveite!** 🚀

