subtotalnotas=0
totalnotas=0
for i in range(0,4,1):
 nota=float(input(f"ingrese la nota de 1.5 a 5.0 \n"))
 subtotalnotas=subtotalnotas+nota
totalnotas=subtotalnotas/4
print(f"el promedio total es",totalnotas,"\n")
if 0.0<= totalnotas <=2.9:
  print(f"reprobaste la asignatura")
elif 3.0 <= totalnotas >= 3.9:
  print(f"pasaste raspando la asignatura")
else:
  print(f"aprobaste con buenos resultados")



 