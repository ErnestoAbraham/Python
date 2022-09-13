import random;
Lista_random = [];
Lista_random.append(random.randint(1, 10));

for n in Lista_random:
    print(Lista_random,n ** 2);
    print( Lista_random, n**3);

l1 = [];
l2 = [];

for i in range(0, 5):
    l1.append(str(input("Ingresa el elemento %d:" % i)));

l2 = l1[::-1];
print("La lista invertida es: ");
for char in l2:
    print(char, end=" ",sep="-");

numero_como_cadena = input("Escribe un número: ")
numero = float(numero_como_cadena)
if numero == 0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")



cantidad = float(input("Ingresa una cantidad: "))


