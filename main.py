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
            if magnitudVi.count(".")==1:
                if (not(magnitudVi.split(".")[0].isdigit())) or (not(magnitudVi.split(".")[1].isdigit())):
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                    validMag = 0
                if (magnitudVi.split(".")[0].isdigit()) and (magnitudVi.split(".")[1].isdigit()):
                    validMag = 1
        infoVectori.append(float(magnitudVi))

        print("A continuación ingresaremos sus cosenos directores\nNo olvides que solo pueden ir de 0 a 180 grados y que la suma de sus cosenos al caudrado debe ser 1.")
        alpha = 0
        beta = 0
        gamma = 0
        correctAngles=False
        while correctAngles==False:
            validAlpha=0
            while validAlpha==0:
                alpha = input("\033[1;32m"+"Ingrese el ángulo alpha (ángulo con el eje X) separando los enteros de los decimales con un punto (.): "+"\033[0;m")
                if alpha.count(".")!=1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validAlpha=0
                if alpha.count(".")==1:
                    if (not(alpha.split(".")[0].isdigit())) or (not(alpha.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validAlpha = 0
                    if (alpha.split(".")[0].isdigit()) and (alpha.split(".")[1].isdigit()):
                        if (float(alpha)<0) or (float(alpha)>180):
                            print("\033[1;31m"+"**"+"\033[4;30m"+"Lo sentimos, lo que has ingresado no es un ángulo válido, debe estar entre 0 y 180 grados, inténtalo de nuevo."+"\033[0;m")
                            validAlpha=0
                        if (float(alpha)<=180) and (float(alpha)>=0):
                            validAlpha=1
            validBeta = 0
            while validBeta == 0:
                beta = input("\033[1;32m"+"Ingrese el ángulo beta (ángulo con el eje Y) separando los enteros de los decimales con un punto (.):  "+"\033[0;m")
                if beta.count(".")!=1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validBeta=0
                if beta.count(".")==1:
                    if (not(beta.split(".")[0].isdigit())) or (not(beta.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validBeta = 0
                    if (beta.split(".")[0].isdigit()) and (beta.split(".")[1].isdigit()):
                        if (float(beta)<0) or (float(beta)>180):
                            print("\033[1;31m"+"**"+"\033[4;30m"+"Lo sentimos, lo que has ingresado no es un ángulo válido, debe estar entre 0 y 180 grados, inténtalo de nuevo."+"\033[0;m")
                            validBeta=0
                        if (float(beta)<=180) and (float(beta)>=0):
                            validBeta=1
            validGamma = 0
            while validGamma == 0:
                gamma = input("\033[1;32m"+"Ingrese el ángulo gamma (ángulo con el eje Z) separando los enteros de los decimales con un punto (.): "+"\033[0;m")
                if gamma.count(".")!=1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validGamma=0
                if gamma.count(".")==1:
                    if (not(gamma.split(".")[0].isdigit())) or (not(gamma.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validGamma = 0
                    if (gamma.split(".")[0].isdigit()) and (gamma.split(".")[1].isdigit()):
                        if (float(gamma)<0) or (float(gamma)>180):
                            print("\033[1;31m"+"**"+"\033[4;30m"+"Lo sentimos, lo que has ingresado no es un ángulo válido, debe estar entre 0 y 180 grados, inténtalo de nuevo."+"\033[0;m")
                            validGamma=0
                        if (float(gamma)<=180) and (float(gamma)>=0):
                            validGamma=1
