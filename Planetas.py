class Hash():

    def __init__(self, tam=0):
        self.tab = {}
        self.tamanho_max = tam

    def funcaohash(self, chave):
        v = int(chave)
        return v % self.tamanho_max

    def buscar(self, pos):

        if self.tab.get(pos) is None:
            return -1

        else:
            return self.tab[pos]

    def inserir(self, pos):

        if self.tab.get(pos) is None:
            self.tab[pos] = 1
        else:
            self.tab[pos] += 1


def absoluto(a):
    if a > 0:
        return a
    else:
        return -a


def maximo(a, b):
    return (a + b + absoluto(a - b)) // 2


M, N = [int(x) for x in input().split()]
planos = [[0, 0, 0, 0] for i in range(M)]

Tabela = Hash(10000)
maior = 0

for k in range(M):
    planos[k][0], planos[k][1], planos[k][2], planos[k][3] = [int(x) for x in input().split()]

for f in range(N):
    x, y, z = [int(x) for x in input().split()]
    binario = ''

    for l in range(M):

        if (planos[l][0] * x) + (planos[l][1] * y) + (planos[l][2] * z) > (planos[l][3]):

            binario += '0'

        else:
            binario += '1'

    Tabela.inserir(int(binario, 2))
    maior = maximo(maior, Tabela.buscar(int(binario, 2)))

print(maior)
