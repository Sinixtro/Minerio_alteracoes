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

if conv1 == 1:
    pass
elif conv2 <= 1543:
    print(f'a temperatura {entrada_celsius}C não faz alterações na forma do ferro')
elif conv2 >= 3000:
    print(f'a temperatura {entrada_celsius}C faz o ferro entrar em ebolição')
elif conv2 >= 1535:
    print(f'a temperatura {entrada_celsius}C faz o ferro entrar em ponto de fusão')
else:
    ''''''



if entrada_1 == 2:
    pass
elif conv2 <= 1063:
    print(f'a temperatura {entrada_celsius}C não faz alterações na forma no ouro')

elif conv2 >= 2700:
    print(f'a temperatura {entrada_celsius}C faz o ouro entrar ebolição')

elif conv2 > 1064:
    print(f'a temperatura {entrada_celsius}C faz o ouro entrar em ponto de fusão')

else:
    ''''''




