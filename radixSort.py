import random

    
def gerar_lista_embaralhada():
    lista = list(range(1,30,1))
    random.shuffle(lista)
    return lista
 
def countingSort(lista, exp):
 
    tamanho = len(lista)
 

    output = [0] * (tamanho)
 

    count = [0] * (10)
 

    for i in range(0, tamanho):
        indice = lista[i] // exp
        count[indice % 10] += 1
 

    for i in range(1, 10):
        count[i] += count[i - 1]
 

    i = tamanho - 1
    while i >= 0:
        indice = lista[i] // exp
        output[count[indice % 10] - 1] = lista[i]
        count[indice % 10] -= 1
        i -= 1
 

    i = 0
    for i in range(0, len(lista)):
        lista[i] = output[i]
 

def radixSort(lista):
 

    maior = max(lista)
 

    exp = 1
    while maior / exp >= 1:
        countingSort(lista, exp)
        exp *= 10
        
    return lista
 



if __name__ == '__main__':

    lista_desordenada = gerar_lista_embaralhada()
    print(lista_desordenada)
 

    lista_ordenada =  radixSort(lista_desordenada)
    print(lista_ordenada)