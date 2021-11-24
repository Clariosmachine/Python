"""
desempacotamento de lista
"""
lista = ['joao', 'maria', 'pedro', 1, 2, 3, 4, 5, 6, 100]

n1, n2, n3, *nova_lista = lista
# cada variével está pegando um valor da lista
# a variável 'nova_lista', como tem um * antes, vai pegar todos os valores restantes.
print(n1, n2)
print(n3)
print(nova_lista)
