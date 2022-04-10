import re
import time
from datetime import datetime
from urllib import error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver



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
            time.sleep(30)
            return download(url, user_agent, num_retries - 1)
    return html


# Se crean funciones que rescaten el nombre del producto, su sku, el precio normal y el precio en oferta

# La siguiente es la función para rescatar la información desde las páginas de la farmacia Salcobrand


def scrap_sb(html):
    soup = BeautifulSoup(html, 'html.parser')
    fixed_html = soup.prettify()
    try:
        name = re.findall('<meta content="(.*?)" property="og:title"/>', fixed_html)[0]
    except:
        name = "Null"
    try:
        info = re.findall('var prices = (.*?);', fixed_html)[0]
        info = info.replace('null', '"Null"')
        start_sku = re.search('\d', info).start()
        end_sku = re.search('":', info).start()
        sku = info[start_sku:end_sku]
        start_dict = re.search('\{"normal', info).start()
        end_dict = re.search('"internet"(.*?)\}', info).end()
        prices = eval(info[start_dict:end_dict])
        normal_price = prices['normal']
        offer_price = prices['oferta']
    except:
        normal_price = "Null"
        offer_price = "Null"
        sku = "Null"
    date = datetime.now().date()
    print("Completado")
    return [str(date), 'SalcoBrand', name, sku, normal_price, offer_price]


# AQUI FALTAN LAS FUNCIONES PARA LAS PAGINAS DE FARMACIAS AHUMADA Y CRUZ VERDE

# Se crean funciones que permitan navegar y descargar las páginas a través del sitemap.
# Utilizando las funciones anteriores, se rescata la información Y se guarda en un dataframe

# La siguiente es la función para la farmacia SalcoBrand


def crawl_sitemap_sb(url, time_sleep=3):
    df = pd.DataFrame(columns=['Fecha', 'Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty, re.DOTALL)
    for enlace in links[2:-1]:
        start = re.search("h", enlace).start()
        end = re.search(".\n", enlace).end()
        link = enlace[start:end - 1]
        html = download(link)
        info = scrap_sb(html)
        df.loc[len(df)] = info
        time.sleep(time_sleep)
    return df

# AQUI FALTAN LAS FUNCIONES PARA LOS SITEMAPS DE LA FARMACIA AHUMADA Y CRUZVERDE

def download2(url, num_retries = 2):
    try:
        browser = webdriver.Firefox()
        browser.get(url)
        time.sleep(8)
        soup = BeautifulSoup(browser.page_source)
        fixed_html = soup.prettify()
        browser.close()
    except error as e:
        print('Download error: ', e.reason)
        fixed_html = None
        if num_retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            time.sleep(30)
            return download2(url, num_retries - 1)
    return fixed_html


def scrap_cv(html,link):
    try:
        name = re.findall('<meta content="(.*?)" name="og::image:alt"/>', html)[0]
    except:
        name = "Null"
    try:
        offer_price = re.findall('\$ (.*?)\n', html)[0]
        normal_price = re.findall('\$ (.*?) \(Normal\)', html)[0]
        start_sku = re.search('./\d(.*?).html', link).start() + 2
        end_sku = re.search('./\d(.*?).html', link).end() - 5
        sku = link[start_sku:end_sku]
    except:
        normal_price = "Null"
        offer_price = "Null"
        sku = "Null"
    date = datetime.now().date()
    print("Completado")
    return [str(date), 'Cruz Verde', name, sku, normal_price, offer_price]



def crawl_sitemap_cv(url):
    df = pd.DataFrame(columns=['Fecha', 'Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty, re.DOTALL)
    for enlace in links[0:1000]:
        start = re.search("h", enlace).start()
        end = re.search(".\n", enlace).end()
        link = enlace[start:end - 1]
        html = download2(link)
        info = scrap_cv(html,link)
        df.loc[len(df)] = info
    return df
