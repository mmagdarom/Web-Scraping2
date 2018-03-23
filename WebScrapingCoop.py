Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requests
>>> url = "https://www.coopjep.fin.ec/inicio"
>>> r = requests.get(url)
>>> datahtml = r.text
>>> souplink = BeautifulSoup(datahtml, 'lxml')
>>> menu_prod = souplink.find_all('div', class_="JEP-footer-varios-box")
>>> print menu_prod
[<div class="JEP-footer-varios-box"> <h4>Ahorros</h4> <ul> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/ahorrosjep">AhorrosJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/fondojep">FondoJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/superjep">SuperJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/ahorros-jepito">JEPito</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/ahorrointelijep">InteliJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/ahorros/inversionesjep">InversionesJEP</a></li> </ul> </div>, <div class="JEP-footer-varios-box"> <h4>Cr\xe9ditos</h4> <ul> <li class="fa fa-angle-right"><a href="/productos-servicios/creditos/credijep">CrediJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/creditos/microjep">MicroJEP</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/creditos/credimivivienda">CrediMIVIVIENDA</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/creditos/microtransporte">MicroTransporte</a></li> <li class="fa fa-angle-right"><a href="/productos-servicios/creditos/credipymes">CrediPYMES</a></li> </ul> </div>, <div class="JEP-footer-varios-box"> <h4>Cajeros y Agencias</h4> <ul> <li class="fa fa-angle-right"><a href="/productos-servicios/tarjetas-cajeros/cajeros-automaticos">Cajeros a Nivel Nacional</a></li> <li class="fa fa-angle-right"><a href="/la-jep/cobertura/agencias">Agencias a Nivel Nacional</a></li> </ul> </div>, <div class="JEP-footer-varios-box"> <h4>Aplicaci\xf3n JEPM\xf3vil</h4> <ul> <li class="fa fa-angle-right"><a href="https://play.google.com/store/apps/details?id=com.jepmovil" target="_blank">Android</a></li> <li class="fa fa-angle-right"><a href="https://itunes.apple.com/us/app/jep-movil/id957463204?l=es&amp;ls=1&amp;mt=8" target="_blank">iOS</a></li> </ul> </div>]
>>> link_prod = []
>>> for i in menu_prod:
	link_prod.append(i.find_all('a'))

	
>>> print link_prod
[[<a href="/productos-servicios/ahorros/ahorrosjep">AhorrosJEP</a>, <a href="/productos-servicios/ahorros/fondojep">FondoJEP</a>, <a href="/productos-servicios/ahorros/superjep">SuperJEP</a>, <a href="/productos-servicios/ahorros/ahorros-jepito">JEPito</a>, <a href="/productos-servicios/ahorros/ahorrointelijep">InteliJEP</a>, <a href="/productos-servicios/ahorros/inversionesjep">InversionesJEP</a>], [<a href="/productos-servicios/creditos/credijep">CrediJEP</a>, <a href="/productos-servicios/creditos/microjep">MicroJEP</a>, <a href="/productos-servicios/creditos/credimivivienda">CrediMIVIVIENDA</a>, <a href="/productos-servicios/creditos/microtransporte">MicroTransporte</a>, <a href="/productos-servicios/creditos/credipymes">CrediPYMES</a>], [<a href="/productos-servicios/tarjetas-cajeros/cajeros-automaticos">Cajeros a Nivel Nacional</a>, <a href="/la-jep/cobertura/agencias">Agencias a Nivel Nacional</a>], [<a href="https://play.google.com/store/apps/details?id=com.jepmovil" target="_blank">Android</a>, <a href="https://itunes.apple.com/us/app/jep-movil/id957463204?l=es&amp;ls=1&amp;mt=8" target="_blank">iOS</a>]]
>>> link_prod1 =[]
>>> for i in menu_prod:
	link_prod1.append(i.get('href'))

	
>>> print link_prod1
[None, None, None, None]
>>> 
