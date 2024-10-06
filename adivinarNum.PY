#--------------------------------------------------------------------------------------------------------------
# Modulos importados
#--------------------------------------------------------------------------------------------------------------
import random


#--------------------------------------------------------------------------------------------------------------
#FUNCIONES
#--------------------------------------------------------------------------------------------------------------
def pedirNumero(_mensajeInput, _mensajeError):
    try:
        num = int(input(_mensajeInput))

        if (len(str(num)) < 4 or len(str(num)) > 4) and num != 0000:
            print(_mensajeError)
            num = pedirNumero(_mensajeInput, _mensajeError)
    except ValueError:
        print(_mensajeError)
        num = pedirNumero(_mensajeInput, _mensajeError)
    return num


def juego():
    numAdivinar = random.randint(1000, 9999)
    digitosNumero = [int(digito) for digito in str(numAdivinar)]

    intentos = 0

    while True:
        mensajeInput = "Ingresa un número de 4 dígitos:  "
        mensajeError = "Error, número inválido, vuelva a intentar"
        num = pedirNumero(mensajeInput, mensajeError)
        
        digitos = [int(digito) for digito in str(num)]
        
        numsPosCorrecta = 0
        numsPosIncorrecta = 0
        numsIncorrectos = 0

        if num == 0000:
            print(f"Puede ser muy estresante este juego, no dudes que la proxima lo conseguiras!\nEl numero a adivinar era {numAdivinar}")
            break
        if num == numAdivinar:
            print("¡Adivinaste el número!")
            print(f"¡En tan solo {intentos} intentos!")
            break
        if intentos == 20:
            print("Recuerda que puedes rendirte ingresando como numero a adivinar 0000...")
        
        diccionarioContadorDigitosNumero = {}
        for i in range(len(digitosNumero)):
            if digitosNumero[i] in diccionarioContadorDigitosNumero:
                diccionarioContadorDigitosNumero[digitosNumero[i]] += 1
            else:
                diccionarioContadorDigitosNumero[digitosNumero[i]] = 1

        for i in range(len(digitos)):
            if digitos[i] == digitosNumero[i]:
                numsPosCorrecta += 1
                diccionarioContadorDigitosNumero[digitos[i]] -= 1

        for i in range(len(digitos)):
            if digitos[i] != digitosNumero[i] and digitos[i] in diccionarioContadorDigitosNumero and diccionarioContadorDigitosNumero[digitos[i]] > 0:
                numsPosIncorrecta += 1
                diccionarioContadorDigitosNumero[digitos[i]] -= 1  

        numsIncorrectos = 4 - (numsPosIncorrecta + numsPosCorrecta)

        intentos += 1
        
        print(f"Números en el número en la posición correcta: {numsPosCorrecta}")
        print(f"Números en el número pero no en la posición correcta: {numsPosIncorrecta}")
        print(f"Números incorrectos: {numsIncorrectos}")

def reglas():
    print()
    print("----------------------------------------------------")
    print("REGLAS DEL JUEGO DE ADIVINAR EL NÚMERO")
    print("----------------------------------------------------")
    
    print("· El objetivo del juego es adivinar un número de 4 dígitos generado aleatoriamente.")
    print("· Los dígitos pueden repetirse, y tendrás que descifrar cuáles son y su posición.")
    print("----------------------------------------------------")
    
    print("· CÓMO JUGAR:")
    print("   - En cada turno, ingresarás un número de 4 dígitos.")
    print("   - El juego te dirá cuántos dígitos son correctos y están en la posición correcta.")
    print("   - También te dirá cuántos dígitos son correctos pero están en la posición incorrecta.")
    print("   - Finalmente, te indicará cuántos dígitos no están en el número.")
    print("----------------------------------------------------")
    
    print("· TERMINAR EL JUEGO:")
    print("   - Hay dos maneras de finalizar el juego:")
    print("      - El juego terminará cuando adivines correctamente los 4 dígitos en sus posiciones exactas.")
    print("      - Si te quieres rendir puedes ingresar como numero 0000 para luego mostrarte que número era el que debias adivinar!.")
    print("----------------------------------------------------")
    
    print("¡Buena suerte! Que empiece el juego.")
    print("----------------------------------------------------")


#--------------------------------------------------------------------------------------------------------------
# Bloque de menú
#--------------------------------------------------------------------------------------------------------------
while True:
    while True:
        try:
            print()
            print("-------------------------------------------")
            print("MENÚ DEL SISTEMA")
            print("-------------------------------------------")
            print("[1] Jugar")
            print("[2] Mostrar Reglas")
            print("-------------------------------------------")
            print("[0] Salir")
            print("-------------------------------------------")
            print()
            opcion = input("Seleccione una opción: ")
            if opcion in ["0","1","2"]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0":
        exit()

    elif opcion == "1":  
       juego()
        
    elif opcion == "2":   
        reglas()
    print()
    input("Presione ENTER para volver al menú.")