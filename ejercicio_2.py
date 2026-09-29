try:

    numero_dia = int(input("Escribe un número del 1 al 7: "))



    match numero_dia:
        case 1:
            print("El día seleccionado es: Lunes")
        case 2:
            print("El día seleccionado es: Martes")
        case 3:
            print("El día seleccionado es: Miércoles")
        case 4:
            print("El día seleccionado es: Jueves")
        case 5:
            print("El día seleccionado es: Viernes")
        case 6:
                print("El día seleccionado es: Sábado")
        case 7:
            print("El día seleccionado es: Domingo")    
        case _:
            print("Error: el número debe estar entre 1 y 7.")
        

except ValueError:
    print("Error: Debes ingresar un número entero.")
        