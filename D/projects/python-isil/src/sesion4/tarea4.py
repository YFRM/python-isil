#https://github.com/YFRM/python-isil

def principal():

    num1= int(993)
    num2= int(913)

    res= num1*num2
    a = res / 100
    b = (res % 100) / 10
    c = (res % 100) % 10

    print ('El primer numero es: ',num1)
    print ('El segundo numero es: ',num2)
    print ('El numero capicua es: ',res)

if __name__=="__main__":
    principal()