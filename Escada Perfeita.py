# Depois de algumas tentativas e erros eu percebi que em casos onde é possivel formar a escada perfeita a soma das
# subtração  dos elementos da lista "desorganizada" pelos elementos correspondentes , no mesmo index, numa lista ja
# organizada é igual à 0.

numero_colunas = int(input())

escada = int(numero_colunas * (numero_colunas - 1) / 2)  # Quantidade de pedras para formar a escada

numero_pedras_total = 0

pedras = []

for x in input().split():
    pedras += [int(x)]
    numero_pedras_total += int(x)

passos = 0

base = int((numero_pedras_total - escada))  # quantidade de pedras da base de pedras

if base % numero_colunas == 0:

    base = int((numero_pedras_total - escada) / numero_colunas)  # quantidade de linhas da base de pedras
    veredito = 0

    if base > 0:

        for i in range(numero_colunas):
            veredito += pedras[i] - (base + i)  # VEREDITO recebe a subtração do elemento na lista PEDRA com o valor que
            # deveria estar nessa posição.

            if pedras[i] > (base + i):
                passos += pedras[i] - (base + i)  # PASSOS recebe esse subtração pois ela resulta no numero de pedras
                # que "movidas"

        if veredito == 0:  # como havia mencionado se soma das subtração  dos elementos da lista "desorganizada"
            #  pelos elementos correspondentes

            print(passos)

        else:
            print("-1")  # Casos em que VEREDITO for diferente de 0, são casos onde há pedras a mais ou a menos.
            # Portanto não é possivel formar uma escada perfeita
    else:
        print('-1')

else:
    print('-1')
