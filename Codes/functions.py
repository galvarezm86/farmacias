import re
import time
from datetime import datetime
from urllib import error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# Se crea una función para descargar una página utilizando la librería urllib.
# Se usó parte del código propuesto en el libro, pero con librerías de python 3.


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

# Se crea una segunda función para descargar páginas basadas en javascript, utilizando la librería Selenium.


def download2(url, num_retries=2):
    # Se intenta abrir la url utilizando webdriver y el navegador Firefox.
    try:
        browser = webdriver.Firefox()
        browser.get(url)
        # Se da un tiempo para que la página cargue toda la información, de lo contrario no se podrá guardarn el html.
        time.sleep(8)
        # Se descarga el html parseado con BautifulSoup.
        soup = BeautifulSoup(browser.page_source)
        fixed_html = soup.prettify()
        # Se cierra el navegador.
        browser.close()
    # Si no se logra abrir la url debido a un error de servidor, se espera 30 segundos y se vuelve a intentar.
    # Este proceso se repite dos veces, si no se logra establecer conexión, se retorna "None".
    except error as e:
        print('Download error: ', e.reason)
        fixed_html = None
        if num_retries > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            time.sleep(30)
            return download2(url, num_retries - 1)
    return fixed_html

# Se crean funciones que rescaten el nombre del producto, su sku, el precio normal y el precio en oferta.
# La siguiente es la función para rescatar la información desde una página de farmacias Salcobrand a partir del html
# que retorna la función download.


#Funciones para Salco Brand
def scrap_sb(html):
    soup = BeautifulSoup(html, 'html.parser')
    fixed_html = soup.prettify()
    # Se intenta buscar el tag donde se encuentra el nombre del producto.
    try:
        name = re.findall('<meta content="(.*?)" property="og:title"/>', fixed_html)[0]
    # Si no se encuentra, se retorna "Null".
    except:
        name = "Null"
    # Se intenta buscar el tag donde se encuentra el sku y los precios del producto.
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
    # Si no se encuentra, se retorna "Null".
    except:
        normal_price = "Null"
        offer_price = "Null"
        sku = "Null"
    # Se guarda la fecha actual para incluirla en el registro.
    date = datetime.now().date()
    # La función retorna la fecha, el nombre de la farmacia, el nombre del producto, el sku y los precios.
    return [str(date), 'SalcoBrand', name, sku, normal_price, offer_price]

# La siguiente es la función para rescatar la información desde una página de farmacias Salcobrand a partir del html
# que retorna la función download2.

#Funciones para Cruz Verde
def scrap_cv(html, link):
    # Se intenta buscar el tag donde se encuentra el nombre del producto
    try:
        name = re.findall('<meta content="(.*?)" name="og::image:alt"/>', html)[0]
    # Si no se encuentra, se retorna "Null".
    except:
        name = "Null"
    # Se intenta buscar el tag donde se encuentran los precios del producto, admás, se rescata el sku desde la dirección
    # del enlace.
    try:
        offer_price = re.findall('\$ (.*?)\n', html)[0]
        normal_price = re.findall('\$ (.*?) \(Normal\)', html)[0]
        start_sku = re.search('./\d(.*?).html', link).start() + 2
        end_sku = re.search('./\d(.*?).html', link).end() - 5
        sku = link[start_sku:end_sku]
    # Si no se encuentra, se retorna "Null".
    except:
        normal_price = "Null"
        offer_price = "Null"
        sku = "Null"
    # Se guarda la fecha actual para incluirla en el registro.
    date = datetime.now().date()
    # La función retorna la fecha, el nombre de la farmacia, el nombre del producto, el sku y los precios.
    return [str(date), 'Cruz Verde', name, sku, normal_price, offer_price]


#Funciones para Ahumada
def scrap_ah(html):
    soup = BeautifulSoup(html, 'html.parser')
    fixed_html = soup.prettify()
    info = re.findall('var dlObjects = (.*?);', fixed_html)[0]
    info = info.replace('null', '"Null"')
    try:
        name = re.findall('"name":"(.*?)",', info)[0]
    except:
        name = 'N/A'
    try:
        sku = re.findall('"id":"(.*?)",', info)[0]
    except:
        sku = 'N/A'
    try:
        normal_price = re.findall('"price":"(.*?)",', info)[0]
    except:
        normal_price = 'N/A'
    try:
        offer_price = re.findall('"price":"(.*?)",', info)[0]
    except:
        offer_price = 'N/A'
    return ['Ahumada', name, sku, normal_price, offer_price]


# Se crean funciones que permitan navegar y descargar las páginas a través del sitemap.
# Utilizando las funciones anteriores, se rescata la información requerida y se guarda en un dataframe.

# La siguiente es la función para la farmacia SalcoBrand.


def crawl_sitemap_sb(url, time_sleep=3):
    # Se crea un dataframe para guardar la información.
    df = pd.DataFrame(columns=['Fecha', 'Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    # Se descarga el mapa del sitio y se parsea con Beautiful Soup.
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    # Se encuentran todos los enlaces que contiene el mapa del sitio.
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty, re.DOTALL)
    # Se recorren todos los enlaces de los productos, descargando la página y recopilando la información útil.
    # Los primeros dos enlaces no corresponden a productos, por lo que se omiten del recorrido.
    for enlace in links[2:-1]:
        start = re.search("h", enlace).start()
        end = re.search(".\n", enlace).end()
        link = enlace[start:end - 1]
        html = download(link)
        info = scrap_sb(html)
        # La información es guardada en el dataframe.
        df.loc[len(df)] = info
        # Se espera un tiempo prudente para no colapsar el servidor.
        time.sleep(time_sleep)
    # La función retorna el dataframe con la información de todos los productos.
    return df

# La siguiente es la función para la farmacia SalcoBrand.


def crawl_sitemap_cv(url):
    # Se crea un dataframe para guardar la información.
    df = pd.DataFrame(columns=['Fecha', 'Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    # Se descarga el mapa del sitio y se parsea con Beautiful Soup.
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    # Se encuentran todos los enlaces que contiene el mapa del sitio.
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty, re.DOTALL)
    # Se recorren todos los enlaces de los productos, descargando la página y recopilando la información útil.
    for enlace in links:
        start = re.search("h", enlace).start()
        end = re.search(".\n", enlace).end()
        link = enlace[start:end - 1]
        html = download2(link)
        info = scrap_cv(html, link)
        # La información es guardada en el dataframe.
        df.loc[len(df)] = info
        # En este caso no se espera un tiempo entre peticiones, ya que la función download2 ya considera un tiempo de
        # espera para que las páginas se carguen.
    # La función retorna el dataframe con la información de todos los productos.
    return df

#Funciones para Ahumada
def crawl_sitemap_ah(url, time_sleep=3):
    df = pd.DataFrame(columns=['Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
    sitemap = download(url)
    soup = BeautifulSoup(sitemap, 'html.parser')
    sitemap_pretty = soup.prettify()
    links = re.findall('<loc>(.*?)</loc>', sitemap_pretty, re.DOTALL)
    #no estamos considerando los productos descontinuados, estos tienen en el nonbre de la url, el texto "deprecated".
    pattern = 'deprecated'
    for enlace in links:
        link = enlace[4:-2]
        if len(link) <= 38:
            continue
        if re.search(pattern, link):
            continue
        try:
            html = download(link)
        except:
            continue
        info = scrap_ah(html)
        df.loc[len(df)] = info
        time.sleep(time_sleep)
    return df
