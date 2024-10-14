# Autor: Jonathan Hernández
# Fecha: 14 octubre 2024
# Descripción: Calculadora Vectorial en Python.
# GitHub: https://github.com/Jona163

#Librerias importadas de python
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Primera parte: Solicitar el número de vectores con el que se va a trabajar.
print("\033[1;34m"+"\n¡Bienvenido al programa de vectores de XFORCE!"+"\033[0;m"+"\n\n¿Con cuántos vectores (n) deseas trabajar?")
numvectors=input("\033[1;32m"+"n= "+"\033[0;m")
while not(numvectors.isdigit()) or not(int(numvectors)>0):
    print("\033[1;31m"+"**"+"\033[4;30m"+ "Lo sentimos, lo que has ingresado no es un número valido, vuelve a intentarlo"+"\033[0;m")
    numvectors= input("\033[1;32m"+"n= "+"\033[0;m")

#Segunda parte: Definir la información que me dará de cada vector y almacenarlo.
vectoresinfo=[]
opValInfo=["a","b","c","1","2"]
for i in range (int(numvectors)):
    infoVectori=[i+1]
    print("\nIngresaremos la información de vector número: ",i+1,"\n¿Qué datos nos proporcionarás?\033[1;34m Opciones de ingreso de datos-MENU 1:\na.- Magnitud y Cosenos Directores.\nb.- Vector Cartesiano.\nc.- Magnitud y Dirección a partir de dos puntos.\n1.-Menu 2-Graficacion 2D\n2.-Menu 2-Graficacion 3D")
    opInfo=input("\033[1;32m"+"La opción de ingreso de datos escogida es: "+"\033[0;m").lower()
    while opInfo not in opValInfo:
        print("\033[1;31m"+"**"+"\033[4;30m"+"Lo sentimos, únicamente puedes escoger entre la opción \"a\",\"b\" o \"c\"."+"\033[0;m")
        opInfo = input("\033[1;32m"+"La opción de ingreso de datos escogida para el vector es: "+"\033[0;m").lower()
    print(" ")
    
 if opInfo=="a":
        print("Usted ha seleccionado la opción \"a.- Magnitud y Cosenos Directores\"")
        infoVectori.append("a")
        #Recordando que una magnitud es positiva y que los ángulos directores indican su dirección.
        print("Ingresaremos la magnitud del vector.")
        magnitudVi=0
        validMag=0
        while validMag==0:
            magnitudVi = input("\033[1;32m"+"Ingrese la magnitud del vector separando los enteros de los decimales con un punto (.): "+"\033[0;m")
            if magnitudVi.count(".")!=1:
                print("Los enteros y los decimales deben estar separados por un punto.")
                validMag=0
