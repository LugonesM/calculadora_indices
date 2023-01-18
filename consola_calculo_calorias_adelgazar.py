# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("ingrese los siguientes datos para calcular las claorias recomendadas que consumir para adelgazar:")

peso_number = float(input("Ingrese su peso en kilogramos: "))
altura_number = float(input("Ingrese su altura en centimetros: "))
edad_number = int(input("Ingrese sus años: "))
genero =(input("Ingrese F si su sexo es femenino, M si es masculino: "))
genero_number = 0.0
while genero_number == 0.0:
    if genero == 'F':
        genero_number = 5.0
        break
    if genero == 'M':
        genero_number = -161.0
        break
    genero =(input("Ingrese F si su sexo es femenino, M si es masculino: "))
    
print("\n")   

print(calc.consumo_calorias_recomendado_para_adelgazar(peso_number, altura_number, edad_number, genero_number))

