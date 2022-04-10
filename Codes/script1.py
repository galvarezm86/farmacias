import pandas as pd
import functions
import warnings
import glob
import os

# Se obtiene la información de la página de SalcoBrand recorriendo los 12 sitemaps con enlaces de productos.

sb1 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap2.xml', time_sleep=3)
sb2 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap3.xml', time_sleep=3)
sb3 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap4.xml', time_sleep=3)
sb4 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap5.xml', time_sleep=3)
sb5 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap6.xml', time_sleep=3)
sb6 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap7.xml', time_sleep=3)
sb7 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap8.xml', time_sleep=3)
sb8 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap9.xml', time_sleep=3)
sb9 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap10.xml', time_sleep=3)
sb10 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap11.xml', time_sleep=3)
sb11 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap12.xml', time_sleep=3)
sb12 = functions.crawl_sitemap_sb('https://salcobrand.cl/sitemap13.xml', time_sleep=3)

# La información de cada dataframe es guardada en un csv.

sb1.to_csv('SalcoBrand1.csv', encoding='utf-8')
sb2.to_csv('SalcoBrand2.csv', encoding='utf-8')
sb3.to_csv('SalcoBrand3.csv', encoding='utf-8')
sb4.to_csv('SalcoBrand4.csv', encoding='utf-8')
sb5.to_csv('SalcoBrand5.csv', encoding='utf-8')
sb6.to_csv('SalcoBrand6.csv', encoding='utf-8')
sb7.to_csv('SalcoBrand7.csv', encoding='utf-8')
sb8.to_csv('SalcoBrand8.csv', encoding='utf-8')
sb9.to_csv('SalcoBrand9.csv', encoding='utf-8')
sb10.to_csv('SalcoBrand10.csv', encoding='utf-8')
sb11.to_csv('SalcoBrand11.csv', encoding='utf-8')
sb12.to_csv('SalcoBrand12.csv', encoding='utf-8')

# Se consolidan todos los archivos csv en uno solo.

files_joined = os.path.join('/home/gabriel/PycharmProjects/farmacias', 'SalcoBrand*.csv')
list_files = glob.glob(files_joined)
sb = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
sb.to_csv('SalcoBrand.csv', encoding='utf-8')


# Al momento de ejecutar las siguientes líneas de código, se muestran mensajes de advertencia cada vez que se carga una
# página. Para evitar que se desplieguen, se ha decidido ignorar los mensajes de advertencia.

warnings.filterwarnings("ignore")

# Se obtiene la información de la página de Cruz Verde recorriendo los 3 sitemaps con enlaces de productos.

cv1 = functions.crawl_sitemap_cv('https://www.cruzverde.cl/sitemap_0-product.xml')
cv2 = functions.crawl_sitemap_cv('https://www.cruzverde.cl/sitemap_1-product.xml')
cv3 = functions.crawl_sitemap_cv('https://www.cruzverde.cl/sitemap_2-product.xml')

# La información de cada dataframe es guardada en un csv.

cv1.to_csv('CruzVerde1.csv', encoding='utf-8')
cv2.to_csv('CruzVerde2.csv', encoding='utf-8')
cv3.to_csv('CruzVerde3.csv', encoding='utf-8')

# Se consolidan todos los archivos csv en uno solo.

files_joined = os.path.join('/home/gabriel/PycharmProjects/farmacias', 'CruzVerde*.csv')
list_files = glob.glob(files_joined)
cv = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
cv.to_csv('CruzVerde.csv', encoding='utf-8')
