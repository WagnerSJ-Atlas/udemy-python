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

cores_list = ['amarelo', 'verde', 'azul']
cores_tupla = ('amarelo', 'verde', 'azul')

# Existe os SETS tbm que EVITA itens duplicados
# Sets não utilizam index

list1 = [10, 20, 30, 50, 60]
list2 = [10, 20, 30, 40, 70]

num1 = set(list1)
num2 = set(list2)

print(num1)