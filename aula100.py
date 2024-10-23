
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

# 1. Aumentando os preços em 10% e gerando novos_produtos
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] *= 1.10

# 2. Ordenando os produtos por nome em ordem decrescente
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda p: p['nome'], reverse=True)

# 3. Ordenando os produtos por preço em ordem crescente
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=lambda p: p['preco'])

# Exibindo os resultados
print("Produtos originais:", produtos)
print("\nNovos produtos com aumento de 10%:", novos_produtos)
print("\nProdutos ordenados por nome (decrescente):", produtos_ordenados_por_nome)
print("\nProdutos ordenados por preço (crescente):", produtos_ordenados_por_preco)
