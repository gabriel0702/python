#!/usr/bin/python3

matris = [
    [1, 2, 3],
    [7, 9, 8],
    [5, 4, 6]
]

#cont = 0

a = 0
b = 0
for cont ,x in enumerate(matris):
    a +=x[cont] #calcular diagonal positivo
    b +=x[-(cont+1)] #calcular diagonal negativo
    #cont += 1

print(a + b)