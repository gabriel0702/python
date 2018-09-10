#!/usr/bin/python3

nomes = ['daniel', 'pedro', 'julia']

try:
    a = int(input('Digite um número: '))
    print(nomes[a -1])

except IndexError:
    print('A lista contem apenas {} elementos vc digitou o index {}'.format(len(nomes), num))

except Exception:
    pass