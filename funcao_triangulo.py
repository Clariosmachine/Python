def triangulo(num):
  for x in range(1, num + 1):
    print(str(num) * x)


def triang_cresc(num):
  for x in range(1, num + 1):
    numeros = tuple(range(1, x + 1))
    print(numeros)
    

numero = int(input('Digite um número: '))
triangulo(numero)
print('-='*15)
triang_cresc(numero)
