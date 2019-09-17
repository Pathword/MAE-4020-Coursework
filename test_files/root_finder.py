import matplotlib.pyplot as plt
import numpy as np


def mass(L):
    #length units in meters
    b = 10.16 / 100
    R = 23.5 / 100
    L2 = 35.5 / 100
    #kg/m^3
    rho = 997
    #mass equation from prelab question 6
    mass = (1/L2)*(0.5)*(b)*(rho)*((R-L)**2)*(((2/3)*(R-L))+L)
    #mass returned in kg
    return mass

actual_length = [17.11,15.59,14.39,12.25]
actual_mass = [100,150,200,300]


length_lin = np.arange(10,30,0.01)


for entry in actual_mass:
    #root finding
    ans = [(mass(n/100)*1000)-entry for n in length_lin]

    sign_change = [np.sign(n) for n in ans]

    #root finding, answer list has been converted to +1 or -1. looking for sign change
    n = 0
    while sign_change[n] == sign_change[n+1]:
        n+=1

    #index of sign change is of same index of length linspace
    print(str(entry) + " grams : " +  str(length_lin[n]) + " cm")