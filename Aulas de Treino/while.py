# while loop
'''
valor = 100
dia = 1

while valor>20:
    dia += 1
    print(f'No {dia} o produto vai ser vendido por {valor}')
    valor-=5
'''

# mais while

valor = int(input('Digite o valor do produto: '))
while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break
