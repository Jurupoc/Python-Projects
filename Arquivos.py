def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arquivos, B = [int(x) for x in input().split()]
Tamanhos = [int(x) for x in input().split()]

heapsort(Tamanhos)

pastas = arquivos
j = arquivos - 1

for i in range(arquivos):

    while j > 0 and Tamanhos[i] + Tamanhos[j] > B:
        j -= 1

    if j > i:
        Tamanhos[i] = Tamanhos[j] = 0
        pastas -= 1
        j -= 1

print(pastas)