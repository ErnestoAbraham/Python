n = 1
while n <= sizeNotas:
    nota = float(input(f"Ingrese Nota[(n)]:"))
    if bajo <= nota <= alto:
         alumno.append(nota)
         n += 1
    else:
         print(f">Debe ingresar una nota entre[{bajo}]y[{alto}]")
#Mostrar notas
print("\n#Notas Alumno")
print("--- ---")
sumaNotas=0
for k in range(len(alumno)):
    nota = alumno[k]
    if nota > notaAlta:
         notaAlta=nota
    if nota<notaBaja:
         notaBaja = nota
    sumaNotas += nota
    print("Nota [{:d}]=[:0.2f}".format(k+1,nota))
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
media= sumaNotas / sizeNotas
print("\nNota Media: {:0.2f}".Format(media))
print("Nota Alta:(:e.zf)".Format(notaAlta))
print("Nota Baja:(:0.2f)".format(notaBaja))