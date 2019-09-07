"""
Dylan Copley
MAE 5020
Homework 1
Problem 1 - extra, investigating bounds of halley iterative function. Note the criteria is not difference between
#xn and xn-1, instead its difference between actual root A and current iteration, however maintain same concept
#of convergence.

"""

import matplotlib.pyplot as plt
import numpy as np

A = 5
xn = 1

def halley(A,x1,crit):

    """
    if x1 == 0:
        return False
    #little math action here, check notes on divergence/convergence
    elif x1 > ((7*A)/3)**0.5:
        return False
    """

    #declaring xn vals to analyze later, declaring initial guess x1
    xn_vals = [x1]

    #declaring initial xn
    xn = x1

    #while absolute difference of current answer is greater than the criteria, iterate
    while np.abs(xn - np.sqrt(A)) > crit:
        #Found out the hard way this algorithm breaks sometimes, testing if xn is blowing up to infinity
        #eq can also go to 0, meaning infinite iterations
        if xn > A**2:
            return False
        elif xn == 0:
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

"""
approx = halley(5,2,0.00000001)

#xn_vals over iteration stored in second index, grab [1]
plt.plot(approx[1])
plt.hlines(np.sqrt(5),0,len(approx[1])+1)
plt.grid(True)
plt.show()
"""

#################################################################

#extra cause im bored, investigating bounds
#noticed that iteration would truncate to 0 if initial guess was 0, makes sense
#also noticed that there seemed to be a maximum value which could not be exceeded or algorithm would blow up to inf.
#Question: what is that upper bound?
#solution: iterate over values of x1 for some initial value A, see if algorithm converges or diverges.
#log # of iterations while were at it

iters = []
crit = 1e-15


#very fancy list comprehension, current value is equal to number of iterations taken from inital guess x1.
#x1 is iterated using np.arange, taking steps of 0.01
#if statement is simply checking if halley diverges or truncates to 0, because in halley function
#(lines 35-38) return a boolean false statement. If some content is returned, no matter class,
#if statement will say true and store value.

A = 5
iters = [len(halley(A,x1,crit)[1]) for x1 in np.arange(0,A,0.01) if halley(A,x1,crit)]

#since using step of 0.01, can assume max x1 is just length of iters times step value.
max_x1 = len(iters)*0.01

#plotting to investigate
#making sure plot of x scale and y scale are the same length, matplotlib yells at you if theyre not
fig = plt.figure()
plt.plot(np.arange(0,len(iters)*0.01,0.01),iters)
plt.xlabel('initial guess')
plt.ylabel('iterations to achieve crit')
plt.title("A = " + str(A) + "\n" + "ratio of sqrt(A) to x1: " + str(round((np.sqrt(A)/max_x1),4)))
fig.show()


#trying again with litteraly a random integer to show that a relationship exists between max initial guess and A
A = np.random.randint(26,63)
iters = [len(halley(A,x1,crit)[1]) for x1 in np.arange(0,A,0.01) if halley(A,x1,crit)]

#since using step of 0.01, can assume max x1 is just length of iters times step value.
max_x1 = len(iters)*0.01

#plotting to investigate
#making sure plot of x scale and y scale are the same length, matplotlib yells at you if theyre not
fig = plt.figure()
plt.plot(np.arange(0,len(iters)*0.01,0.01),iters)
plt.xlabel('initial guess')
plt.ylabel('iterations to achieve crit')
plt.title("A = " + str(A) + "\n" + "ratio of sqrt(A) to x1: " + str(round((np.sqrt(A)/max_x1),4)))
fig.show()

#########################################

#extremely clear that there exists some relationship between A and the critical guess by simply a coefficient
#The coefficient of A to the critical initial guess is sqrt((7/3)*A).
#see work on github, P1_extra_critical_guess_solution.pdf
#additionally, its clear that less iterations are needed if initial guess is close to final answer of sqrt(A)