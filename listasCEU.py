"""
PREGUNTA 4

En este ejercicio se os pide crear un fichero llamado listasCEU.py 
que realice las siguientes funcionnes


Define una lista que contenga al menos 4 elementos de todos 
los tipos de valores permitidos en Python.
Selecciona cada dos elementos (uno si otro no) 
desde el final de la lista.
Cambia solamente la posición del primer elemento con el último elemento de la lista.
Elimina el último elemento de la lista modificada en el paso anterior.
Crea una nueva lista con la repetición de los elemento 
de la lista guardada en el paso anterior."""

def CEU():
    VERDADERO=["true", "verdadero", "1", "v", "t"]
    listaCEU=[]
    lista=[]
    lista_final=[]
    for i in range(4):
        print("Enteros")
        listaCEU.append(int(input("Entero #{} ".format(i+1))))
        print("Float")
        listaCEU.append(float(input("Float #{} ".format(i+1))))
        print("String")
        listaCEU.append(input("Palabra #{} ".format(i+1)))
        print("Booleano")
        respuesta=listaCEU.append(input("True or False#{} ".format(i+1)))
        def evaluacion_bool():
            if respuesta in VERDADERO:
                return True
            else:
                return False
        evaluacion_bool()
    for elemento in listaCEU:
        lista.append(listaCEU[::-2])
    lista[-1]=lista[0]
    lista[0]=lista[-1]
    for elemento in lista:
        if elemento in lista and elemento not in lista_final:
            lista_final.append(elemento)
    return lista_final

print(CEU())

 
      