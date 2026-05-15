
start = True

while start:
    num = int(input("Digite numerador : "))
    den  = int(input("Digite Dvisor : "))
    if den == 2 :
        raise Exception("No esta permitido dividir en 2") 
    try:
        print(f"La division de {num} entre {den} es : {num / den}")

    except ZeroDivisionError:
        print("No puede divisor en 0")

    opcion = input(f"Si desea salir digite X en lo contrario presione cualquier TECLA ")
    if opcion == "X":
        start = False