def suc(a):
    res = a + 1
    return res


def soma(a, b):
    for i in range(b):
        a = suc(a)
    return a


def multiplicacao(a, b):
    c = 0
    for i in range(b):
        c = soma(c, a)
    return c


def exponencial(a, b):
    c = 1
    for i in range(b):
        c = multiplicacao(c, a)
    return c


while True:
    a = input()
    if a:
        entrada = a.split()
        if entrada[0] == 'Suc':
            print(suc(int(entrada[1])))
        elif entrada[0] == 'Soma':
            print(soma(int(entrada[1]), int(entrada[2])))
        elif entrada[0] == 'Multi':
            print(multiplicacao(int(entrada[1]), int(entrada[2])))
        elif entrada[0] == 'Exp':
            print(exponencial(int(entrada[1]), int(entrada[2])))
    else:
        break
