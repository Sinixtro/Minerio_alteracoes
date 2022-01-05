
print('-='*30)
print('-='*30)
print('(1)ferro')
print('(2)ouro')
print('(3)cobre')
print('-='*30)

entrada_1 = input('escolha um dos minerios:')
conv1 = int(entrada_1)

print('-='*30)

entrada_celsius = input('digite uma temperatura em celsius que deseje:')
conv2 = float(entrada_celsius)

def ferro_check (conv1):
    if conv2  >= 1535:
        print(f'A temperatura {entrada_celsius} faz o ferro entrar em ponto de fusão')
    elif conv2 >= 3000:
        print (f'A temperatura {entrada_celsius} faz o ferro entrar em ponto de ebulição')
    else:
        print(f'A temperatura {entrada_celsius} não faz alterações no ferro')

def ouro_check (conv1):
    if conv2 >= 1064:
        print(f'A temperatura {entrada_celsius} faz o ouro entrar em ponto de fusão')
    elif conv2 >= 2700:
        print(f'A temperatura {entrada_celsius} faz o ouro entrar em ponto de fusão')
    else:
        print(f'A temperatura {entrada_celsius} não faz alterações no ouro')

def check_minerios(conv1):
    match conv1:
     case 1:
        ferro_check(conv2)
     case 2:
        ouro_check(conv2)


check_minerios(conv1)





