n1 = int(input("dame el valor1"));
n2 = int(input("dame el valor2"));


def Mayor(n1,n2):
    if n1 > n2:
        return n1;
    else:
        return n2;

resultado = Mayor(n1, n2)
print("el valor mas grande es", resultado)