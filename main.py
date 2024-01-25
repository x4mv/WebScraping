import requests 
import bs4 
from urls import url1, url2

# Extraemos el hmtl crudo como texto 
result = requests.get(url1)


#Convertimos en un texto que sea legible
soup = bs4.BeautifulSoup(result.text, 'lxml')


# Sacamos el nombre de todos los autores de la primera pagina
autores_raw = soup.select('.author')

#filtramos el nombre solo de los autores
autores = []

for author in autores_raw:
    autores.append(author.getText())
    #autores.append(autores_raw[author])

#imprimimos los nombres de los autores de la primera pagina
for names in autores:
    print(names)


#Extraer todas las primeras quotes de la primera pagina
#filtramos la tarjeta quote entera
quotes_raw = soup.select('.quote')

#iteramos para filtrar la carta de la quote
quotes = []
for card_raw in quotes_raw:

    #filtramos el contenedor de la quote
    text_quote_raw = card_raw.select('.text')

    #filtramos solo el texto de la quote
    for text_quote in text_quote_raw:

        quotes.append(text_quote.text)

value = 1
for quote in quotes:
    print(f'{value} - {quote}')
    value += 1


#Extraer todos los tags de la caja de la derecha 
caja_raw = soup.select('.tag-item')

#iteramos para extraer los tags
tags = []

for tag in caja_raw:
    tags.append(tag.getText()[1:-1])


for item in tags:
    print(item)


#Extraer todos los autores distintos de las paginas

autores_distintos = []


for pagina in range(1,11):

    url = url2.format(pagina)

    content = requests.get(url)

    sopa = bs4.BeautifulSoup(content.text, 'lxml')

    autores_por_pagina = sopa.select('.author')

    for autor in autores_por_pagina:
        
        if autor.getText() not in autores_distintos:
            autores_distintos.append(autor.getText())
        
            

        


print(len(autores_distintos))