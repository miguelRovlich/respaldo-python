num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def numeroRomano(num):
    if num >0 and num <101:
        roman = ''
        while num > 0:
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
    else:
        return "El numero ingresado es invalido"

num = int(input("Ingrese un numero: "))
print(numeroRomano(num))