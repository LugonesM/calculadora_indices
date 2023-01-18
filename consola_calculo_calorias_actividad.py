# -*- coding: utf-8 -*-
import calculadora_indices as calc

print("ingrese los siguientes datos para calcular las claorias que quema por semana al realizar actividad fisica:")

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
    
actividad = (input("Si su actividad fisica semanal es poca ingrese: A. Si es ligera: B. Si es moderada: C. Si es deportista: D. Si es atleta: E :  "))
actividad_number = 0.0
while actividad_number == 0.0 :
    if actividad == 'A':
        actividad_number = 1.2
        break
    if actividad == 'B':
        actividad_number = 1.375
        break
    if actividad == 'C':
        actividad_number = 1.55
        break
    if actividad == 'D':
        actividad_number = 1.725
        break
    if actividad == 'E':
        actividad_number = 1.9       
        break
    actividad = (input("Ingrese una letra valida: "))
                       
print("\n")
TMBActividadFisica = calc.calcular_calorias_en_actividad(peso_number, altura_number, edad_number, genero_number, actividad_number)
print("Usted quema: " + str(TMBActividadFisica) + " calorias por semana")
  