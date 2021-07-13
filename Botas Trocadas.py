class No:
    def __init__(self, valor=None):
        self._valor = valor
        self._prox = None
        self._anter = None

    def mostrar(self):
        return self._valor


class Lista:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def __iter__(self):
        i = self._inicio
        while i is not None:
            yield i._valor
            i = i._prox

    def primeiro(self):
        if self._inicio is None:
            return self._inicio
        else:
            return self._inicio.mostrar()

    def isVazia(self):
        if self._inicio is None:
            return True
        return False

    def inserirNoFim(self, valor=None):
        novono = No(valor)

        if self.isVazia():
            self._inicio = self._fim = novono
        else:
            novono._anter = self._fim
            self._fim._prox = novono
            self._fim = novono

    def buscar(self, x):
        i = self._inicio
        while i is not None:
            if x == i._valor:
                break
            else:
                i = i._prox
        return i

    def removerElemento(self, x):
        no_encontrado = self.buscar(x)
        if no_encontrado is not None:
            if no_encontrado._anter is not None:
                no_encontrado._anter._prox = no_encontrado._prox
            else:
                self._inicio = no_encontrado._prox
            if no_encontrado._prox is not None:
                no_encontrado._prox._anter = no_encontrado._anter
            else:
                self._fim = no_encontrado._anter
        return no_encontrado

    def removerDo_inicio(self):
        novono = self._inicio
        if not self.isVazia():
            if novono._prox is None:
                self._fim = None
            else:
                novono._prox._anter = None
            self._inicio = novono._prox
        return novono


N = int(input())

botas_D, botas_E = Lista(), Lista()

pares_corretos = 0

for i in range(N):

    M, L = input().split()

    if L == 'D':
        botas_D.inserirNoFim(int(M))
    else:
        botas_E.inserirNoFim(int(M))

for i in botas_D:

    if i in botas_E:
        botas_E.removerElemento(i)
        pares_corretos += 1

print(pares_corretos)
