# -*- coding: utf-8 -*-
import calculadora_indices as calc
peso_number = float(input("Ingrese su peso en kilogramos: "))
altura_number = float(input("Ingrese su altura en metros: "))
edad_number = int(input("Ingrese sus años: "))
genero =(input("Ingrese F si su sexo es femenino, M si es masculino: "))
genero_number = -1.0
while genero_number == -1.0:
    if genero == 'F':
        genero_number = 0.0
        break
    if genero == 'M':
        genero_number = 10.8
        break
    genero =(input("Ingrese F si su sexo es femenino, M si es masculino: "))
    
print("\n")   
Pgrasa = calc.calcular_porcentaje_grasa(peso_number, altura_number, edad_number, genero_number)
print("Usted tiene: " + str(Pgrasa) + " de porcentage de grasa")
