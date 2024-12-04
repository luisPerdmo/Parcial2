import random

def juego():
    while True:
        try:
            maxNumero = int(input("Introduce el número máximo del rango:"))
            if maxNumero <= 1:
                raise ValueError("El rango debe ser mayor que 1.")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}")
         
    intentosMax = max(maxNumero // 20, 1)
    print(f"Tendrás un máximo de {intentosMax} intentos.")
      
    # numero aleatorio a adivinar
    numeroAdivinar = random.randint(1, maxNumero)

    intentos = 0
    while intentos < intentosMax:
        while True:
            try:
                adivinar = int(input(f"Adivina un número entre 1 y {maxNumero}: "))
                if 1 <= adivinar <= maxNumero:
                    break
                else:
                    print(f"Por favor, introduce un número entre 1 y {maxNumero}.")
            except ValueError as e:
                print("¡Error! Debes introducir un número entero.")
        
        intentos += 1

        if adivinar < numeroAdivinar:
            print("El número a adivinar es mayor.")
        elif adivinar > numeroAdivinar:
            print("El número a adivinar es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numeroAdivinar} en {intentos} intentos.")
            break
        print(f"Intentos restantes: {intentosMax - intentos}")
        
    if intentos == intentosMax and adivinar != numeroAdivinar:
        print(f"Has agotado todos los intentos. El número correcto era {numeroAdivinar}.")

juego()