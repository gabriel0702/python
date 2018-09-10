#!/usr/bin/python3

nomes = ['daniel', 'maria', 'joao']

busca = input('Digite o nome: ')

for nome in nomes:
    if nomes == nome.strip().lower():
        print('achei')
        break
else:
    print('Não achei')

    