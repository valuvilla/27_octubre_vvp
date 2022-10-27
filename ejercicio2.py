cadena = "zeréP nauJ,01"
lista=list(cadena)
def Nombre_Apellido(lista):
    for x in range(len(lista)):
        F=cadena[x]
        legible=F[::-1]
        frase=legible.split(sep=",")
        Nota_de_nota=frase[0]
        Nombre_Apellido=frase[1]
    return "{} ha sacado un {}".format(Nombre_Apellido,Nota_de_nota)

print(Nombre_Apellido(lista))
