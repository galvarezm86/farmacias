import builtwith as builtwith
import whois

# Se analizan las tecnologías con las que fueron construidas las páginas web:

tech_SB = builtwith.parse('https://salcobrand.cl/')
tech_CV = builtwith.parse('https://www.cruzverde.cl/')
tech_FA = builtwith.parse('https://farmaciasahumada.cl/')

# Se muestra las tecnologías usadas en cada página Web

print('Las tecnologías usadas en cada sitio web son: \n \n SalcoBrand: \n', tech_SB, '\n \n Cruz Verde: \n', tech_CV,
      '\n \n Farmacias Ahumada: \n', tech_FA)

# Se analiza información de la página

whois_SB = whois.whois('https://salcobrand.cl')
whois_CV = whois.whois('https://cruzverde.cl')
whois_FA = whois.whois('https://farmaciasahumada.cl')

# Se muestra información de la página

print('SalcoBrand: \n', whois_SB, '\n Cruz Verde: \n', whois_CV, '\n Farmacias ahumada: \n', whois_FA)

# AQUI HAY QUE ARREGLAR LA PARTE DE LOS WHOIS YA QUE ARROJA UN ERROR