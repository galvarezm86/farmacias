import re
from datetime import datetime
from typing import Any

from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4.element import ResultSet


url='https://www.farmaciasahumada.cl/pub/sitemap.xml'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

paginas = soup.find_all('loc')
lpaginas = list()

ah = pd.DataFrame(columns=['Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])

pattern = 'deprecated'
for i in paginas:
    if len(i.text)>32:
        if not re.search(pattern, i.text):
            #lpaginas.append(i.text)

            url = i.text
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            fixed_html = soup.prettify()
            try:
                info = re.findall('var dlObjects = (.*?);', fixed_html)[0]
                info = info.replace('null', '"Null"')

                name = re.findall('"name":"(.*?)",', info)[0]
                sku = re.findall('"id":"(.*?)",', info)[0]
                precio = re.findall('"price":"(.*?)",', info)[0]
                date = datetime.now().date()
            except:
                #print('Download error: ')
                lpaginas.append(i.text)
                continue

            print(name)
            print(sku)
            print(precio)
            normal_price=precio
            offer_price=precio
            ah = ah.append( [str(date), 'Ahumada', name, sku, normal_price, offer_price], ignore_index=True)

ah.to_csv('Ahumada.csv', encoding='utf-8')
