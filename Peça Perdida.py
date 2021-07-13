N = int(input())

conjunto = input().split()

completa = (N * (N + 1)) / 2
faltando = 0

for i in conjunto:
    faltando += int(i)

print(int(completa - faltando))
