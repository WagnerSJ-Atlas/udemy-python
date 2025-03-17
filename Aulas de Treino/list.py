# lista normal
'''
frutas = ['maça', 'abacaxi']

print(list(frutas))
'''

# Input em lista
'''
frutas_usuario = input("Digite as frutas separadas por virgula: ")

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)
'''

# Tupla (a diferença de tupla é lista é q a tupla é imutavel)
# Tupla gasta menos memoria! 
'''
cores_list = ['amarelo', 'verde', 'azul']
cores_tupla = ('amarelo', 'verde', 'azul')
'''
# Existe os SETS tbm que EVITA itens duplicados
# Sets não utilizam index
'''
list1 = [10, 20, 30, 50, 60]
list2 = [10, 20, 30, 40, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)
'''

# list comprehension
    # Para criar uma nova lista a partir de uma existente
    # expressao for iten in itens

frutas1 = ['maça', 'abacaxi', 'limao', 'morango', 'abacate']

# frutas2 = []

# for iten in frutas1:
#     if 'b' in iten:
#         frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)

# Expressões generator (MUITO MELHOR PARA DESEMEPNHO)

'Para fazer um generator é só mudar o [] de uma lista para ().'