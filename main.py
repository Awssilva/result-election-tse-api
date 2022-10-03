import requests
import json
import pandas as pd
import os
from time import sleep
from datetime import datetime, timedelta
clear = lambda: os.system('clear') 

data = requests.get(
    "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
)
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for infos in json_data['cand']:
    if infos['seq'] in '1 2 3 4 5 6 7 8 9 10'.split(' '):
        candidato.append(infos['nm'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])
while True:
  df_eleicao = pd.DataFrame(
  list(zip(candidato, votos, porcentagem)),
  columns=['Candidato', 'Votos', 'Porcentagem']
  )
  to_gmt3 = datetime.now() - timedelta(hours=3)
  print(f'{to_gmt3.strftime("%H:%M:%S")} - Aguarde\n')
  print(df_eleicao,'\n')
  sleep(30)
  clear()
