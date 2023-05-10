import random


    
def gerar_lista_embaralhada():
    lista = list(range(1,30,1))
    random.shuffle(lista)
    return lista


def particao(lista, valores_baixos, valores_altos):

    pivo = lista[valores_altos]
 
    i = valores_baixos - 1
 
    for j in range(valores_baixos, valores_altos):
        if  lista[j] <= pivo:
 
            i = i + 1

            (lista[i], lista[j]) = (lista[j], lista[i])
 
    (lista[i + 1], lista[valores_altos]) = (lista[valores_altos], lista[i + 1])
 
    return i + 1
 
 

def quicksort(lista, valores_baixos, valores_altos):
    if valores_baixos < valores_altos:
 
        pi = particao(lista, valores_baixos, valores_altos)
 
        quicksort(lista, valores_baixos, pi - 1)

        quicksort(lista, pi + 1, valores_altos)
        
    return lista
 
 
# Driver code
if __name__ == '__main__':

    lista_desordenada = gerar_lista_embaralhada()
    tamanho = len(lista_desordenada)
    print(lista_desordenada)
 
    # Function call
    lista_ordenada =  quicksort(lista_desordenada, 0, tamanho - 1)
    print(lista_ordenada)