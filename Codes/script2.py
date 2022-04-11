import pandas as pd
import functions

# Se obtiene la información de la página de Farmacia Ahumada
url = 'https://www.farmaciasahumada.cl/pub/sitemap.xml'

ah1 = functions.crawl_sitemap_ah(url, time_sleep=3)

ah = pd.DataFrame(columns=['Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
ah = ah.append(ah1, ignore_index=True)

# Se exporta a un csv
ah.to_csv('Ahumada.csv', encoding='utf-8')
