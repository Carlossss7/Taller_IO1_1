#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot

#Generamos los datos para los graficos
x = numpy.arange(-2, 4, 0.6)
y = numpy.arange(-3, 11, 1.4)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i]=5 - 2*x[i]
a = [5.3]

#Señalamos la region solucion
a=[-2,-2,3.4, 3.4 ,-2]
b=[9, -3, -3, y2[9], 9]

#Creamos el Grafico
pyplot.fill(a,b, 'y')
pyplot.plot(x,y2, linestyle = 'dashed', color='b')
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')
pyplot.show()