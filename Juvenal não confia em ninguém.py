def gerar_matriz(a, b):

    global matriz

    for k in range(a):

        line = []
        entrada = input()

        for m in entrada:

            line.append(m)

        matriz.append(line)

    encontraBarco(matriz, a, b)


def encontraBarco(m, l, c):

    global indexBarco
    global tamanho

    for i in range(l):
        for n in range(c):
            if m[i][n] == '#':

                m[i][n] = indexBarco
                organizaBarcos(m, i, n)
                indexBarco += 1
                barcos.append(tamanho)
                tamanho = 1

            elif m[i][n] == '.':
                pass
            else:
                pass


def organizaBarcos(matrix, linha, coluna):

    global tamanho
    global indexBarco

    if coluna + 1 <= len(matrix[0]) - 1 and matrix[linha][coluna + 1] == '#':
        matrix[linha][coluna + 1] = indexBarco
        tamanho += 1
        organizaBarcos(matrix, linha, coluna+1)

    if coluna - 1 >= 0 and matrix[linha][coluna - 1] == '#':
        matrix[linha][coluna - 1] = indexBarco
        tamanho += 1
        organizaBarcos(matrix, linha, coluna-1)

    if linha + 1 <= (len(matrix) - 1) and matrix[linha + 1][coluna] == '#':
        matrix[linha + 1][coluna] = indexBarco
        tamanho += 1
        organizaBarcos(matrix, linha + 1, coluna)

    if linha - 1 >= 0 and matrix[linha - 1][coluna] == '#':
        matrix[linha - 1][coluna] = indexBarco
        tamanho += 1
        organizaBarcos(matrix, linha-1, coluna)

    else:
        return tamanho


def verificaTiro(f, d, m):
    if m[f][d] == '.':
        pass
    else:
        barcos[(m[f][d] - 1)] -= 1


indexBarco = 1
matriz = []
barcos = []
tamanho = 1
tirosCertos = 0

linha, coluna = input().split()
linha, coluna = int(linha), int(coluna)
gerar_matriz(linha, coluna)

tiros = int(input())

for i in range(tiros):
    l, c = input().split()
    l, c = int(l) - 1, int(c) - 1
    verificaTiro(l, c, matriz)

for i in barcos:
    if i == 0:
        tirosCertos += 1
    else:
        pass

print(tirosCertos)