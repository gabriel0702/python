#!/usr/bin/python3

try:
    notas =int(input("Digite numero de notas: "))

    soma = 0
    for x in range (notas):
        try:
            nota = int(input("Digite n{}:".format(x+1)))
        except Exception as e:
            print('ERRO {}'.format(e))
        soma += nota
    media = soma / notas
    if media >= 7:
        print('Media {}, aluno aprovado'.format(media))
    elif media >= 3:
        print('Media {}, recuperacao'.format(media))
    else:
        print('Media {}, REPROVADO!!'.format(media))



