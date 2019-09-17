"""
Dylan Copley
MAE 4020
Problem 3
Bisection method


"""

import numpy as np
import matplotlib.pyplot as plt



y = "(x**3)-(x)-np.exp(x)-2"


def QuadSectRoot(fun,a,b):
    x_lins = np.arange(a, b, np.abs(a-b)/4)
    vals = [eval(fun) for x in x_lins]
    svals = [np.sign(n) for n in vals]


    for n in range(0, len(svals) - 1):
        if svals[n] != svals[n + 1]:
            #flag list contains previous iteration and stopping iteration
            #iteration that looks for sign change is feed through
            flags = [x_lins[n],x_lins[n]]

    #only looking at first flagged instance, problem specifies range of 2 to 3 anyways
    #estimation should be lower bound of flag
    return flags


print(QuadSectRoot(y,2,3))
est = []

