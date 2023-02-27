#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot
from shapely.geometry import LineString

#Generamos los datos para los graficos
x = numpy.arange(-0.5, 4, 0.45)
y = numpy.arange(-4, 5, 0.9)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
y3 = numpy.zeros(len(x))
y4 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i]=3 - 2*x[i]
  y3[i]=0.5
  y4[i]=x[i]

#Guardamos las funciones
Linea_1 = LineString(numpy.column_stack((x, y2)))
Linea_2 = LineString(numpy.column_stack((x, y3)))
Linea_3 = LineString(numpy.column_stack((x, y4)))
i1 = Linea_1.intersection(Linea_2)
i2 = Linea_1.intersection(Linea_3)

#Guardamos las intersecciones
a=[i2.x, i1.x, 3.55, 3.55 , i2.x]
b=[i2.y, 0.5, 0.5, y4[9], i2.y]

#Creamos el Grafico
pyplot.fill(a,b,'y')
pyplot.plot(x,y2, linestyle = 'dashed')
pyplot.plot(x,y3, linestyle = 'dashed')
pyplot.plot(x,y4)
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')
pyplot.show()