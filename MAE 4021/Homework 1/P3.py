"""
Dylan Copley
MAE 4021
Homework 1
Problem 3

"""



#importing numpy package as user friendly np, contains useful math tools
import numpy as np
#importing matplotlib.pyplot for plotting tools
import matplotlib.pyplot as plt

#defining function distance as function of r and h.
def distance(r,h):
    #nothing to declare, simply return modified value
    #exponents are handled by double asterisk ** in python. h**2 == h^2
    #sqrt(n) == n**0.5 == n^0.5
    return (((2*r*h)+(h**2))**0.5)

#declaring r values
earth_r = 7926/2
mars_r = 4217/2

#creating linspace vector (numpy array) from 0 to 10000 feet. Also converted feet to miles.
hills = np.linspace(0,10000*0.000189394)

#list comprehension. See P1-3
d2h_earth = [distance(earth_r,h) for h in hills]
d2h_mars = [distance(mars_r,h) for h in hills]

#plotting with color. Note how "hill" is of class (ndarray) and d2h_earth is of class (list).
#this is automatically handled by matplotlib. Declaring color. Since a legend is to be added, a label is declared.
#
plt.plot(hills,d2h_earth,'b',label='Earth')

#plt automatically "holds" figure until shown.
plt.plot(hills,d2h_mars,'r',label='Mars')

#prettifying
plt.title("Distance to horizon as function of vertical distance h")
plt.xlabel("Miles to horizon")
plt.ylabel("Miles traveled vertically")
plt.grid(True)

#labels have been declared, initializing legend
plt.legend()

#show figure
plt.show()
