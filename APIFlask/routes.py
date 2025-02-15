import os
from App import app
from flask import jsonify, request, render_template, send_file
from AnaliseCSV import _analisar #<- LOGICA EXERCICIO 2 PASTA AnaliseCSV


##########END POINTS PROPOSTOS NA QUESTAO 3 AVALIAÇÃO

#End Point de Saudação
@app.route('/saudacao', methods=['GET'])
def saudacao():
    #Parametro recebido por QueryString
    nome = request.args['nome']
    return f"Olá, {nome} seja muito bem-vindo(a) a minha API Flask"


#End Point de Soma
@app.route('/soma', methods=['POST'])
def soma():
    #recebendo o objeto json enviado no body da requisição
    json = request.get_json()
    #verifica se existe um json
    if not json:
        return jsonify({"erro":"Envie Um objeto JSON na requisição"}),400
    #obtem as propriedades do JSON
    operando1 = json.get("operando1")
    operando2 = json.get("operando2")
    #Retorna a soma dos Numeros
    return f"A soma de {operando1} + {operando2} é {operando1+operando2}"


############END POINTS DA QUESTAO 2 DA AVALIAÇÃO

#End point Para manipular CSV
@app.route('/csv', methods=['POST'])
def csv():
    #RECEBE O ARQUIVO CARREGADO PELO HTML
    arquivo = request.files['file']

    #Caminho para salvamento temporario
    caminho_arquivo = os.path.join('temp', arquivo.filename)

    #Cria a pasta temporaria caso ainda não exista
    os.makedirs('temp', exist_ok=True)

    #Salva o arquivo na pasta do sistema
    arquivo.save(caminho_arquivo)

    return _analisar(caminho_arquivo)


############END POINTS SOBRESALENTES

#End point home
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


#Download Arquivo JSON
@app.route('/download-json')
def download_json():
    caminho_arquivo = "postmanJson/postman_collection.json"
    return send_file(caminho_arquivo, as_attachment=True, mimetype='application/json')


#Download Arquivo CSV
@app.route('/download-csv')
def download_csv():
    return send_file("Vendas.csv", as_attachment=True, mimetype='csv')
