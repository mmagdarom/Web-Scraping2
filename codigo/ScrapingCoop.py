'''
Created on 1 abr. 2018

@author: Magdalena y Augusta
'''
from bs4 import BeautifulSoup
import requests
import unicodedata
from bs4.element import Tag
import time
class ProductosScraper():
    def __init__(self):
        self.urlcoop1 = "https://www.coopjep.fin.ec"
        self.urlcoop2 = "https://www.ccca.fin.ec"
        self.prodreqben = []
        self.nombrecoop1 = []
        self.nombrecoop2 = [] 
            
    def __cargarhtml(self,urlcoop):
        r = requests.get(urlcoop)
        datahtml = r.text
        souplink = BeautifulSoup(datahtml, 'lxml')
        return souplink
    
    #obtener los urls de los productos de la coop1 JEP
    def __obtenerLinkProdCoop1(self, soupl):
        link_prod = []
        link_prod1 = []
        titulocoop = soupl.find('title')
        self.nombrecoop1 = titulocoop.text
        menu_prod = soupl.find_all('li', class_="fa fa-angle-right")
        for i in menu_prod:
            link_prod = i.find('a',href=True)
            #se obtienen solo los links de los productos y agencias
            if 'ahorros' in link_prod.get('href') or 'creditos' in link_prod.get('href') or 'agencias' in link_prod.get('href'):
                link_prod1.append(self.urlcoop1+link_prod.get('href'));
        return link_prod1
    
    #para obtener los urls de los productos de la coop2 CCCA
    def __obtenerLinkProdCoop2(self, soupl):
        link_prod = []
        link_prod1 = []
        titulocoop2 = soupl.find('title')
        self.nombrecoop2 = titulocoop2.text
        #se realiza diferentes analisis de la pagina porque existen multiples url y se obtuvo por el tipo de producto
        menu_ahorros = soupl.find_all('li', class_="item143 parent grouped")
        for i in menu_ahorros:
            link = i.findAll('li')
            for l in link:
                link_prod = l.find('a',href=True)
                #se eliminaron de las listas estas condiciones ya que estos productos se encuentran en una imagen
                if 'javascript' not in link_prod.get('href') and 'dueno-y-senor' not in link_prod.get('href') and 'chequera' not in link_prod.get('href') and 'cuenta-corriente' not in link_prod.get('href'):
                    link_prod1.append(self.urlcoop2+link_prod.get('href'));
        menu_creditos = soupl.find_all('li', class_="item144 parent grouped")
        for i in menu_creditos:
            link = i.findAll('li')
            for l in link:
                link_prod = l.find('a',href=True)
                #se eliminaron de las listas estas condiciones ya que estos productos se encuentran en una imagen
                if 'javascript' not in link_prod.get('href') and 'credito-auto' not in link_prod.get('href'):
                    link_prod1.append(self.urlcoop2+link_prod.get('href'))
        menu_creditos1 = soupl.find_all('li', class_="item211 parent grouped")
        for i in menu_creditos1:
            link = i.findAll('li')
            for l in link:
                link_prod = l.find('a',href=True)
                if 'javascript' not in link_prod.get('href'):
                    link_prod1.append(self.urlcoop2+link_prod.get('href'))
        menu_agencias = soupl.find_all('li', class_="item256")
        for i in menu_agencias:
            link_prod = i.find('a',href=True)
            if 'javascript' not in link_prod.get('href'):
                link_prod1.append(self.urlcoop2+link_prod.get('href'))   
        return link_prod1
    
    #funcion para eliminar las tildes
    def __borrar_tildes(self, texto):
        return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    
    #funcion para obtener tipo de producto, producto, requisitos, beneficios y agencias de Coop1 JEP
    def __obtenerReqBen_Agencias(self, soupl, urllink, soupage):
        tipo_prod = soupl.find('h1')
        prod_reqben = soupl.find_all('div', class_="JEP_plantillaPS_textos")
        prod_reben = []
        prod_reben.append(self.__borrar_tildes(self.nombrecoop1[8:]))
        if 'ahorros' in urllink:
            prod_reben.append("Ahorros")
        else:
            if 'creditos' in urllink:
                prod_reben.append("Creditos")
        prod_reben.append(self.__borrar_tildes(tipo_prod.text))
        
        #obtener requisitos y beneficios
        for pr in prod_reqben:
            des = pr.find('p')
            des1 = pr.find_all('ul')
            #es la caracteristica o descripcion del producto
            prod_reben.append(self.__borrar_tildes(des.text))
            cont = 0
            #identificador para obtener los requisitos y beneficios segun el producto, ya que el producto
            #microtransporte tiene diferente a los demas
            if 'microtransporte' in urllink:
                idreq = 1
                idben = 0
            else:
                idreq = 0
                idben = 1
        #se obtienen los requisitos
        for rq in des1[idreq]:
            #para ignorar datos con null o que no sean string y poder obtener los datos reales
            if isinstance(rq, Tag):
                a = rq.find('a',href=True)
                if cont < 3:
                    #para agregar el texto del href del requisito del producto en el caso que exista 
                    if 'Apertura de cuenta' in self.__borrar_tildes(rq.find(text=True)):
                        prod_reben.append(self.__borrar_tildes(rq.find(text=True))+self.__borrar_tildes(a.text))
                        cont = cont + 1
                    else:
                        prod_reben.append(self.__borrar_tildes(rq.find(text=True)))
                        cont = cont + 1
                else:
                    break
        #se agrega NR en el caso que no existan 3 requisitos
        for con in range(len(prod_reben), 7):
            prod_reben.append('NR')
        #se obtienen los beneficios
        cont = 0
        if len(des1) > 1:
            for rq1 in des1[idben]:
                #para ignorar datos con null que no sean string y poder obtener los datos reales
                if isinstance(rq1, Tag):
                    if cont < 3:
                        prod_reben.append(self.__borrar_tildes(rq1.find(text=True)))
                        cont = cont + 1
                    else:
                        break
        #se agrega NB en el caso que no existan 3 beneficios o el producto no tenga beneficios
        for con1 in range(len(prod_reben), 10):
            prod_reben.append('NB')
        #obtener agencias    
        agencias = soupage.find_all('div', class_="JEP_Agencias_dots")
        #contador para insertar solo 5 agencias
        conta = 0
        for ag in agencias:
            agen = ag.find(text=True)
            if (conta <= 4):
                prod_reben.append(self.__borrar_tildes(agen))
                conta = conta+1
            else:
                break
        print prod_reben
        return prod_reben
    
    #funcion para obtener tipo de producto, producto, requisitos, beneficios y agencias de Coop2 CCCA
    def __obtenerReqBen_Agencias_Coop2(self, soupl, urllink, soupage):
        tipo_prod1 = soupl.find('title')
        prod_ahocre = []
        prod_ahocre.append(self.__borrar_tildes(self.nombrecoop2))
        if 'cuentas' in urllink:
            prod_ahocre.append("Ahorros")
        else:
            if 'creditos' in urllink:
                prod_ahocre.append("Creditos")
        tituloprod = tipo_prod1.text
        prod_ahocre.append(self.__borrar_tildes(tituloprod[17:]).encode('ascii','ignore').decode('ascii'))
        if 'cuentas' in urllink:
            #se obtiene la caracteristica o descripcion del producto
            caracteristica = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane active")
            for j in caracteristica:
                a = j.find('p')
                prod_ahocre.append(self.__borrar_tildes(a.text).encode('ascii','ignore').decode('ascii'))
            requisitos = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane")
            cont = 0
            for j in requisitos:
                reqc2 = j.findAll('p')
                rebe = j.find('h2')
                for k in reqc2:
                    #se obtienen los requisitos
                    if rebe.text == 'REQUISITOS':
                        if cont < 3:
                            if 'Requisitos personas naturales' not in k.find(text=True):
                                #se le coloco el ascci ignore, luego de borrar las tildes porque habian textos con caracteres especiales
                                #y no dejaba grabar en el archivo
                                prod_ahocre.append(self.__borrar_tildes(k.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                cont = cont + 1
                    #se obtienen los beneficios
                    if rebe.text == 'beneficios1':
                        if cont >= 3 and cont < 6:
                            prod_ahocre.append(self.__borrar_tildes(k.findNext(text=True)).encode('ascii','ignore').decode('ascii'))
                            cont = cont + 1
                        else:
                            break
        else:
            if 'creditoeducativo' in urllink or 'casafacil' in urllink or 'cooperativa-3' in urllink:
                #se obtiene el primer beneficio como caracteristica del producto
                caracteristicac = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane active")
                for j1 in caracteristicac:
                    reqc3 = j1.find('span')
                    prod_ahocre.append(self.__borrar_tildes(reqc3.text).encode('ascii','ignore').decode('ascii'))
                requisitosc = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane")
                cont = 0
                for j2 in requisitosc:
                    reqc3 = j2.findAll('li')
                    rebe = j2.find('h2')
                    for k in reqc3:
                        if rebe.text == 'REQUISITOS':
                            if cont < 3:
                                #se controla que no obtenga los \n
                                if '\n' not in k.find(text=True):
                                    prod_ahocre.append(self.__borrar_tildes(k.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                    cont = cont + 1
                            else:
                                break
                #se agrega NR en el caso que no existan 3 requisitos
                for con2 in range(len(prod_ahocre), 7):
                    prod_ahocre.append('NR')
                #se obtienen los beneficios
                beneficiosc = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane active")
                if 'microcreditos' not in urllink:
                    cont = 0
                    for j3 in beneficiosc:
                        reqc4 = j3.findAll('li')
                        rebe1 = j3.find('h2')
                        for k1 in reqc4:
                            if rebe1.text == 'beneficios1':
                                if cont >= 1 and cont < 4:
                                    #se controla que no obtenga los \n
                                    if '\n' not in k1.find(text=True) and 'creditos' not in self.__borrar_tildes(k1.find(text=True)):
                                        prod_ahocre.append(self.__borrar_tildes(k1.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                        cont = cont + 1
                                else:
                                    if cont == 0:
                                        cont = cont + 1
                                    else:
                                        break
                else:
                    cont = 0
                    for j7 in beneficiosc:
                        reqc8 = j7.findAll('span')
                        rebe3 = j7.find('h2')
                        for k5 in reqc8:
                            if rebe3.text == 'beneficios1':
                                if cont >= 1 and cont < 4:
                                    #se controla que no obtenga los \n
                                    if '\n' not in k5.find(text=True) and 'creditos' not in self.__borrar_tildes(k5.find(text=True)):
                                        prod_ahocre.append(self.__borrar_tildes(k5.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                        cont = cont + 1
                                else:
                                    if cont == 0:
                                        cont = cont + 1
                                    else:
                                        break
                #se agrega NB en el caso que no existan 3 beneficios o el producto no tenga beneficios
                for con3 in range(len(prod_ahocre), 10):
                    prod_ahocre.append('NB')
            else:
                if 'credito-de-consumo' in urllink:
                    caracteristicaco = soupl.find_all('div', class_="component-content")
                    cont = 0
                    #se obtiene el primer beneficio como caracteristica del producto
                    for j4 in caracteristicaco:
                        reqc5 = j4.findAll('li')
                        for k2 in reqc5:
                            if cont == 1:
                                #se controla que no obtenga los \n
                                if '\n' not in k2.find(text=True):
                                    prod_ahocre.append(self.__borrar_tildes(k2.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                    cont = cont + 1
                            else:
                                if cont == 0:
                                    cont = cont + 1
                                else:
                                    break
                    #se obtienen los requisitos
                    requisitosco = soupl.find_all('div', class_="tab-pane rl_tabs-pane nn_tabs-pane active")
                    cont = 0
                    for j5 in requisitosco :
                        reqc6 = j5.findAll('li')
                        rebe2 = j5.find('h2')
                        for k3 in reqc6:
                            if rebe2.text == 'REQUISITOS':
                                if cont < 3:
                                    #se controla que no obtenga los \n
                                    if '\n' not in k3.find(text=True):
                                        prod_ahocre.append(self.__borrar_tildes(k3.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                        cont = cont + 1
                                else:
                                    break
                    #se agrega NR en el caso que no existan 3 requisitos
                    for con4 in range(len(prod_ahocre), 7):
                        prod_ahocre.append('NR')
                    #se obtienen los beneficios
                    beneficiosco = soupl.find_all('div', class_="component-content")
                    cont = 0
                    for j6 in beneficiosco :
                        reqc7 = j6.findAll('li')
                        for k4 in reqc7:
                            if cont >= 1 and cont < 4:
                                #se controla que no obtenga los \n
                                if '\n' not in k4.find(text=True) and 'creditos' not in self.__borrar_tildes(k4.find(text=True)):
                                    prod_ahocre.append(self.__borrar_tildes(k4.find(text=True)).encode('ascii','ignore').decode('ascii'))
                                    cont = cont + 1
                            else:
                                if cont == 0:
                                    cont = cont + 1
                                else:
                                    break
                    #se agrega NB en el caso que no existan 3 beneficios o el producto no tenga beneficios
                    for con5 in range(len(prod_ahocre), 10):
                        prod_ahocre.append('NB')
        #obtener agencias
        agencias = soupage.find_all('div', class_="component-content")
        #contador para insertar solo 5 agencias
        conta = 0
        for ag in agencias:
            agent = ag.findAll('strong')
            for ag1 in agent:
                if conta >= 2 and conta < 7:
                    #para que no se guarden datos de telefonos, solo agencias
                    if '(' not in ag1.find(text=True):
                        prod_ahocre.append(self.__borrar_tildes(ag1.find(text=True)).encode('ascii','ignore').decode('ascii'))
                        conta = conta+1
                else:
                    if conta == 0 or conta == 1:
                        conta = conta + 1
                    else:
                        break  
        print prod_ahocre               
        return prod_ahocre 
                                  
       
    #funcion para realizar el scraping de todos los productos    
    def scraperProd(self):    
        #para comprobar el tiempo que se demora en realizar el scraping
        #inicia time
        iniciar_time = time.time()
        #primera coop JEP
        bs = self.__cargarhtml(self.urlcoop1)
        link_productos = []
        link_productos = self.__obtenerLinkProdCoop1(bs)
        cabListaProd = ['Coop Ahorro y Credito','Tipo de Producto','Producto','Caracteristica','Requisito1','Requisito2','Requisito3','Beneficio1','Beneficio2','Beneficio3','Agencia Matriz','Agencia2','Agencia3','Agencia4','Agencia5']
        self.prodreqben.append(cabListaProd)
        print 'Productos de la Coop JEP'
        for i in range(0, len(link_productos)-1):
            bsp = self.__cargarhtml(link_productos[i])
            #es el link de la agencias de la coop1
            bspagencias = self.__cargarhtml(link_productos[len(link_productos)-1])
            self.prodreqben.append(self.__obtenerReqBen_Agencias(bsp, link_productos[i], bspagencias))
        #segunda coop CCCA
        bs1 = self.__cargarhtml(self.urlcoop2)
        link_productos1 = []
        link_productos1 = self.__obtenerLinkProdCoop2(bs1)
        print 'Productos de la Coop CCCA'
        for i in range(0, len(link_productos1)-1):
            bsp1 = self.__cargarhtml(link_productos1[i])
            #es el link de las agencias de la coop2
            bspagencias1 = self.__cargarhtml(link_productos1[len(link_productos1)-1])
            self.prodreqben.append(self.__obtenerReqBen_Agencias_Coop2(bsp1, link_productos1[i], bspagencias1))
        #fin time
        fin_time = time.time()
        print 'Tiempo estimado para scraping es: ' + str(round(((fin_time - iniciar_time) / 60) , 2)) + ' minutos'
    
    #funcion para grabar los datos en el archivo DataSet        
    def grabarDataset(self, filecsv):
        filedat = open("../" + filecsv, "w+")
        for i in range(0, len(self.prodreqben)):
            for j in range(0, len(self.prodreqben[i])):
                filedat.write(self.prodreqben[i][j])
                filedat.write(str(";"))
            filedat.write("\n")
        print 'Datos grabados correctamente'
        filedat.close()
            
        