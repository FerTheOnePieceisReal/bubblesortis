# sorter.py
class Sorter:
    def bubble_sort(self, vet):
        # Clonamos la lista para no mutar el original en las pruebas
        arr = vet.copy() 
        n = len(arr)
        
        # Implementación del código de la guía adaptado a Python
        for i in range(n, 1, -1):
            for j in range(0, i - 1):
                if arr[j] > arr[j + 1]:
                    # Intercambio (aux)
                    aux = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = aux
        return arr