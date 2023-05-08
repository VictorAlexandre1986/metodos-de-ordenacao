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
    
    def BubbleSort(self,lista):
        tamanho_lista = len(lista)

        swapped = False

        for i in range(tamanho_lista-1):

            for j in range(0, tamanho_lista-i-1):
 
                if lista[j] > lista[j + 1]:
                    swapped = True
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
         
            if not swapped:

                return 
        return lista
    

if __name__ == '__main__':
    obj = Ordenacao()
    lista = obj.gerar_lista_embaralhada()
    print(lista)

    ordenada = obj.BubbleSort(lista)
    print(ordenada)
    