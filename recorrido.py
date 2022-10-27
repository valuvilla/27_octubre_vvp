"""
Crea un Script llamado recorrido.py que realice las siguientes funciones:

Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]

Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
"""

from ast import main


def recorrer():
    lista=[18, 50, 210, 80, 145, 333, 70, 30]
    nueva_lista=[]
    while True:
        for i in lista:
            if i % 10 == 0 and i<200:
                nueva_lista.append(i)
                return nueva_lista
            if i>300:
                break

print(recorrer())

if __name__=="__main__":
    main()