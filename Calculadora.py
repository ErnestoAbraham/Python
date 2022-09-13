def divide (num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR 0")
        return "operacion herronea"

try:
    num1 = (int(input("Introduce el primer numero")))

    num2 = (int(input("Introduce el primer numero2")))

    op = input("introduce la operacion a realizar")


    if op == "divide":
        print(divide(num1, num2))

    else:
        print("operacion no contemplada")
        print("operacion ejecutada")

except ValueError:
    print("no se permiten caracteres")