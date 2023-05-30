#import libraries
import numpy as np
import matplotlib.pyplot as plt

#function that need to be plotted
def function_one(x):
  return 3*x**2
def function_two(x):
  return 4*x-3

#creates value between -5 and 16 for the "x" which will be use to calculate the value of "y"
x_coordinates=np.arange(-5,16)

#calculating values for y using x coordinate in function_one and function_two
y_coordinate1=function_one(x_coordinates)
y_coordinate2=function_two(x_coordinates)

#plooting the coordinates and labeling them
plt.plot(x_coordinates,y_coordinate1,'o',label='f(x)=3x^2')
plt.plot(x_coordinates,y_coordinate2,'x',label='f(x)=4x-3')

plt.title('Graph of y=f(x), f(x)=3x^2 and f(x)=4x-3') #adding title
plt.xlabel('x values') #labeling x-axis
plt.ylabel('y values') #labeling y-axis
plt.grid(True)#adding grid
plt.legend() #adding legend
plt.show #displaying

