"""
Dylan Copley
MAE 5020
Homework 1
Problem 3

"""

import numpy as np

def e_aprox(k):

    #A list that is k long of random integers generated from 1 to k. Why numpy makes you set parameters using low=
    #and high = is beyond me, should be able to just pass a range or tuple.
    #docs: https://www.geeksforgeeks.org/random-sampling-in-numpy-randint-function/
    integers = [np.random.randint(low=1,high=k) for n in range(0,k)]

    #setting value of non_gens to 0
    non_gen = 0
    #for all numbers between 1 and k
    for n in range(1,k):
        #if current number wasnt generated
        if n not in integers:
            #add 1 to non_gen counter
            non_gen+=1

    #return value of e, given as k/non_gen
    return k/non_gen


print("Approximated value of e: " + str(e_aprox(10000)))
print("Actual value of e: " + str(np.e))
