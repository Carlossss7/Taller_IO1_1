#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot
from shapely.geometry import LineString

#Generamos los datos para los graficos
x = numpy.arange(-1, 60, 6.1)
y = numpy.arange(-10, 150, 16)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
y3 = numpy.zeros(len(x))
y4 = numpy.zeros(len(x))
x2 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i]=3000/24 - (60/24)*x[i]
  y3[i]=65-x[i]
  y4[i]=20
  x2[i]=23

#Guardamos las funciones
Linea_1 = LineString(numpy.column_stack((x, y2)))
Linea_2 = LineString(numpy.column_stack((x, y3)))
Eje_x = LineString(numpy.column_stack((x, y4)))
Eje_y = LineString(numpy.column_stack((x2, y)))

#Guardamos las intersecciones
i1 = Linea_2.intersection(Eje_y)
i2 = Linea_2.intersection(Linea_1)

#Graficamos
pyplot.ion()

#Señalamos las funciones
pyplot.plot(x,y2)
pyplot.plot(x,y3)
pyplot.plot(x,y4, color='r')
pyplot.plot(x2,y, color='r')
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')

#Señalamos la region solucion
pyplot.plot([i1.x, i2.x], [i1.y, i2.y], color='k', linewidth=3)

#Señalamos los vertices
pyplot.plot(*i1.xy, 'o', color='k')
pyplot.plot(*i2.xy, 'o', color='k')

#Determinamos el minimo
Vertices_x = [i1.x, i2.x]
Vertices_y = [i1.y, i2.y]

Min=120*Vertices_x[0]+200*Vertices_y[0]
aux=0
if 120*Vertices_x[1]+200*Vertices_y[1]<Min:
  Min=120*Vertices_x[1]+200*Vertices_y[1]
  aux=1

#Imprimimos en la consola el resultado
print ("El valor maximo de p es: ", round(Min), ", X es: ", round(Vertices_x[aux]), "y Y es: ", round(Vertices_y[aux]))