import urllib
import builtwith as builtwith
import whois

# Se descargan los archivos robots.txt de cada sitio web.
robots_sb = 'https://salcobrand.cl/robots.txt'
robots_cv = 'https://cruzverde.cl/robots.txt'
robots_ah = 'https://farmaciasahumada.cl/robots.txt'
urllib.request.urlretrieve(robots_sb, "sb_robots.txt")
urllib.request.urlretrieve(robots_cv, "cv_robots.txt")
urllib.request.urlretrieve(robots_ah, "ah_robots.txt")

# Se analizan las tecnologías con las que fueron construidas las páginas web.
tech_SB = builtwith.parse('https://salcobrand.cl/')
tech_CV = builtwith.parse('https://www.cruzverde.cl/')
tech_FA = builtwith.parse('https://farmaciasahumada.cl/')

# Se muestra las tecnologías usadas en cada página Web.
print('Las tecnologías usadas en cada sitio web son: \n \n SalcoBrand: \n', tech_SB, '\n \n Cruz Verde: \n', tech_CV,
      '\n \n Farmacias Ahumada: \n', tech_FA)

# Se analiza información de la página.
whois_SB = whois.whois('https://salcobrand.cl')
whois_CV = whois.whois('https://cruzverde.cl')
whois_FA = whois.whois('https://farmaciasahumada.cl')

# Se muestra información de la página.
print('Información del sitio \n \n SalcoBrand: \n', whois_SB, '\n Cruz Verde: \n', whois_CV, '\n Farmacias Ahumada: \n',
      whois_FA)

