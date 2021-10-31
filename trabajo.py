
def primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, " No es primo")
            return False
    return True

def num_gemelo(a,b):
    var1 = primo(a)
    var2 = primo(b)
    if a > b:
        areducido = a-2
        if areducido == b and var1 == True and var2 == True:
            print(a,' y ',b,' Son primos gemelos')
        else:
            print(a,' y ',b,' No son primos gemelos')
    elif a < b:
        if a == b-2 and var1 and var2:
            print(a,' y ',b,' Son primos gemelos')
        else:
            print(a,' y ',b,' No son primos gemelos')

a =int(input('Ingrese numero 1'))
b =int(input('Ingrese numero 2'))

print(num_gemelo(a,b))