import pandas as pd

import functions

# Se obtiene la información de la página de SalcoBrand

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

# Se condensa en un solo DataFrame

sb = pd.DataFrame(columns=['Farmacia', 'Producto', 'SKU', 'Normal', 'Oferta'])
sb = sb.append(sb1, ignore_index=True)
sb = sb.append(sb2, ignore_index=True)
sb = sb.append(sb3, ignore_index=True)
sb = sb.append(sb4, ignore_index=True)
sb = sb.append(sb5, ignore_index=True)
sb = sb.append(sb6, ignore_index=True)
sb = sb.append(sb7, ignore_index=True)
sb = sb.append(sb8, ignore_index=True)
sb = sb.append(sb9, ignore_index=True)
sb = sb.append(sb10, ignore_index=True)
sb = sb.append(sb11, ignore_index=True)
sb = sb.append(sb12, ignore_index=True)

# Se exporta a un csv

sb.to_csv('SalcoBrand.csv', encoding='utf-8')

# AQUÍ FALTA HACER LO MISMO PARA CRUZVERDE Y FARMACIAS AHUMADA
