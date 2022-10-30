from principal import *
from configuracion import *
import random
import math

def liste(palabre):
    lista1=[]
    for i in palabre:
        lista1.append(i)
    return lista1




def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    correctaWord=liste(palabraCorrecta)
    userWord=liste(palabra)
    es=False
    for i in range(0,len(correctaWord)):
        if correctaWord[i]==userWord[i]:
            correctas.append(correctaWord[i])
        elif userWord[i] in correctaWord:
            casi.append(userWord[i])
        else:
            incorrectas.append(userWord[i])
    if palabra==palabraCorrecta:
        es=True
    return es




def nuevaPalabra(lista):
    word=random.choice(lista)
    return word




def lectura(archivo, salida, largo):
    for i in archivo:
        if len(i)==largo:
            salida.append(i)
    return salida










