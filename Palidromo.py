def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Dame una frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es un Palindromo")
    else:
        print("No es un palindromo")


if __name__ == "__main__":
    run()