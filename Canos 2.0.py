def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if j == colunas - 1:
                print(f"{matriz[i][j]}")
            else:
                print(f"{matriz[i][j]}", end=" ")


def absoluto(a):
    if a > 0:
        return a
    else:
        return -a


def maximo(a, b):
    return (a + b + absoluto(a - b)) // 2


pedidos, tamanho = input().split()

#  Estas (↓) duas lista são geradas com dois elementos pois no algoritmo (Mochila Booleana) partiremos do index 2.

pesos = [0, 0]
valores = [0, 0]

for i in range(int(pedidos)):
    peso, valor = input().split()
    pesos.append(int(peso))
    valores.append(int(valor))

#  Geram uma matriz com a formatação necessária para o algoritmo. ↓

matrix = [["#"] + [i for i in range(int(tamanho) + 1)]]

for i in range(0, int(pedidos) + 1):
    matrix.append([i] + [0] * (int(tamanho) + 1))

    # Este é o formato em que a matriz é gerada.

    #  # 0 1 2 3 4 5 6 7 8 9 10
    #  0 0 0 0 0 0 0 0 0 0 0 0
    #  1 0 0 0 0 0 0 0 0 0 0 0
    #  2 0 0 0 0 0 0 0 0 0 0 0
    #  ...

# Algortimo de Mochila Booleana. ↓

for i in range(2, int(pedidos) + 2):
    for j in range(2, int(tamanho) + 2):

        # Por conta daquele formato partimos do elemento matriz[2][2].

        matrix[i][j] = matrix[i - 1][j]

        if pesos[i] <= matrix[0][j]:
            matrix[i][j] = maximo(matrix[i - 1][j],
                                  matrix[i][j - pesos[i]] + valores[i])

print(matrix[-1][-1])
