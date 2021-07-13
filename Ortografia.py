def absoluto(a):
    if a > 0:
        return a
    else:
        return -a


def minimo(a, b, c):
    d = (a + b - absoluto(a - b)) // 2
    return (c + d - absoluto(c - d)) // 2


def comparacao(a, b):  # a == Palavra errada, b == Palavra do Dicionario
    global saida  # String que salva as palavras do dicionário

    #  Gera as primeiras 2 linhas da matriz ↓

    matrix = [['#', '#'] + [i for i in a], ['#'] + [i for i in range(len(a) + 1)]]

    # Este código gera a matriz com a formatação de tabela

    for i in range(len(b)):
        matrix.append([b[i]] + [i + 1] + [0] * len(a))

    # Algoritmo de Distância de Edição

    for i in range(2, len(b) + 2):
        for j in range(2, len(a) + 2):
            if matrix[i][0] == matrix[0][j]:
                c = 0
            else:
                c = 1
            matrix[i][j] = minimo(matrix[i - 1][j - 1] + c,
                                  matrix[i - 1][j] + 1,
                                  matrix[i][j - 1] + 1)

    # Verifica se a quantidade de edições é menor que 3

    if matrix[-1][-1] < 3:
        saida += b + ' '


n, m = [int(i) for i in input().split()]

dicionario = [input() for i in range(n)]

palavras = [input() for i in range(m)]

saida = ''

for i in palavras:

    for x in dicionario:  # Compara uma palavras por vez com as do DICIONÁRIO

        comparacao(i, x)

    print(saida)

    saida = ''
