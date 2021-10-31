opcion = ''
while opcion != 'N':
    try:
        names = input("ingrese nombres de los jugadores: ")
        arrNames = names.split(" ")
        player1 = arrNames[0]
        player2 = arrNames[1]
        play1 = player1[:3].upper()
        play2 = player2[:3].upper()
    except:
        print("nombre ingresado invalido")
        break
    score1 = 501
    score2 = 501
    if play1 == play2:
        play2 = play2 + "2"
    
    while score1 > 0 or score2 >0:    
        try:
            for i in range(3):
                shoot1 = input("Ingrese un valor: ")
                if shoot1.upper() == "DOUBLE BULL":
                    score1 = score1 - 50
                elif shoot1.upper() == "SINGLE BULL":
                    score1 = score1 - 25
                elif shoot1.upper() == "NULL":
                    score1 = score1
                else:
                    shoot = shoot1.split(" ")
                    multiplicador = int(shoot[0])
                    if multiplicador > 3 or multiplicador < 0:
                        print("Multiplicador fuera de rango, debe ser entre 1 y 3")
                        break
                    number = int(shoot[1])
                    if number >20 or number <0:
                        print("Puntaje fuera de rango")
                        break
                    score1 = score1 - (multiplicador*number)
                if score1 <0:
                    score1 = score1 * - 1
        except:
            print("Error en el ingreso")
            break
        try:
            for j in range(3):
                shoot2 = input("Ingrese un valor: ").upper()
                if shoot2.upper() == "DOUBLE BULL":
                    score2 = score2 - 50
                elif shoot2.upper() == "SINGLE BULL":
                    score2 = score2 - 25
                elif shoot2.upper() == "NULL":
                    score2 = score2
                else:
                    shoot = shoot2.split(" ")
                    multiplicador = int(shoot[0])
                    if multiplicador > 3 or multiplicador < 0:
                        print("Multiplicador fuera de rango, debe ser entre 1 y 3")
                        break
                    number = int(shoot[1])
                    if number >20 or number <0:
                        print("Puntaje fuera de rango")
                        break
                    score2 = score2 - (multiplicador*number)
                if score2 <0:
                    score2 = score2 * - 1
        except:
            print("Error en el ingreso")
            break
        print(play1,score1)
        print(play2,score2)
        if score1 == 0:
            print("Gana ",player1," Felicidades")
            break
        elif score2 == 0:
            print("Gana ",player2," Felicidades")
            break
    opcion = input("Desea jugar de nuevo(Y/N):").upper()