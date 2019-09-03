"""
Dylan Copley
MAE 5020
Homework 1
Problem 1

"""

import matplotlib.pyplot as plt
import numpy as np

A = 5
xn = 1

def halley(A,x1,crit):

    if x1 == 0:
        print("Initial guess must be greater than 0")
        return False
    #little math action here, check notes on divergence/convergence
    elif x1 > ((7*A)/3)**0.5:
        print("Broke critical initial guess, guess smaller")
        return False

    #declaring xn vals to analyze later, declaring initial guess x1
    xn_vals = [x1]

    #declaring initial xn
    xn = x1

    #while absolute difference of current answer is greater than the criteria, iterate
    while np.abs(xn - np.sqrt(A)) > crit:
        #Found out the hard way this algorithm breaks sometimes, testing if xn is blowing up to infinity
        if xn > A**2:
            print("Im broken " + str(xn))
            return False
        else:
            #formula stuff
            yn = (1/A)*(xn**2)
            xn = (xn/8)*(15-(yn*(10-(3*yn))))
            #append current xn value
            xn_vals.append(xn)

    #returning a list, good way to return multiple variables from a function in python.
    #First index is final val, second index is val list
    return [xn,xn_vals]


approx = halley(5,2,0.00000001)

#xn_vals over iteration stored in second index, grab [1]
plt.plot(approx[1])
plt.hlines(np.sqrt(5),0,len(approx[1])+1)
plt.grid(True)
plt.show()


