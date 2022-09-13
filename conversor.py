

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuantos " + tipo_pesos + " tienes?: "));
    dolares = pesos / valor_dolar;
    dolares = round(dolares, 2)
    dolares = str(dolares);
    print("Tienes $" + dolares + " Dolares")


menu = """
Bienvenido al conversor de monedas 💋

1 - Pesos Mexicanos
2 - Dolares
3 - Pesos Colombianos

Elige una opcion: 
"""
opcion = int(input(menu))

if opcion == 1:

    conversor("Pesos Mexicanos", 20)
elif opcion == 2:
    conversor("Dolares", 1)
elif opcion == 3:
    conversor("Pesos_Colombianos", 3875)
else:
    print("Ingresa una opcion valida");

