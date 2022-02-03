import requests

def teste_post_criar_tag():
    tag = {"nome": "tag teste"}
    url = "http://localhost:5000/criarTag"
    response = requests.post(url,json=tag)
    id_tag = response.json()["ID"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json'

def teste_post_criar_card():
    print(id_tag)
    card = {"texto": "Teste api", "Tags":[id_tag]}
    url = "http://localhost:5000/criarTag"
    response = requests.post(url,json=card)
    id_card = response.json()["ID"]
    assert response.status_code == 200
    assert response.headers["Content-Type"] == 'application/json'