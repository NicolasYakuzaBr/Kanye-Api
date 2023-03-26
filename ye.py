import requests
from googletrans import Translator, constants

#-- Puxa os dados do site 

response = requests.get("https://api.kanye.rest/")
response.raise_for_status()
data = response.json()
quote = data ["quote"]

#--- Mostra as informações vinda deste site

print("\n\n*************\n\n")
print('Tweets do Kanye West')
print("Em inglês: ", quote)

#---- Traduz para Português porque na escola a gente só estudou o verbo to be 

traduzir = Translator()
tradução = traduzir.translate(quote, dest="pt")
print("Em português: ", f"{tradução.text}" )
print("\n\n*************\n\n")























