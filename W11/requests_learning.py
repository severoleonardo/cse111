import requests 

######## GET ########
# requisicao = requests.get('https://request-learning-1c1c4-default-rtdb.firebaseio.com/.json')
# print(requisicao)
# print(requisicao.json())


######## POST ########
# informacoes = '{"Nome": "Amanda", "Idade": 32}'
# requisicao = requests.post('https://request-learning-1c1c4-default-rtdb.firebaseio.com/.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())


######## POST ########
# informacoes = '{"Nome": "Amanda", "Idade": 21, "Sobrenome": "Candiotto"}'
# requisicao = requests.patch('https://request-learning-1c1c4-default-rtdb.firebaseio.com/-Nkerg-4bxlIH0Y4uxle.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())

# informacoes = '{"Nome": "Amanda", "Idade": 60, "Sobrenome": "Peres"}'
# requisicao = requests.post('https://request-learning-1c1c4-default-rtdb.firebaseio.com/-Nkes6RGBONrkFRBf2eS.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())


######## DELETE ########
requisicao = requests.delete('https://request-learning-1c1c4-default-rtdb.firebaseio.com/-Nkerg-4bxlIH0Y4uxle.json')
print(requisicao)
print(requisicao.json())