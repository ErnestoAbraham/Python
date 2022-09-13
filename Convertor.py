print("***********")
print("conversor")
print("************")

print("menu de opciones")
print("presiona 1 para convertir de numero a palabra.")
print("presiona 2 para convertir de palabra a numero.")

opcion = int(input("Cual es la opcion deseada?"))

if opcion == 1:
    print("\n Conversor de numero a palabra")

    opcion_uno = int(input("Cual es el numero que deseas convertir a palabra"))

    if opcion_uno == 1:
        print("el numero es 'uno'")
    elif opcion_uno == 2:
        print("el numero es 'dos'")
    elif opcion_uno == 3:
        print("el numero es 'tres'")
    elif opcion_uno == 4:
        print("el numero es 'cuatro'")
    elif opcion_uno == 5:
        print("el numero es 'cinco'")
    else:
        print("El numero selecionado no esta registrado")

if opcion == 2:
    print("\n Conversor de palabra a numero")

    opcion_dos = input("Cual es la palabra que deseas convertir a numero?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("El numero es '1")
    elif opcion_dos == "dos":
        print("El numero es '2")
    elif opcion_dos == "tres":
        print("El numero es '3")
    elif opcion_dos == "cuatro":
        print("El numero es '4")
    elif opcion_dos == "cinco":
        print("El numero es '5")
        
else:
    print("opcion no disponible")

print("fin.")