"""
PREGUNTA 6

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)

print( nueva_lista[0] == sum(nueva_lista[1:]) )

True

Recordatorio

La función sum(lista) devuelve una suma de los elementos de una lista.
"""


from ast import main


def modificar():
    lista=[1,4,6,7,8,9,3,4,5,63,5,24]
    nueva_lista=[]
    pares=[]
    for lista in lista:
        if lista not in nueva_lista:
           nueva_lista.append(lista)

    lista_final=sorted(nueva_lista)

    print("La lista ordenada de mayor a menor es {}".format(lista_final)) 

    for i in lista_final:
        if int(i) % 2 == 0:
            pares.append(i)

    pares.insert(0, sum(pares))
    print("la lista modificado solo con los pares es {}".format(pares))

    return pares[0]==sum(pares[1:])

print(modificar())

if __name__=="__main__":
    main()