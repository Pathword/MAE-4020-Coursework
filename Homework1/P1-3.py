"""
Dylan Copley
MAE 4020
Homework 1
Problems 1-3

"""
####################################################################################

###problem 1

#defining function lbf2n as a function of F
def lbf2n(F):
    #nothing to declare, simply return value
    return (F*4.44822)


####################################################################################


###problem 2

#defining function in2m as a function of inch
def in2m(inch):
    # nothing to declare, simply return value
    return (inch*0.0254)


####################################################################################


###problem 3

#data is declared in a list. Could potentially import .txt or .xlsx file of formatted data

stress_data_raw = [0,2000,4000,6000,7500,8000,9500,9000,9500,10000]
strain_data_raw = [2,2.0024,2.0047,2.007,2.0094,2.0128,2.0183,2.0308,2.05,2.075]

#importing matplotlib package, specifically pyplot module and declaring it as user friendly "plt".
#usually good practice to import all modules at the beginning of your code

import matplotlib.pyplot as plt

#list comprehension. "stress_data" is equal to a list generated by iterating over stress_data_raw and
#modifiying iterator n. This technique avoids bad practice of rewriting data #and also saves computing time by not
#declaring an empty list or appending. lbf2n and in2m are called as the modifiers.

stress_data = [lbf2n(n) for n in stress_data_raw]
strain_data = [in2m(n) for n in strain_data_raw]

#plotting.
plt.plot(strain_data,stress_data)
#prettifying
plt.title("Problem 3: Stress Strain Data")
plt.xlabel("strain (m)")
plt.ylabel("stress (N)")
plt.grid(True)
#show figure.
plt.show()




