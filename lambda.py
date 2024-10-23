pessoas = [
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Ana', 'idade': 22},
    {'nome': 'Maria', 'idade': 25},
]
#Ordenado por idade crescente
pessoas_idade = sorted(pessoas, key = lambda p:p['idade'])
#Ordenando por nome decrescente
pessoas_nome = sorted(pessoas, key = lambda n:n['nome'], reverse=True)
print(pessoas_nome)

#Use map() com uma função lambda para converter a lista [2, 4, 6, 8, 10] em uma lista que contém o dobro de cada número.
lista = [2, 4, 6, 8, 10]

lista_dobro = list(map(lambda x:x*2, lista))
print(lista_dobro)

#Use filter() com uma função lambda para filtrar apenas os nomes que começam com a letra "A" na lista:
nomes = ['Ana', 'Carlos', 'Amanda', 'Beatriz', 'Antonio']

nomes_a = list(filter(lambda n:n.startswith('A'), nomes))
print(nomes_a)

#Combine map() e filter() para pegar uma lista de números e retornar o quadrado de todos os números pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrando os números pares e calculando o quadrado deles
quadrados_pares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
# Exibindo o resultado
print(quadrados_pares)
