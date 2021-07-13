import sys
sys.setrecursionlimit(10000)


def gerar_matriz(a, b):

    global matriz

    for k in range(a):

        line = []
        entrada = input()

        for m in entrada:

            line.append(m)

        matriz.append(line)

    encontraPasto(matriz, a, b)


def encontraPasto(m, l, c):
    global lobos
    global ovelhas
    global g
    global w
    for i in range(l):
        for n in range(c):
            if m[i][n] == '.' or m[i][n] == 'v' or m[i][n] == 'k':
                ovelhas = 0
                lobos = 0
                if m[i][n] == 'v':
                    m[i][n] = '*'
                    lobos += 1
                    encontraAnimais(i, n, m)
                    if lobos > ovelhas or lobos == ovelhas:
                        ovelhas = 0
                        w += lobos
                    elif ovelhas > lobos:
                        lobos = 0
                        g += ovelhas
                elif m[i][n] == 'k':
                    m[i][n] = '*'
                    ovelhas += 1
                    encontraAnimais(i, n, m)
                    if lobos >= ovelhas:
                        ovelhas = 0
                        w += lobos
                    elif ovelhas > lobos:
                        lobos = 0
                        g += ovelhas
                elif m[i][n] == '.':
                    m[i][n] = '*'
                    encontraAnimais(i, n, m)
                    if lobos >= ovelhas:
                        ovelhas = 0
                        w += lobos
                    elif ovelhas > lobos:
                        lobos = 0
                        g += ovelhas
            else:
                pass


def encontraAnimais(linha, coluna, matrix):
    global lin
    global col
    global ovelhas
    global lobos

    if coluna + 1 <= col - 1:

        if matrix[linha][coluna + 1] == 'v':
            lobos += 1
            matrix[linha][coluna + 1] = '*'
            encontraAnimais(linha, coluna + 1, matrix)

        elif matrix[linha][coluna + 1] == 'k':
            ovelhas += 1
            matrix[linha][coluna + 1] = '*'
            encontraAnimais(linha, coluna + 1, matrix)

        elif matrix[linha][coluna + 1] == '.':
            matrix[linha][coluna + 1] = '*'
            encontraAnimais(linha, coluna + 1, matrix)

    if coluna - 1 >= 0:

        if matrix[linha][coluna - 1] == 'v':
            lobos += 1
            matrix[linha][coluna - 1] = '*'
            encontraAnimais(linha, coluna - 1, matrix)

        elif matrix[linha][coluna - 1] == 'k':
            ovelhas += 1
            matrix[linha][coluna - 1] = '*'
            encontraAnimais(linha, coluna - 1, matrix)

        elif matrix[linha][coluna - 1] == '.':
            matrix[linha][coluna - 1] = '*'
            encontraAnimais(linha, coluna - 1, matrix)

    if linha + 1 <= lin - 1:

        if matrix[linha + 1][coluna] == 'v':
            lobos += 1
            matrix[linha + 1][coluna] = '*'
            encontraAnimais(linha + 1, coluna, matrix)

        elif matrix[linha + 1][coluna] == 'k':
            ovelhas += 1
            matrix[linha + 1][coluna] = "*"
            encontraAnimais(linha + 1, coluna, matrix)

        elif matrix[linha + 1][coluna] == '.':
            matrix[linha + 1][coluna] = '*'
            encontraAnimais(linha + 1, coluna, matrix)

    if linha - 1 >= 0:

        if matrix[linha - 1][coluna] == 'v':
            lobos += 1
            matrix[linha - 1][coluna] = '*'
            encontraAnimais(linha - 1, coluna, matrix)

        elif matrix[linha - 1][coluna] == 'k':
            ovelhas += 1
            matrix[linha - 1][coluna] = '*'
            encontraAnimais(linha - 1, coluna, matrix)

        elif matrix[linha - 1][coluna] == '.':
            matrix[linha - 1][coluna] = '*'
            encontraAnimais(linha - 1, coluna, matrix)

    else:
        return


matriz = []
pastos = []
lobos = 0
ovelhas = 0
g = 0
w = 0

lin, col = input().split()
lin, col = int(lin), int(col)
gerar_matriz(lin, col)

print(g, w)
