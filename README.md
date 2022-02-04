# Passos para rodar API

Rode os seguintes comandos no terminal
```
sudo docker pull mongo
```

```
sudo docker create -it --name MongoApiCards -p 27017:27017 mongo
```

```
sudo docker start MongoApiCards
```

```
pip install -r requirements.txt
```

```
python Api_python/api_cards.py 
```

Assim a Api está rodando em `localhost:5000`

### Segue as urls da API

- POST `localhost:5000/criarCard` - campos json: texto (str) e tags (list(tag ids))
- GET `localhost:5000/lerCard/<id>`
- DELETE `localhost:5000/removerCard/<id>`
- PUT `localhost:5000/atualizarCard/<id>` - campos json: campos a serem atualizados
- GET `localhost:5000/listarCards`
- GET `localhost:5000/cardsPorTags/<tagid>`
- POST `localhost:5000/criarTag` - campos json: nome (str)
- GET `localhost:5000/lerTag/<id>`
- GET `localhost:5000/lerTagPorNome/<nome>`
- DELETE `localhost:5000/removerTag/<id>`
- PUT `localhost:5000/atualizarTag/<id>` - campos json: campos a serem atualizados
- GET `localhost:5000/listarTags`


# Importar dados de CSV para API

Rode o seguinte comando no terminal

```
python Api_python/importar_dados_csv.py <caminho_do_arquivo_csv>
```
