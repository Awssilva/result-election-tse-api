import requests
import json
import pandas as pd
from time import sleep

data = requests.get(
    "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
)
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for infos in json_data['cand']:
    if infos['seq'] in '1 2 3 4'.split(' '):
        candidato.append(infos['nm'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])
while True:
  df_eleicao = pd.DataFrame(
          list(zip(candidato, votos, porcentagem)),
          columns=['Candidato', 'Nº votos', 'Porcentagem']
  )
  print(df_eleicao)
  sleep(10)
