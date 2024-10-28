lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
# def soma(lista_a,lista_b):
#     a = list(zip(lista_a,lista_b))
#     re = []
#     i=0
#     for it in a:
#         re.append(lista_a[i] + lista_b[i])
#         i+=1
#     print(re)
# soma(lista_a,lista_b)
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)