#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot

#Generamos los datos para los graficos
x = numpy.arange(-5, 6, 1.1)
y = numpy.arange(-1, 7, 0.8)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i]=5

#Señalamos la region solucion
a=[-5,5,5,-5,-5]
b=[5,5,-1,-1,5]

#Creamos el Grafico
pyplot.fill(a,b,'y')
pyplot.plot(x,y2)
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')
pyplot.show()