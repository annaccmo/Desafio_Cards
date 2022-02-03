from flask import Flask, request, Response, json
from datetime import datetime
import uuid
from mongo_connection import MongoDB

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Api para cards de conteúdo'

@app.route('/criarCard', methods=['POST'])
def criarCard():
    card = request.get_json()
    if card is None:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')

    data = datetime.today().strftime('%Y-%m-%d %H:%M')
    card_id = str(uuid.uuid1())
    card["id"] = card_id
    card["data_criacao"] = data
    card["data_modificacao"] = data
    
    db_obj = MongoDB("cards")
    response = db_obj.insert(card)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/lerCard/<id>', methods=['GET'])
def lerCard(id):
    dados = {}
    dados['id'] = id 
    db_obj = MongoDB("cards")
    response = db_obj.read_by_id(dados)
    response['_id'] = str(response['_id'])
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    

@app.route('/removerCard/<id>', methods=['DELETE'])
def removerCard(id):
    dados = {}
    dados['id'] = id
    db_obj = MongoDB("cards")
    response = db_obj.delete(dados)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    

@app.route('/atualizarCard/<id>', methods=['PUT'])
def atualizarCard(id):
    dados = {}
    dados['id'] = id
    dados['newData'] = request.get_json()
    if dados['newData'] is None:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    
    data = datetime.today().strftime('%Y-%m-%d %H:%M')
    dados['newData']['data_modificacao'] = data

    db_obj = MongoDB("cards")
    response = db_obj.update(dados)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/listarCards', methods=['GET'])
def listarCard():
    db_obj = MongoDB("cards")
    response = db_obj.read_all()
    return Response(response=json.dumps(str(response)),
                    status=200,
                    mimetype='application/json')
    #return str(response)

@app.route('/cardsPorTags/<tagid>', methods=['GET'])
def cardsPorTags(tagid):
    db_obj = MongoDB("cards")
    response = db_obj.read_with_filter(tagid)
    return Response(response=json.dumps(str(response)),
                    status=200,
                    mimetype='application/json')

@app.route('/criarTag', methods=['POST'])
def criarTag():
    tag = request.get_json()
    if tag is None:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    
    tag_id = str(uuid.uuid1())
    tag['id'] = tag_id
    db_obj = MongoDB("tags")
    response = db_obj.insert(tag)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/lerTag/<id>', methods=['GET'])
def lerTag(id):
    dados = {}
    dados['id'] = id 
    db_obj = MongoDB("tags")
    response = db_obj.read_by_id(dados)
    response['_id'] = str(response['_id'])
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/lerTagPorNome/<nome>', methods=['GET'])
def lerTagPorNome(nome):
    dados = {}
    dados['nome'] = nome
    db_obj = MongoDB("tags")
    response = db_obj.find_by_name(name)
    response['_id'] = str(response['_id'])
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/removerTag/<id>', methods=['DELETE'])
def removerTag(id):
    dados = {}
    dados['id'] = id
    db_obj = MongoDB("tags")
    response = db_obj.delete(dados)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/atualizarTag/<id>', methods=['PUT'])
def atualizarTag(id):
    dados = {}
    dados['id'] = id
    dados['newData'] = request.get_json()
    if dados['newData'] is None:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')

    db_obj = MongoDB("tags")
    response = db_obj.update(dados)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/listarTags', methods=['GET'])
def listarTags():
    db_obj = MongoDB("tags")
    response = db_obj.read_all()
    return Response(response=json.dumps(str(response)),
                    status=200,
                    mimetype='application/json')
    

app.run()