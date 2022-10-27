"""
PREGUNTA 1

Realiza los siguientes ejercicios en un fichero 
llamado Ejercicio1.py:
*Convertir la variable "var_1"
 en todas las letras mayúsculas y en minúsculas 
 (var_1 = "Módulo 1 de Python ")

*Consulta el tamaño o la longitud de la 
variable "var_1" y calcula la división de ese numero 
entre "7" redondeado a 4 decimales

*Realiza una función llamada funcion1  que calcule siguiente operación 
para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
*Realiza una función llamada funcion2 para que calcule 
la siguiente operación para que el resultado final sea igual a 
catorce (14)// 12 - 4 * (2 - 2) + 2
*Realiza una función llamda funcion3 para pedir al usuario que 
introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
"""
def parte1():
    var_1 = "Módulo 1 de Python "
    var_1_miniscula=var_1.lower()
    var_1_mayuscula=var_1.upper()
    print("la frase en minuscula sería => {} en mayuscula es => {}".format(var_1_miniscula, var_1_mayuscula))
    longitud=int(len(var_1))
    division=longitud / 7
    return "{:.04f}".format(division) 


def funcion1():
    numero=(0) //12 - (4 * 2) - (2 + 2)
    if numero == 0:
        return "Sin realizar cambios\nResultado=0"
    else:
        print("Se tiene que hacer cambios")
        return "El resultado {} pero es el deseado es {}".format(numero, numero - numero)

print(funcion1())

def funcion2():
    numero=(14)// 12 - 4 * (2 - 2) + 2
    if numero == 14:
        return "Sin realizar cambios\nResultado=0"
    else:
        print("Se tiene que hacer cambios")
        catorce=numero - numero + 14
        return "El resultado {} pero es el deseado es {}".format(numero, catorce)

def funcion3():
    edad=int(input("Introduce tu edad: "))
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

print(funcion3())
    