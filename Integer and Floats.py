mi_numero = 1;
print(mi_numero);

print(type(mi_numero));


edad = input("dime tu edad")
print("tu edad es: " + edad);

num1 = 20;
num2 = 30.5;

num1 = num1+num2;
print(type(num1));
print(type(num2));


edad = input("dime tu edad: ");
edad = int(edad);
nueva_edad = 1+ edad;
print(nueva_edad);


print("suma");

numero_uno = 5;
numero_dos = 4;

resultado = numero_uno + numero_dos;
print("el resultado de la suma es: ");
print(resultado);

print("el resultado de la suma es: " +str(resultado));


mensaje = "hola luis";
buscar_subcadena=mensaje.find("luis");
print(buscar_subcadena);

x = 10;
y = 5;

print("mis numero son "+ str(x)+ " y "+ str(y) );
print("mis numeros son {} y {} ".format(x,y));
print("la suma de {} y {} es igual a {} ".format(x,y, x+y));

color = "rojo";
matricula=4565825;

print(f"el auto es color {color} y su matricula es {matricula}");


print(f"{x} + {y} = {x+y}");
print(f"{x} - {y} = {x-y}");
print(f"{x} * {y} = {x*y}");
print(f"{x} / {y} = {x/y}");
print(f"{x} % {y} = {x%y}");
print(f"{x} ^ {y} = {x**y}");
print(f"{x} ^ {y} = {x**y}");
print(f"La raiz cuadrada de {x} = {x**0.5}");


#cifra sin redondear
print(90/7);
#cifra redondeada
print(round(90/7));

#otro ejemplo
valor = 95.666666666;
#redondeando
print(round(valor,2));

#Creando la variable texto
texto = "Este es el texto de jose luis";
#almacenando texto en la variable resultado
resultaddo = texto;
#imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo upper
resultado = texto.upper();
#imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo upper pero solo el indice 2
resultado = texto[2].upper();
#imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo lower
resultado = texto.lower();
#imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo split
resultado = texto.split();
#imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo split eliminando las t
resultado = texto.split("t");
#imprimiendo la variable
print(resultado);

#usando el metodo join, se tienen las
# variables a, b, c, d y e pero en e
# indicamos que se uniran las palabras
# pero usando un espacio de separacion
a = "Aprender";
b = "Python";
c = "es";
d = "genial";
e = " ".join([a, b, c, d]);
print(e);

#almacenando texto en la variable resultado
# y usando el metodo find()
# (cuando no encuentra lo que buscas regresa -1)
resultado = texto.find("s");
# imprimiendo la variable
print(resultado);

#almacenando texto en la variable resultado y
#usando el metodo replace()
resultado = texto.replace("Jose", "todo");
#imprimiendo la variable
print(resultado);


palabra = input("introduce una palabra");
num_int = int(input("teclea un numero entero"));
num_float = float(input("teclea un numero float"));
num_complejo = complex(input("teclea un numero complejo"));

print("string", palabra);
print("entero", num_int);
print("flotante", num_float);
print("complejo", num_complejo);

#Se utiliza para leer lineas string y (""") para multilineas
poema ="""Mil pequeños peces blancos
como si hirviera en el color del agua"""

print(poema);
print("peces" in poema);
print(len(poema));

#uso de los operadores logicos
print(3&2);
print(3|2);
#XOR, si (1/0) son iguales da 0 y si son diferentes da 1
print(3^2);
#Es lo contrario a Xor
print(3or 2);


