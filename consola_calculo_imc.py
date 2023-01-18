# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("ingrese los siguientes datos para calcular el indice de masa corporal: ")

peso_number = float(input("Ingrese su peso en kilogramos: "))
altura_number = float(input("Ingrese su altura en metros: "))


    
print("\n")   
IMC = calc.calcular_IMC(peso_number, altura_number)
print("Usted quema: " + str(IMC) + " calorias por semana en reposo")

