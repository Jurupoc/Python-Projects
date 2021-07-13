def insertionSort(arr):

    for d in range(1, len(arr)):

        key = int(arr[d][2])

        j = d - 1

        while j >= 0 and key > int(arr[j][2]):
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1

        if j >= 0 and key == int(arr[j][2]):

            insertionSort_alfabeto(arr)


def insertionSort_alfabeto(arr):

    for i in range(1, len(arr)):

        key = arr[i][0]

        j = i - 1
        while j >= 0 and key < arr[j][0] and int(arr[i][2]) == int(arr[j][2]):
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1


numero_de_pacientes = int(input())

premium = []
diamante = []
ouro = []
prata = []
bronze = []
resto = []

planos = [premium, diamante, ouro, prata, bronze, resto]

for i in range(numero_de_pacientes):

    lista = (input().split())
    lista = lista[0], lista[1], int(lista[2])

    if lista[1] == 'premium':
        premium.append(lista)

    elif lista[1] == 'diamante':
        diamante.append(lista)

    elif lista[1] == 'ouro':
        ouro.append(lista)

    elif lista[1] == 'prata':
        prata.append(lista)

    elif lista[1] == 'bronze':
        bronze.append(lista)

    elif lista[1] == 'resto':
        resto.append(lista)

for i in planos:
    if len(i) > 1:
        insertionSort(i)

for i in planos:
    for n in i:
        print(n[0])