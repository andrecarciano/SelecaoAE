# IMAGEM DO PYTHON NA VERSAO 3.13.2
FROM python:3.13.2-slim

#PASTA RAIZ DO LINUX DO CONTAINER ONDE OS ARQUIVOS DO PROJETO SERÃO COPIADOS
WORKDIR /usr/src/app

#COPIA OS ARQUIVOS DO PROJETO PARA O CONTAINER
COPY . .

#INSTALA AS DEPENDENCIAS(BIBLIOTECAS) DO PROJETO PRESENTES NO ARQUIVO "requirements.txt"(exemplo Flask OU Pandas)
RUN pip install --no-cache-dir -r requirements.txt

#EXPOE A PORTA 5000 DO CONTAINER PARA PODERMOS ACESSA-LA E MAPEAR COM ALGUMA PORTA DA MAQUINA LOCAL (EXEMPLO: 5000:5000)
EXPOSE 5000

#COMANDO QUE SERÁ EXECUTADO QUANDO O CONTAINER INICIAR
CMD [ "python", "APIFlask/App.py" ]
