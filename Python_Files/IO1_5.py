#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot

#Generamos los datos para los graficos
x = numpy.arange(-1, 36, 3.7)
y = numpy.arange(-1, 25, 2.6)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i] = 20 - (2/3)*x[i]

#Señalamos la region solucion
a=[0, 0, 30, 0]
b=[20,0,0,20]

#Creamos el Grafico
pyplot.fill(a,b,'y')
pyplot.plot(x,y2)
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')
pyplot.show()