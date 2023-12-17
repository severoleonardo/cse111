import requests
import pprint
import pandas as pd


######## GET ########   


# pegar todas as informações com varias requisições

tabela_final = pd.DataFrame()
pular_indice = 0 

# Loop para gerar 
while True:
    link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular_indice}&$orderby=Data%20desc&$format=json"
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    tabela = pd.DataFrame(informacoes['value'])
    if len(informacoes['value']) < 1:
        break
    tabela_final = pd.concat([tabela_final, tabela])
    pular_indice += 10000


# Processamento e Apresentação
tabela_final["Quantidade"] = tabela_final["Quantidade"].map("{:,}".format)
tabela_final["Valor"] = tabela_final["Valor"].map("R${:,.2f}".format)

pprint.pprint(tabela_final)


