from flask import jsonify, request, render_template
from main import app

#rotas
#End point home
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


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
