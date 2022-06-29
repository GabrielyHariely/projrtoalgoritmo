import random

def palpite(x):
    random_numero = random.randint(1, x)
    palpite = 0

    while palpite != random_numero:
        palpite = int(input(f'Digite um número entre 1 e {x}: '))

        if palpite < random_numero:
            print('Desculpa, chute outra vez. Foi muito baixo.\n')

        elif palpite > random_numero:
            print('Desculpa, chute outra vez. Foi muito alto.\n')

    else:
        print(f'Parabéns. Você acertou o número secreto {random_numero} corretamente!')

palpite(100)






