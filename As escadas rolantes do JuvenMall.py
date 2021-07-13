def escada_rolante(c):
    tempo_total = 10
    for i in range(1, len(c) - 1):
        tempo_total += min(10, (c[i + 1] - c[i]))
    print(tempo_total)


entrada = [int(input())]
for l in range(entrada[0]):
    entrada.append(int(input()))

escada_rolante(entrada)
