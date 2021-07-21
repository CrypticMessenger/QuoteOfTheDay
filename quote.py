# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:54:00 2021

@author: NAMAN
"""
import requests
from bs4 import BeautifulSoup
url="https://www.azquotes.com/"
source_code=requests.get(url)
text=source_code.text
bswebpage=BeautifulSoup(text,features='lxml')
quotes=bswebpage.findAll("a",{'class':"title"})
f0=open('quote.txt','w')

f0.write("Today's quote is: \n")
for quote in quotes:
    f0.write(quote.text)
    break

f0.write("\n")

person=bswebpage.findAll("div",{'class':"q_user"})

for p in person:
    f0.write("said by -"+p.text)
    break



f0.close()