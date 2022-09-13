#creando una lista
mi_lista = ['a', 'b', 'c'];
#sabiendo el tipo de dato de la lista
print(type(mi_lista));
#creando una variable para almacenar la longitud de la lista
resultado = len(mi_lista);
#imprimiendo
print(mi_lista);
print(resultado);

#creando otra lista de diferente tipo de datos
otra_lista =['a', 'palabra', 5, 3.1]
#imprimiendo
print(otra_lista)

#extrayendo una lista
extrayendo = otra_lista[1]
print(extrayendo)

#buscando los indices desde x
extrayendo = otra_lista[1:3]
print(extrayendo)

#creando una nueva lista para concatenar
mi_lista2 = ['d', 'e', 'f']
print(mi_lista+mi_lista2)

#modificando un elemento de mi lista
mi_lista[0] = 'beta';
#guardando en mi lista 3 a mi lista y mi lista2
mi_lista3 = mi_lista+mi_lista2;
print(mi_lista3)

#metodo append()
# sirve para agregar un elemento a mi lista
mi_lista3.append('g');
print(mi_lista3)

#metodo pop
#sirve para eliminar un elemento de la lista
mi_lista3.pop(0)
print(mi_lista3)

#guardando el elemento eliminado
eliminando= mi_lista3.pop(3)
print(eliminando)
print(mi_lista3)

#creando mi lista desordenada
lista = ['g', 'o', 'c', 'm', 'f']
lista.sort()
print(lista)

#usando metodo reverse() invierte el orden
lista.reverse()
print(lista)


#declarando un diccionar
#las claves no se pueden repetir
#pero los valores si
diccionario = {'c1': 'valor1', 'c2': 'valor2'}
#viendo de que tipo es
print(type(diccionario))
print(diccionario)

#mostrando el contenido de c1
resultado = diccionario['c1'];
print(resultado);

#creando otro diccionario
cliente = {'nombre': 'luis', 'apellido': 'Sanchez',
           'peso':72, 'talla':65.4}
#Viendo que tiene la clave apellido
consulta = (cliente['apellido'])
print(consulta)

#creando otro de otro diccionario
diccionario2 = {'c1': 55, 'c2':[1,2,3], 'c3':{'s1':100, 's2':200}}
print(diccionario2['c2'])
print(diccionario2['c2'][1])


#guardando el elemetno eliminado
eliminado = mi_lista3.pop(3)
print(eliminado)

#creando una lista en desorden
lista = ['g', 'o', 'c', 'm' 'f'];
#ordenando la lista con metodo sort()
lista.sort()
print(lista)

#usando el metodo reverse() para invertir el orden
lista.reverse()
print(lista)

#creando un diccionario para poder sacar determinada letra
dic = {'c1': ['a','b','c'],'c2':['d', 'e', 'f']};

#agregar elementos a un diccionario que ya fue creado
dic2 = {1:'a', 2:'b'}
print(dic2)

#creamos otro diccionario con un solo elemento
dic[3] = 'c';
print(dic2)

#sobre escribiendo un valor que ya existe
dic2[2] = 'B';
print(dic2)

#metodo para imprimir todas las claves
print(dic2.keys());

#imprimiendo los valores
print(dic2.values());

#Imprimiendo todo lo que contiene nuestro diccionario
print(dic2.items());



#creando un tuple
mi_tuple = (1,2,3,1);
#imprimiendo para saber que tipo es el tuple
print(type(mi_tuple));
print(mi_tuple)
#imprimiendo al indice 0
print(mi_tuple[0]);
#imprimiendo la longitud
print(len(mi_tuple))
#usando el metodo count para saber cuantas veces aparece el 1
print(mi_tuple.count(1));


#creando un set
mi_set = set([1,2,3,4,5,1,1]);
#imprimiendo el tipo de dato de set
print(type(mi_set));
print(mi_set);

#usando len
print(len(mi_set));

#buscando si un esta valor en la set
print(2 in mi_set)

#otra manera de crear un set y unirlo con el metodo union
s1 = {1,2,3};
s2 = {3,4,5};
s3 = s1.union(s2);
print(s3)

#Agregando un elemento a nuestro set
s3.add(6);
print(s3)

#eliminando un elemento
s3.reomove();


#BOOLEANOS
var1 = True;
var2 = False;

print(type(var1))
print(var1)

numero = bool(5<6);
print(numero);

lista = [1,2,3,4];
control = 5 in lista;
print(control);

#estructura de los condicionales
num_uno = 5;
if num_uno == 5:
    print("el numero es : ", num_uno)
else:
    print("el numero es incorrecto;",num_uno)
print("fin");








