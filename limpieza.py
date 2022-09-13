
def run():
    numero = int(input("Dame un numero: "))
    if numero % 2 == 0:
        print("Tu numero", numero , "es par")
    elif numero % 2 == 1:
        print("Tu numero", numero, " es impar")

if __name__ == "__main__":
    run()
