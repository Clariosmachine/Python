def fibonacci(ntermos):
    x = 0
    y = 1
    cont = 0
    while cont < ntermos:
        print(x, end=' → ')
        cont += 1
        if cont < ntermos:
            print(y, end=' → ')
            cont += 1
        x += y
        y += x
    print('Fim')


termos = int(
    input(
        'Quantos termos da sequência de Fibonacci você quer que sejam mostrados?\n'
    ))
fibonacci(termos)
