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
            opAngles=(math.cos(math.radians(float(alpha))))**2+(math.cos(math.radians(float(beta))))**2+(math.cos(math.radians(float(gamma))))**2
            if (opAngles<=1.10)and (opAngles>=0.9):
                correctAngles=True
            else:
                print("\033[1;31m"+"**"+"\033[4;30m"+"La suma de los cosenos directores al cuadrado no se encuentra entre 0.9 y 1.1"+"\033[0;m")
                correctAngles=False

        infoVectori.append(float(alpha))
        infoVectori.append(float(beta))
        infoVectori.append(float(gamma))

        print("\nSe ha registrado la información del vector", i+1,":\nSu magnitud es de: ",infoVectori[2],"\nSus ángulos directores (α,β,γ) son: ",(infoVectori[3],infoVectori[4],infoVectori[5]),"grados.")
        reguladora = input("Presiona \"ENTER\" para continuar con el programa...")

    if opInfo=="b":
        print("Usted ha seleccionado la opción \"b.- Vector Cartesiano\"")
        infoVectori.append("b")

        print("A continuación ingresaremos la componente del vector en cada eje.")

        print("Empezaremos con la componente del vector en el eje X.")
        compFx = 0
        validFx = 0
        while validFx == 0:
            compFx = input("\033[1;32m"+"Ingrese la componente en el eje X, separe los enteros de los decimales con un punto (.): "+"\033[0;m")
            if not(compFx.startswith("-")):
                if compFx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFx = 0
                if compFx.count(".") == 1:
                    if (not (compFx.split(".")[0].isdigit())) or (not (compFx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFx = 0
                    if (compFx.split(".")[0].isdigit()) and (compFx.split(".")[1].isdigit()):
                        validFx = 1
            if compFx.startswith("-"):
                possFx=compFx[1:]
                if possFx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFx = 0
                if possFx.count(".") == 1:
                    if (not (possFx.split(".")[0].isdigit())) or (not (possFx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFx = 0
                    if (possFx.split(".")[0].isdigit()) and (possFx.split(".")[1].isdigit()):
                        validFx = 1
        infoVectori.append(float(compFx))

        print("Ahora continuaremos con la componente del vector en el eje Y.")
        compFy = 0
        validFy = 0
        while validFy == 0:
            compFy = input("\033[1;32m"+"Ingrese la componente en el eje Y, separe los enteros de los decimales con un punto (.): "+"\033[0;m")
            if not(compFy.startswith("-")):
                if compFy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFy = 0
                if compFy.count(".") == 1:
                    if (not (compFy.split(".")[0].isdigit())) or (not (compFy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFy = 0
                    if (compFy.split(".")[0].isdigit()) and (compFy.split(".")[1].isdigit()):
                        validFy = 1
            if compFy.startswith("-"):
                possFy=compFy[1:]
                if possFy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFy = 0
                if possFy.count(".") == 1:
                    if (not (possFy.split(".")[0].isdigit())) or (not (possFy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFy = 0
                    if (possFy.split(".")[0].isdigit()) and (possFy.split(".")[1].isdigit()):
                        validFy= 1
        infoVectori.append(float(compFy))

        print("Finalmente registraremos la componente del vector en el eje Z.")
        compFz = 0
        validFz = 0
        while validFz == 0:
            compFz = input("\033[1;32m"+"Ingrese la componente en el eje Z, separe los enteros de los decimales con un punto (.): "+"\033[0;m")
            if not(compFz.startswith("-")):
                if compFz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFz = 0
                if compFz.count(".") == 1:
                    if (not (compFz.split(".")[0].isdigit())) or (not (compFz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFz = 0
                    if (compFz.split(".")[0].isdigit()) and (compFz.split(".")[1].isdigit()):
                        validFz = 1
            if compFz.startswith("-"):
                possFz=compFz[1:]
                if possFz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFz = 0
                if possFz.count(".") == 1:
                    if (not (possFz.split(".")[0].isdigit())) or (not (possFz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFz = 0
                    if (possFz.split(".")[0].isdigit()) and (possFz.split(".")[1].isdigit()):
                        validFz = 1
        infoVectori.append(float(compFz))

        print("\nSe ha registrado la información del vector", i + 1, ":\nSu componente en x es: ", infoVectori[2],
              "\nSu componente en y es: ", infoVectori[3],"\nSu componente en z es: ", infoVectori[4])
        reguladorb = input("Presiona \"ENTER\" para continuar con el programa...")

    if opInfo=="c":
        print("Usted ha seleccionado la opción \"c.- Magnitud y Dirección a partir de dos puntos.\"")
        infoVectori.append("c")

        print("Ingresaremos la magnitud del vector.")
        magnitudVi = 0
        validMag = 0
        while validMag == 0:
            magnitudVi = input("\033[1;32m"+"Ingrese la magnitud del vector separando los enteros de los decimales con un punto (.): "+"\033[0;m")
            if magnitudVi.count(".") != 1:
                print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                validMag = 0
            if magnitudVi.count(".") == 1:
                if (not (magnitudVi.split(".")[0].isdigit())) or (not (magnitudVi.split(".")[1].isdigit())):
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                    validMag = 0
                if (magnitudVi.split(".")[0].isdigit()) and (magnitudVi.split(".")[1].isdigit()):
                    validMag = 1
        infoVectori.append(float(magnitudVi))

        print("Vamos a ingresar el punto final y el punto inicial para obtener la dirección.")

        print("Ingresaremos las coordenadas del punto inicial (Xi,Yi,Zi).")
        puntoIx=0
        validIx = 0
       while validIx == 0:
            puntoIx = input("\033[1;32m"+"Ingrese la coordenada Xi: "+"\033[0;m")
            if not (puntoIx.startswith("-")):
                if puntoIx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIx = 0
                if puntoIx.count(".") == 1:
                    if (not (puntoIx.split(".")[0].isdigit())) or (not (puntoIx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIx = 0
                    if (puntoIx.split(".")[0].isdigit()) and (puntoIx.split(".")[1].isdigit()):
                        validIx = 1
            if puntoIx.startswith("-"):
                possIx = puntoIx[1:]
                if possIx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIx = 0
                if possIx.count(".") == 1:
                    if (not (possIx.split(".")[0].isdigit())) or (not (possIx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIx = 0
                    if (possIx.split(".")[0].isdigit()) and (possIx.split(".")[1].isdigit()):
                        validIx = 1
        infoVectori.append(float(puntoIx))

        puntoIy = 0
        validIy = 0
        while validIy == 0:
            puntoIy = input("\033[1;32m"+"Ingrese la coordenada Yi: "+"\033[0;m")
            if not (puntoIy.startswith("-")):
                if puntoIy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIy = 0
                if puntoIy.count(".") == 1:
                    if (not (puntoIy.split(".")[0].isdigit())) or (not (puntoIy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIy = 0
                    if (puntoIy.split(".")[0].isdigit()) and (puntoIy.split(".")[1].isdigit()):
                        validIy = 1
            if puntoIy.startswith("-"):
                possIy = puntoIy[1:]
                if possIy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIy = 0
                if possIy.count(".") == 1:
                    if (not (possIy.split(".")[0].isdigit())) or (not (possIy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIy = 0
                    if (possIy.split(".")[0].isdigit()) and (possIy.split(".")[1].isdigit()):
                        validIy = 1
        infoVectori.append(float(puntoIy))

        puntoIz = 0
        validIz = 0
       while validIz == 0:
            puntoIz = input("\033[1;32m"+"Ingrese la coordenada Zi: "+"\033[0;m")
            if not (puntoIz.startswith("-")):
                if puntoIz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIz = 0
                if puntoIz.count(".") == 1:
                    if (not (puntoIz.split(".")[0].isdigit())) or (not (puntoIz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIz = 0
                    if (puntoIz.split(".")[0].isdigit()) and (puntoIz.split(".")[1].isdigit()):
                        validIz = 1
            if puntoIz.startswith("-"):
                possIz = puntoIz[1:]
                if possIz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validIz = 0
                if possIz.count(".") == 1:
                    if (not (possIz.split(".")[0].isdigit())) or (not (possIz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validIz = 0
                    if (possIz.split(".")[0].isdigit()) and (possIz.split(".")[1].isdigit()):
                        validIz = 1
        infoVectori.append(float(puntoIz))

        print("Ingresaremos las coordenadas del punto final (Xf,Yf,Zf).")

        puntoFx = 0
        validFx = 0
        while validFx == 0:
            puntoFx = input("\033[1;32m"+"Ingrese la coordenada Xf: "+"\033[0;m")
            if not (puntoFx.startswith("-")):
                if puntoFx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFx = 0
                if puntoFx.count(".") == 1:
                    if (not (puntoFx.split(".")[0].isdigit())) or (not (puntoFx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFx = 0
                    if (puntoFx.split(".")[0].isdigit()) and (puntoFx.split(".")[1].isdigit()):
                        validFx = 1
            if puntoFx.startswith("-"):
                possFx = puntoFx[1:]
                if possFx.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFx = 0
                if possFx.count(".") == 1:
                    if (not (possFx.split(".")[0].isdigit())) or (not (possFx.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFx = 0
                    if (possFx.split(".")[0].isdigit()) and (possFx.split(".")[1].isdigit()):
                        validFx = 1
        infoVectori.append(float(puntoFx))

        puntoFy = 0
        validFy = 0
        while validFy == 0:
            puntoFy = input("\033[1;32m"+"Ingrese la coordenada Yi: "+"\033[0;m")
            if not (puntoFy.startswith("-")):
                if puntoFy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFy = 0
                if puntoFy.count(".") == 1:
                    if (not (puntoFy.split(".")[0].isdigit())) or (not (puntoFy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFy = 0
                    if (puntoFy.split(".")[0].isdigit()) and (puntoFy.split(".")[1].isdigit()):
                        validFy = 1
            if puntoFy.startswith("-"):
                possFy = puntoFy[1:]
                if possFy.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFy = 0
                if possFy.count(".") == 1:
                    if (not (possFy.split(".")[0].isdigit())) or (not (possFy.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFy = 0
                    if (possFy.split(".")[0].isdigit()) and (possFy.split(".")[1].isdigit()):
                        validFy = 1
        infoVectori.append(float(puntoFy))

        puntoFz = 0
        validFz = 0
        while validFz == 0:
            puntoFz = input("\033[1;32m"+"Ingrese la coordenada Zi: "+"\033[0;m")
            if not (puntoFz.startswith("-")):
                if puntoFz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFz = 0
                if puntoFz.count(".") == 1:
                    if (not (puntoFz.split(".")[0].isdigit())) or (not (puntoFz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFz = 0
                    if (puntoFz.split(".")[0].isdigit()) and (puntoFz.split(".")[1].isdigit()):
                        validFz = 1
            if puntoFz.startswith("-"):
                            possFz = puntoFz[1:]
                if possFz.count(".") != 1:
                    print("\033[1;31m"+"**"+"\033[4;30m"+"Los enteros y los decimales deben estar separados por un punto."+"\033[0;m")
                    validFz = 0
                if possFz.count(".") == 1:
                    if (not (possFz.split(".")[0].isdigit())) or (not (possFz.split(".")[1].isdigit())):
                        print("\033[1;31m"+"**"+"\033[4;30m"+"Los elementos antes y después del punto deben ser números."+"\033[0;m")
                        validFz = 0
                    if (possFz.split(".")[0].isdigit()) and (possFz.split(".")[1].isdigit()):
                        validFz = 1
        infoVectori.append(float(puntoFz))

        print("\nSe ha registrado la información del vector", i + 1, ":\nLa magnitud del vector es: ", infoVectori[2],
              "\nLas coordenadas del punto inicial son: ", (infoVectori[3],infoVectori[4],infoVectori[5]), "\nSu componente en z es: ", (infoVectori[6],infoVectori[7],infoVectori[8]))
        reguladorc = input("Presiona \"ENTER\" para continuar con el programa...")
    vectoresinfo.append(infoVectori)

#Menú y cálculos
print("\033[1;34m"+"\nGracias por ingresar tus datos, ahora vamos a proceder con las opciones de cálculo."+"\033[0;m")
menu="\nEscoge una opción del menú.\n1. Ver el vector resultante.\n2. Ver los ángulos entre los vectores ingresados y el vector resultante.\n3. Vector perpendicular al vector fuerza resultante y un vector de los ingresados.\n4. Proyección de un vector ingresado sobre el vector resultante.\n5. Salir."
optionchose= ""
while optionchose != "5":
    #[1,"a",Magnitud,Alpha,Teta,Gamma]
    #[2,"b",Fx,Fy,Fz]
    #[3,"c",Magnitud,Xi,Yi,Zi,Xf,Yf,Zf]
    print(menu)
    optionchose=input("\033[1;32m"+"Ingrese una opción del menú: "+"\033[0;m")
    componentesx = []
    componentesy = []
    componentesz = []
    magnitudesN = []
    vectoresNxyz = []
    angulosNyR = []

    #Analizaremos la información de cada vector
    for i in vectoresinfo:
        #Recopilación de las componentes si el vector fue ingresado con la opción a
        if i[1]=="a":
            componentesx.append(i[2]*(math.cos(math.radians(i[3]))))
            componentesy.append(i[2]*(math.cos(math.radians(i[4]))))
            componentesz.append(i[2]*(math.cos(math.radians(i[5]))))
        # Recopilación de las componentes si el vector fue ingresado con la opción b
        if i[1]=="b":
            componentesx.append(i[2])
            componentesy.append(i[3])
            componentesz.append(i[4])
        # Recopilación de las componentes si el vector fue ingresado con la opción c
        if i[1]=="c":
            mgUnitario=((i[6] - i[3])**2+(i[7] - i[4])**2+(i[8] - i[5])**2)**0.5
            unitarioX = (i[6] - i[3])/mgUnitario
            unitarioY = (i[7] - i[4])/mgUnitario
            unitarioZ = (i[8] - i[5])/mgUnitario
            componentesx.append(i[2]*unitarioX)
            componentesy.append(i[2]*unitarioY)
            componentesz.append(i[2]*unitarioZ)
    # Magnitudes de los n vectores
    for i in vectoresinfo:
        #Recopilación de la magnitud si el vector fue ingresado con la opción a
        if i[1]=="a":
            magnitudesN.append(i[2])
        # Recopilación de la magnitud si el vector fue ingresado con la opción b
        if i[1]=="b":
            magnitudesN.append(((i[2])**2+(i[3])**2+(i[4])**2)**0.5)
        # Recopilación de la magnitud si el vector fue ingresado con la opción c
        if i[1]=="c":
            magnitudesN.append(i[2])
    # El vector resultante como vector cartesiano es.
    resultX = sum(componentesx)
    resultY = sum(componentesy)
    resultZ = sum(componentesz)
    # Hallar la magnitud y cosenos directores.
    resultMag = ((resultX) ** 2 + (resultY) ** 2 + (resultZ) ** 2) ** 0.5
    resultAlpha = math.degrees(math.acos(resultX / resultMag))
    resultBeta = math.degrees(math.acos(resultY / resultMag))
    resultGamma = math.degrees(math.acos(resultZ / resultMag))
    # Hallar el ángulo entre el vector n y el vector resultante.
    for i in range(len(vectoresinfo)):
        niVect=np.array([componentesx[i],componentesy[i],componentesz[i]])
        resVect=np.array([resultX,resultY,resultZ])
        prodDotNyR=np.dot(niVect,resVect)
        angleNyR= math.degrees(math.acos((prodDotNyR)/(resultMag*magnitudesN[i])))
        angulosNyR.append(angleNyR)

    if optionchose == "1":
        print("\nHa seleccionado la opción 1. Ver el vector resultante.")
        print("A continuación te mostraremos la información del vector resultante.\nLa magnitud del vector resultante es: ",
            round(resultMag, 3), "\nSu ángulo director α es: ", (round(resultAlpha, 3)), "\nSu ángulo director β es: ",
            (round(resultBeta, 3)), "\nSu ángulo director γ es: ", (round(resultGamma, 3)),
            "\nSu componente en el eje x es: ", (round(resultX, 3)), "\nSu componente en el eje y es: ",
            (round(resultY, 3)), "\nSu componente en el eje z es: ", (round(resultZ, 3)),
            "\n¡Acompáñanos a ver la gráfica!")

        # Limpiar la información previa.
        plt.clf()
        # Creamos de nuevo un lienzo en blanco.
        fig = plt.figure("N Vectores y Vector Resultante")
        # Agregar un tercer eje para la tercera coordenada
        ax = Axes3D(fig)

        #Graficar n vectores
        for i in range (len(componentesx)):
            xn=np.array([0,componentesx[i]])
            yn=np.array([0,componentesy[i]])
            zn=np.array([0,componentesz[i]])
            ax.text(componentesx[i], componentesy[i], componentesz[i], "V" + str(i + 1), zorder=1, color="y")
            ax.plot(xn, yn, zn, marker='>', color='y')
        #Graficar Vector resultante
        xr = np.array([0, resultX])
        yr = np.array([0, resultY])
        zr = np.array([0, resultZ])
        ax.plot(xr, yr, zr, marker='>', color='g')
        #Graficar punto de origen
        ax.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]), marker='o', color='y')
        #Graficar la información
            # Rotulación de ejes y leyendas
        ax.set_xlabel("$X$", color='darkviolet')
        ax.set_ylabel("$Y$", color='darkviolet')
        ax.set_zlabel("$Z$", color='darkviolet')
        ax.set_title("$Vector  Resultante$", color='g')
        ax.text2D(0.02, 0.02, "|Fr|: "+ str(round(resultMag,3))+"\nα: "+str(round(resultAlpha, 3))+"\nβ: "+
            str(round(resultBeta, 3))+"\nγ: "+str(round(resultGamma, 3))+"\nFrx: "+ str(round(resultX, 3))+"\nFry: "+str(round(resultY, 3))+"\nFrz: "+str(round(resultZ, 3)), transform=ax.transAxes)
         # Configuración inicial de vista
        ax.view_init(20, 75)
        #Mostrar la gráfica
        plt.show()
  elif optionchose == "2":
        print("\nHa seleccionado la opción 2. Ver los ángulos entre los vectores ingresados y el vector resultante.")
        for i in range (len(vectoresinfo)):
            print("El ángulo entre el vector resultante y el vector ",(i+1),"es: ",round(angulosNyR[i],3),"grados.")
        regulador2=input("Presiona \"ENTER\" para continuar con otra opción del menú...")

    elif optionchose == "3":
        print("\nHa seleccionado la opción 3. Vector perpendicular al vector fuerza resultante y un vector de los ingresados.")
        print("Para esta opción debe seleccionar uno de los ", numvectors, "vectores ingresados.")
        eleccion3 = input("\033[1;32m" + "Ingrese el vector elegido: " + "\033[0;m")
        while (not(eleccion3.isdigit())) or (int(eleccion3) > int(numvectors)) or (int(eleccion3) <= 0):
            print("\033[1;31m" + "**" + "\033[4;30m" + "Lo ingresado no está entre las opciones posibles, recuerda que debes ingresar el número del vector con el que deseas trabajar." + "\033[0;m")
            eleccion3 = input("\033[1;32m" + "Ingrese el vector elegido: " + "\033[0;m")
        indice1 = int(eleccion3) - 1
        vtor_eleccion = np.array([componentesx[indice1], componentesy[indice1], componentesz[indice1]])
        vtor_resultante = np.array([resultX, resultY, resultZ])
        perpV = np.cross(vtor_resultante, vtor_eleccion)
        perpMag= (np.dot(perpV,perpV))**0.5
        print("La magnitud de un vector perpendicular al vector resultante y al vector seleccionado es: ", round(perpMag,3))
        print("Las componentes (x,y,z) de un vector perpendicular al vector resultante y al vector seleccionado son: ", (round(perpV[0],3),round(perpV[1],3),round(perpV[2],3)))

        # Limpiar la información previa.
        plt.clf()
        # Creamos de nuevo un lienzo en blanco.
        fig = plt.figure("Vector perpendicular al vector resultante y al vector seleccionado")
        # Agregar un tercer eje para la tercera coordenada
        ax = Axes3D(fig)
        # Graficar el vector n seleccionado.
        xn = np.array([0, componentesx[indice1]])
        yn = np.array([0, componentesy[indice1]])
        zn = np.array([0, componentesz[indice1]])
        ax.plot(xn, yn, zn, marker='>', color='y')
        # Graficar Vector resultante
        xr = np.array([0, resultX])
        yr = np.array([0, resultY])
        zr = np.array([0, resultZ])
        ax.plot(xr, yr, zr, marker='>', color='g')
        # Graficar el Vector Perpendicular
        xp = np.array([0, perpV[0]])
        yp = np.array([0, perpV[1]])
        zp = np.array([0, perpV[2]])
        ax.plot(xp, yp, zp, marker='>', color='b')
        # Graficar punto de origen
        ax.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]), marker='o', color='y')
        # Graficar la información
        # Rotulación de ejes y leyendas
        ax.set_xlabel("$X$", color='darkviolet')
        ax.set_ylabel("$Y$", color='darkviolet')
        ax.set_zlabel("$Z$", color='darkviolet')
        ax.set_title("$Vector  Perpendicular a Vr y Vn$", color='b')
        ax.text2D(0.02, 0.02, "│Vp┴│: "+ str(round(perpMag, 3))+"\nVp┴x: " + str(round(perpV[0],3)) + "\nVp┴y: "+ str(round(perpV[1],3))+"\nVp┴z: "+ str(round(perpV[2],3)),transform=ax.transAxes)
        ax.text2D(0.80, 0.02, "│Fr│: " + str(round(resultMag, 3)), transform=ax.transAxes, color="g")
        ax.text2D(0.80, 0.06, "│V" + str(eleccion3) + "│: " + str(round(magnitudesN[indice1], 3)),transform=ax.transAxes, color="y")

        # Configuración inicial de vista
        ax.view_init(20, 75)
        # Mostrar la gráfica
        plt.show()

    elif optionchose == "4":
        print("Ha seleccionado la opción 4. Proyección de un vector ingresado sobre el vector resultante.")
        print("Para esta opción debe seleccionar uno de los ", numvectors, "vectores ingresados.")
        eleccion4 = input("\033[1;32m" + "Ingrese el vector elegido: " + "\033[0;m")
        while (not (eleccion4.isdigit())) or (int(eleccion4) > int(numvectors)) or (int(eleccion4) <= 0):
            print(
                "\033[1;31m" + "**" + "\033[4;30m" + "Lo ingresado no está entre las opciones posibles, recuerda que debes ingresar el número del vector con el que deseas trabajar." + "\033[0;m")
            eleccion4 = input("\033[1;32m" + "Ingrese el vector elegido: " + "\033[0;m")
        indice2 = int(eleccion4) - 1
        # Conseguir el vector unitario de la resultante
        compo_unitariorx = resultX / resultMag
        compo_unitariory = resultY / resultMag
        compo_unitariorz = resultZ / resultMag
        # Proyeción del n vector sobre el vector unitario.
        proyecx = compo_unitariorx * componentesx[indice2]
        proyecy = compo_unitariory * componentesy[indice2]
        proyecz = compo_unitariorz * componentesz[indice2]
        magnitudproyec = round(proyecx + proyecy + proyecz, 3)
        vtorproyecx = round(magnitudproyec * compo_unitariorx, 3)
        vtorproyecy = round(magnitudproyec * compo_unitariory, 3)
        vtorproyecz = round(magnitudproyec * compo_unitariorz, 3)
        proyec_vector = (vtorproyecx, vtorproyecy, vtorproyecz)
        print("La proyección del vector", eleccion4, "cuyas componentes son: ",
              (round(componentesx[indice2], 3), round(componentesy[indice2], 3), round(componentesz[indice2], 3)),
              " sobre el vector resultante en coordenadas cartesianas es", proyec_vector)
        print("La magnitud de la proyección del vector",
              (componentesx[indice2], componentesy[indice2], componentesz[indice2]), "sobre el vector resultante es",
              magnitudproyec)

        # Limpiar la información previa.
        plt.clf()
        # Creamos de nuevo un lienzo en blanco.
        fig = plt.figure("Proyección del vector seleccionado sobre el vector resultante")
        # Agregar un tercer eje para la tercera coordenada
        ax = Axes3D(fig)
        # Graficar el vector n seleccionado.
        xn = np.array([0, componentesx[indice2]])
        yn = np.array([0, componentesy[indice2]])
        zn = np.array([0, componentesz[indice2]])
        ax.plot(xn, yn, zn, marker='>', color='y')
        # Graficar Vector resultante
        xr = np.array([0, resultX])
        yr = np.array([0, resultY])
        zr = np.array([0, resultZ])
        ax.plot(xr, yr, zr, marker='>', color='g')
        # Graficar el Vector Proyectado
        xp = np.array([0, vtorproyecx])
        yp = np.array([0, vtorproyecy])
        zp = np.array([0, vtorproyecz])
        ax.plot(xp, yp, zp, marker='>', color='b')
        # Graficar punto de origen
        ax.plot(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]), marker='o', color='y')
        # Graficar la información
        # Rotulación de ejes y leyendas
        ax.set_xlabel("$X$", color='darkviolet')
        ax.set_ylabel("$Y$", color='darkviolet')
        ax.set_zlabel("$Z$", color='darkviolet')
        ax.set_title("$Vector Proyección Fn sobre Fr$", color='b')
        ax.text2D(0.02, 0.02,"│Vproy│: " + str(magnitudproyec) + "\nVproy-x: " + str(vtorproyecx) + "\nVproy-y: " + str(vtorproyecy) + "\nVproy-z: " + str(vtorproyecz), transform=ax.transAxes)
        ax.text2D(0.80, 0.02, "│Fr│: " + str(round(resultMag, 3)), transform=ax.transAxes, color="g")
        ax.text2D(0.80, 0.06, "│V"+str(eleccion4)+"│: " + str(round(magnitudesN[indice2], 3)), transform=ax.transAxes, color="y")
        # Configuración inicial de vista
        ax.view_init(20, 75)
        # Mostrar la gráfica
        plt.show()

    elif optionchose!="1" and optionchose!="2" and optionchose!="3" and optionchose!="4" and optionchose!="5":
        print("\033[1;31m"+"**"+"\033[4;30m"+"No existe esa opción en el menu."+"\033[0;m")

print("\033[1;34m"+"¡Gracias por usar nuestro programa, espero sea de gran ayuda para ustedes!"+"\033[0;m")
