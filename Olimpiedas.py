def heapify(lista, n, i):

    bigger = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] > lista[l]:
        bigger = l

    if r < n and lista[bigger] > lista[r]:
        bigger = r

    if bigger != i:
        lista[i], lista[bigger] = lista[bigger], lista[i]
        heapify(lista, n, bigger)

def heapSort(lista):
    n = len(lista)

    for i in range(n, 0, -1):
        heapify(lista, n, i - 1)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)


Npais, modalidades = [int(x) for x in input().split()]

paises = []
podio = []

for x in range(Npais):
    paises.append([0, 0, 0, -(x+1)])

for i in range(modalidades):
    medalhas = input().split()
    for l in range(len(medalhas)):

        pais = int(medalhas[l]) - 1

        if l == 0:
            paises[pais][0] = int(paises[pais][0])+1
        if l == 1:
            paises[pais][1] = int(paises[pais][1])+1
        if l == 2:
            paises[pais][2] = int(paises[pais][2])+1


heapSort(paises)


for i in range(len(paises)):
    podio.append(str(paises[i][-1] * -1))

print(' '.join(podio))
