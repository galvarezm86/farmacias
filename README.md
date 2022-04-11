# Tipología y ciclo de vida de los datos

# 'PRÁCTICA 1: Web scrapping'
Autores: Gabriel Álvarez Morgado y Héctor Castillo Jeria

## El objetivo de este práctico es obtener los productos y sus respectivos precios de las 3 principales cadenas de farmacias de Chile


Los archivos del repositorio se encuentran organizados de la siguiente manera:

Archivo Practica1.pdf: Archivo con el desarrollo de las respuestas a los apartados 1-10 solicitados en la práctica.

Carpeta Codes: Carpeta con los códigos necesarios para la correcta ejecución de los script para obtener la información. Dentro de ella se encuentran los siguientes archivos:

	requirements.txt: Archivo de texto que muestra las librerías de Python necesarias para ejecutar correctamente los scripts.
	info_pages.py: script que permite mostrar información relevante de las páginas a explorar. Descarga los archivos robots.txt, muestra las tecnologías con las que fueron construidos los sitios y los propietarios de las páginas.
	functions.py: Archivo que define funciones que serán utilizadas en el script1.
	script1.py: Script que realiza un web scrapping a las páginas de las farmacias SalcoBrand y Cruz Verde, obteniendo el nombre de los productos, su código interno único (SKU), el precio normal y el precio en oferta. Posteriormente guarda la información de todos los productos en archivos csv.
	script2.py: Script que realiza un web scrapping a las páginas de las farmacias Ahumada, obteniendo el nombre de los productos, su código interno único (SKU), el precio normal y el precio en oferta. Posteriormente guarda la información de todos los productos en un archivo csv.

	
Carpeta Data: Carpeta con los archivos csv obtenidos tras el proceso de web scrapping. Dentro de ella se encuentran los siguientes archivos:

	Ahumada.csv: Archivo con 9813 registros correspondientes a los productos ofrecidos por Farmacias Ahumada, con su respectivo precio normal y de oferta.
	CruzVerde.csv: Archivo con 10729 registros correspondientes a los productos ofrecidos por Farmacias Cruz Verde, con su respectivo precio normal y de oferta.
	SalcoBrand.csv: Archivo con 13189 registros correspondientes a los productos ofrecidos por Farmacias SalcoBrand, con su respectivo precio normal y de oferta.


Además de encontrarse en la carpeta Data, los 3 archivos descritos anteriormente se encuentran en un repositorio de Zenodo, cuyo DOI es: 10.5281/zenodo.6441879


Para la correcta ejecución del script1, es necesario contar con el navegador Firefox, además de tener el driver Geckodriver instalado en la carpeta "Bin" (linux) o "Scripts" (windows), las que se encuentran dentro del fichero "Venv" correspondiente al environment del proyecto. El driver puede descargarse desde https://github.com/mozilla/geckodriver.

En el archivo LICENSE se encuentra información sobre la licencia del proyecto.
