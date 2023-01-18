# -*- coding: utf-8 -*-
def calcular_IMC(peso: float, altura: float)->float:
    """Calcula el índice de masa corporal de una persona a partir de la ecuación definida anteriormente
    
    retorno: Índice de masa corporal de la persona """
    imc = peso/(altura**2) #Peso de la persona en kilogramos y Altura de la persona en metros
    return  imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)->float:
    """Calcula el porcentaje de grasa de una persona a partir de la ecuación definida anteriormente
    
    retorno: El porcentaje de grasa que tiene el cuerpo de la persona"""
    
    GC = 1.2 * (peso/(altura**2)) + 0.23 * edad - 5.4 - valor_genero
    return  GC 


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: float)->float:
    """Calcula la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal), a partir de la ecuación definida anteriormente
    
    retorno: La cantidad de calorías que la persona quema en reposo"""

    TMB = 10 * peso + 6.25 * altura - 5 * edad + valor_genero
    return  TMB


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)->float:
    """Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física),
    a partir de la ecuación definida anteriormente
    
    retorno: La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente"""

    TMBenActividadFisica = (10 * peso + 6.25 * altura - 5 * edad + valor_genero)*valor_actividad
    return  TMBenActividadFisica 


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float)->str:
    """Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar,
    a partir de la ecuación definida anteriormente
    
    retorno: Una cadena indicando el rango de calorías que una persona debe consumir si desea adelgazar. """

    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    result80 = str(TMB*0.80)
    result85 = str(TMB*0.85)
    return  "Para adelgazar es recomendado que consumas entre: " + result80 + " y " + result85 + " calorías al día."









