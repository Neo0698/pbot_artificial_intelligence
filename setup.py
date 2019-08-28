# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:35:45 2019

@author: Rapha
"""

import os
os.system("pip install pyaudio")
result=input("did pyaudio install? yes/no")
if(result=="yes"):
        os.system("pip install opencv-contrib-python --upgrade")
if(result=="no"):
    ac=input("install anaconda and type install after installation:")
    os.system("conda install pyaudio")
    ac=input("did it work")
    if(ac=="yes"):
        os.system("pip install opencv-contrib-python --upgrade")

