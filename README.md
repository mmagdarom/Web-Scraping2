Práctica 1: Web Scraping con Python

Descripción

La presente práctica pertenece a la asignatura de Topología y Ciclo de Vida de los Datos de la maestría Ciencia de Datos de la UOC.
En esta práctica, hemos aplicado técnicas de web scraping en el lenguaje Python, con el objetivo de extraer información y obtener el dataset de dos sitios web de las instituciones financieras: JEP (Juventud Ecuatoriana Progresista) y CCCA (Cooperativa de Ahorro y Crédito Cámara de Comercio de Ambato).

Lo anterior, es de gran utilidad para que la comunidad ecuatoriana conozca y tome la decisión de apertura o cierre de cuentas en alguna de las 2 entidades financieras que son reconocidas a nivel del país.

Miembros del equipo

Las integrantes que ejecutamos el desarrollo de la presente práctica somos:
-	María Magdalena Romero Guzmán
-	María Augusta Jimbo Granda

Ficheros del código fuente y DataSet
- codigo/MainCoop.py, clase principal del scraping, aquí llama a ScrapingCoop.py que contiene la clase ProductosScraper().
- codigo/ScrapingCoop.py, Contiene la implementación de la clase ProductosScraper(), cuyos métodos obtienen los urls utilizados en cada página para poder obtener los productos, beneficios y 5 agencias de las dos cooperativas.
- csv/DataSetCoop.csv, se encuentra el archivo DataSet con los datos del scraping
- pdf/ CaractDataSetCoopMRMJ.pdf, se encuentra el archivo con las características del DataSet

Se debe instalar las siguientes librerias:
- pip install bs4
- pip install requests
- pip install lxml

Para ejecutar se ingresa donde se tiene el código y se ejecuta desde el cmd: python MainCoop.py

Recursos
- Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
- Masip, D. (2010). El lenguaje Python. Editorial UOC.
- El lenguaje Python.
- https://www.ccca.fin.ec/index.php
- https://www.coopjep.fin.ec/inicio
