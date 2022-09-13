print("sistema para clacular el promedio de un alumno");

nombre = input("para comenzar dame tu nombre")

matematicas = float(input(nombre + "cual es tu calificacion?: "))
Quimica = float(input(nombre + "cual es tu calificacion?: "))
Biologia = float(input(nombre + "cual es tu calificacion?: "))

promedio = ((matematicas+Quimica+Biologia)/3);

if promedio >= 6:
    print('felicitaciones '+nombre+' "Aprovaste con un promedio de: "', round(promedio, 2));
else:
    print('Lo sentimos '+ nombre +  "has \'reprobado\' con un promedio de:" ,promedio);

print("fin.")