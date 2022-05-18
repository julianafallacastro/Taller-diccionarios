n=1
estudiantes = {}

while(n<=10):
    nombre = input("Ingrese nombre: ")
    nota = float(input("Ingrese nota: "))
    print("\n")

    estudiantes[n] = {'nombre':nombre, 'nota':nota}
    n+=1

#Mostrando todos los estudiantes
print("Lista de todos los estudiantes de la clase")
for n,d in estudiantes.items():
    print(f"Nombre: {d['nombre']} Nota = {d['nota']}")


#mostrando los estudiantes suspendidos
print("\nEstudiantes Suspendidos")
for n,d in estudiantes.items():
    if(d['nota']<6.0):
        print(f"Nombre: {d['nombre']} Nota = {d['nota']}")

#mostrando los estudiantes aprobados
print("\nEstudiantes Aprobados")
for n,d in estudiantes.items():
    if(d['nota']>=6.0):
        print(f"Nombre: {d['nombre']} Nota = {d['nota']}")

#Nota promedia de la clase
print("\nNota promedio de la clase")
nota = 0
for n,d in estudiantes.items():
    nota += d['nota'] # es igual a nota = nota + d['nota']
print(nota/len(estudiantes))