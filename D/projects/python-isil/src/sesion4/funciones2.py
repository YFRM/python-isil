def suma_mejorada(*args, **kwargs):
    return sum(args)
    
def multiplica(*args):
    resultado = 1
    for num in args:
        resultado = restultado * num
        # resultado *= num
    return resultado

def multiplica_5():
    secuencia = list(range(0, num + 1, 5))[1:]
    return multiplica(*secuencia)
    
def principal():
    print(suma_mejorada(5, 5, 10)) #20
    print(multiplica(5, 5, 10))    #30
    print(multiplica5(100))        #5


if __name__ == '__main__':
    principal()