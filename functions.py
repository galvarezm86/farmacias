import re
import time
from datetime import datetime
from urllib import error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Se crea una función para descargar una página
# Se usó parte del código propuesto en el libro, pero con librerías de python 3


def download(url, user_agent='wswp', num_retries=2):
    request = Request(url)
    request.add_header('User_agent', user_agent)
    try:
        html = urlopen(request).read()
    except error as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, user_agent, num_retries - 1)
    return html


# Se crean funciones que rescaten el nombre del producto, su sku, el precio normal y el precio en oferta

# La siguiente es la función para rescatar la información desde las páginas de la farmacia Salcobrand


def scrap_sb(html):
    soup = BeautifulSoup(html, 'html.parser')
    fixed_html = soup.prettify()
    name = re.findall('<meta content="(.*?)" property="og:title"/>', fixed_html)[0]
    info = re.findall('var prices = (.*?);', fixed_html)[0]
    info = info.replace('null', '"Null"')
    sku = info[2:8]
    prices = eval(info[10:-1])
    normal_price = prices['normal']
    offer_price = prices['oferta']
    date = datetime.now().date()
    return [str(date), 'SalcoBrand', name, sku, normal_price, offer_price]


# AQUI FALTAN LAS FUNCIONES PARA LAS PAGINAS DE FARMACIAS AHUMADA Y CRUZ VERDE

# Se crean funciones que permitan navegar y descargar las páginas a través del sitemap.
# Utilizando las funciones anteriores, se rescata la información Y se guarda en un dataframe

# La siguiente es la función para la farmacia SalcoBrand


def crawl_sitemap_sb(url, time_sleep=3):
    df = pd.DataFrame(columns=['Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty,re.DOTALL)
    for enlace in links:
        link = enlace[4:-2]
        html = download(link)
        info = scrap_sb(html)
        df.loc[len(df)] = info
        time.sleep(time_sleep)
    return df

# AQUI FALTAN LAS FUNCIONES PARA LOS SITEMAPS DE LA FARMACIA AHUMADA Y CRUZVERDE
