#Importamos las librerias necesarias
import numpy
from matplotlib import pyplot

#Generamos los datos para los graficos
x = numpy.arange(-3, 5, 0.8)
y = numpy.arange(-1, 6, 0.7)
y1 = numpy.zeros(len(x))
x1 = numpy.zeros(len(x))
y2 = numpy.zeros(len(x))
for i in range(len(x)):
  y2[i] = 0.5*x[i] + 1
  
#Señalamos la region solucion
a=[-3, -3, 4.2, 4.2,-3]
b=[5.3, y2[0], y2[9], 5.3, 5.3]

#Creamos el Grafico
pyplot.fill(a,b,'y')
pyplot.plot(x,y2, linestyle = 'dashed', color='b')
pyplot.plot(x,y1, color='k')
pyplot.plot(x1,y, color='k')
pyplot.show()