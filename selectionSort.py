import random

class Ordenacao():
    
    def gerar_lista_embaralhada(self):
        lista = list(range(1,30,1))
        random.shuffle(lista)
        return lista


    def SelectionSort(self,lista):
        for preencher_slot in range(len(lista) - 1, 0, -1):
            max_index = 0
            for localizacao in range(1, preencher_slot + 1):
                if lista[localizacao] > lista[max_index]:
                    max_index = localizacao
            lista[preencher_slot],lista[max_index] = lista[max_index],lista[preencher_slot]
        return lista

if __name__ == '__main__':
    obj = Ordenacao()
    lista_embaralhada = obj.gerar_lista_embaralhada()
    print(lista_embaralhada)
    
    lista_ordenada = obj.SelectionSort(lista_embaralhada)
    print(lista_ordenada)