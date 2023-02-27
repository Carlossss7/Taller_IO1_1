#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot
from shapely.geometry import LineString

#Generamos los datos para los graficos
x = numpy.arange(-1, 108, 10.9)
y = numpy.arange(-20, 200, 22)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
y3 = numpy.zeros(len(x))
y4 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i] = 180 - 2*x[i]
  y3[i] = 80 - (1/2)*x[i]
  y4[i] = 100 - x[i]
  
#Guardamos las funciones
Linea_1 = LineString(numpy.column_stack((x, y2)))
Linea_2 = LineString(numpy.column_stack((x, y3)))
Linea_3 = LineString(numpy.column_stack((x, y4)))
Eje_x = LineString(numpy.column_stack((x, y1)))
Eje_y = LineString(numpy.column_stack((x1, y)))

#Guardamos las intersecciones
i1 = (0,0)
i2 = Linea_2.intersection(Eje_y)
i3 = Linea_2.intersection(Linea_3)
i4 = Linea_1.intersection(Linea_3)
i5 = Linea_1.intersection(Eje_x)

#Graficamos
pyplot.ion()

#Señalamos la region solucion
a=[0, 0, i5.x, i4.x, i3.x, 0]
b=[i2.y, 0, 0, i4.y, i3.y, i2.y]
pyplot.fill(a,b,'y')

#Señalamos las funciones
pyplot.plot(x,y2)
pyplot.plot(x,y3)
pyplot.plot(x,y4)
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')

#Señalamos los vertices
pyplot.plot(i1, 'o', color='k')
pyplot.plot(*i2.xy, 'o', color='k')
pyplot.plot(*i3.xy, 'o', color='k')
pyplot.plot(*i4.xy, 'o', color='k')
pyplot.plot(*i5.xy, 'o', color='k')

#Determinamos el maximo
Vertices_x = [i1[0], i2.x, i3.x, i4.x, i5.x]
Vertices_y = [i1[1], i2.y, i3.y, i4.y, i5.y]

Max=4*Vertices_x[0]+6*Vertices_y[0]
aux=0;
for i in range(len(Vertices_x)-1):
  if 4*Vertices_x[i+1]+6*Vertices_y[i+1]>Max:
    Max=4*Vertices_x[i+1]+6*Vertices_y[i+1]
    aux=i+1

#Imprimimos en la consola el resultado
print ("El valor maximo de p es: ", round(Max), ", X es: ", round(Vertices_x[aux]), "y Y es: ", round(Vertices_y[aux]))