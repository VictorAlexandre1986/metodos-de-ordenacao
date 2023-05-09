import random

class Ordenacao():
    
    def __init__(self):
        lista=[]    
    
    def gerar_lista_embaralhada(self):
        lista = list(range(1,30,1))
        random.shuffle(lista)
        return lista
            
    def __repr__(self):
        return f"<Lista : {self.lista}>"
    
    def InsertionSort(self, lista):

        for i in range(1, len(lista)):
            j = i-1
            proximo_elemento = lista[i]
            while (lista[j] > proximo_elemento) and (j >= 0):
                lista[j+1] = lista[j]
                j = j-1
                lista[j+1] = proximo_elemento
        return lista
    

if __name__ == '__main__':
    obj = Ordenacao()
    lista = obj.gerar_lista_embaralhada()
    print(lista)

    ordenada = obj.InsertionSort(lista)
    print(ordenada)
    