#Algoritmos de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                
                #Estas 3 líneas equivalen a la línea de abajo
                '''
                temporal = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temporal
                '''

                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_with_while(arr):
    n = len(arr)
    while n > 1:
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        n -= 1



def ordenamiento_por_insercion(arr):
    n = len(arr)
    for i in range(1, n):
        actual = arr[i]
        j = i
        while j > 0 and arr[j-1] > actual:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = actual


def ordenamiento_por_seleccion(arr):
    n = len(arr)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[minimo]:
                minimo = j
        arr[i], arr[minimo] = arr[minimo], arr[i]

lista = [64, 34, 25, 12, 22, 11, 90]

ordenamiento_por_seleccion(lista)




#Algoritmos de búsqueda
def busqueda_lineal(arr, objetivo):
    for elemento in arr:
        if elemento == objetivo:
            return True
    return False


def busqueda_binaria(arr, objetivo):
    if len(arr) == 0:
        return False
    
    #El signo // divide redondeando a un entero
    mitad = (len(arr) - 1) // 2

    if arr[mitad] == objetivo:
        return True
    elif arr[mitad] < objetivo:
        return busqueda_binaria(arr[mitad+1:], objetivo)
    else:
        return busqueda_binaria(arr[:mitad], objetivo)
    

print(busqueda_binaria(lista, 22))