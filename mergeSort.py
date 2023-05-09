import random


    
def gerar_lista_embaralhada():
    lista = list(range(1,30,1))
    random.shuffle(lista)
    return lista
        
def mergeSort(lista):
    if len(lista) > 1:
 
        mid = len(lista)//2
 
        L = lista[:mid]
 
        R = lista[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista
 

if __name__ == '__main__':
    lista = gerar_lista_embaralhada()
    print(lista)
    ordenada = mergeSort(lista)
    print(ordenada)