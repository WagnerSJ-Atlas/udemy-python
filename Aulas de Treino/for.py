# Basico do for com range
'''
numero = 6

for numero in range(1,numero+1):
    print(numero)
'''

# Loop com string
'''
palavra = "Google"

for letra in palavra:
    print(f"A letra '{letra}' está dentro da palavra {palavra}")
'''  

# Loop com if
'''
compra_confirmada = False
dados_compra = "Compra deu certo"

for enviar in range(2):
    if compra_confirmada == True:
        print(dados_compra)
        print("Detalhe enviado")
        break
    else:
        print("Algo deu errado")
        break
'''

# Loops aninhado
    # For Loop nested
        # Outer Loop
            # Inner loop
'''
for numero1 in range(5):
    print(f"Produto {numero1}")
    for numero2 in range(5):
        print(numero2)'
'''

# Separando string
'''
palavra = "Papagaio"

for espaco in palavra:
    print(f'{espaco} ', end='')
'''

# Criando um retangulo
'''
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(f'{simbolo}', end='')
    print()
'''