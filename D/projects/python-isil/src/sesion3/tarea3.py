# https://github.com/YFRM/python-isil.git

def principal():

    numero = [1,2,3,4,5,6,7,8,9]
    print(numero)

    for num in numero:
        print(num**2)

    suma = 0
    i = 0
    for elemento in numero:
        suma += elemento**2
    i += 1
    resultado = suma
    print(resultado)

    texto = "hola mi nombre es yvan"
    lista_texto=list(texto)

    contador=0
    for letra in lista_texto:
        if(letra=='y'):
            contador=contador+1

    print(contador)


    
if __name__=='__main__':
    principal()
