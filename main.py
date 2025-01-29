import requests
from datetime import datetime

cotacoes = requests.get('http://economia.awesomeapi.com.br/last/USD-BRL')

requisicao_dic = cotacoes.json()
cotacao_dolar = requisicao_dic['USDBRL']['bid']

print(f"Cotação Dólar Atualizada: {datetime.now()} \n Dólar: R${cotacao_dolar}")
