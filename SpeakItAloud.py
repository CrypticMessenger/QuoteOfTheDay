# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:02:58 2021

@author: NAMAN
"""


import pyttsx3
import quote
exec(open('quote.py').read())
fo=open("quote.txt",'r')
engine=pyttsx3.init()
engine.setProperty("rate", 150)
engine.say(fo.read())
fo.close()
engine.runAndWait()