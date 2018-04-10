'''
Created on 1 abr. 2018

@author: Magdalena y Augusta
'''
from ScrapingCoop import ProductosScraper
filecsv = "DataSetCoop.csv";
webs = ProductosScraper();
webs.scraperProd();
webs.grabarDataset(filecsv);
