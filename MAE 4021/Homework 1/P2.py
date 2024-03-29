"""
Dylan Copley
MAE 4021
Homework 1
Problem 2

"""

#function height(t)
def height(t):
    #nothing to declare, simply return value generated by function
    #in python, exponents handled by **, n**2 == n^2
    return ((-9.81/2)*(t**2)) + (125*t) + 500


#creating "linspace"... using numpy module, named np. Native range() function doesnt support decimal step values
import numpy as np

t_vec = np.arange(0,30,0.5)

#list comprehension. This technique avoids bad practice of rewriting data and also saves computing time by not
#declaring an empty list or appending. height(t) is called as the modifier. t is arbitrary.

height_vec = [height(t) for t in t_vec]

#importing matplotlib for plotting

import matplotlib.pyplot as plt

#have to add a subplot for later part of labeling specific points on plot, weird graphics stuff
#https://stackoverflow.com/questions/22272081/label-python-data-points-on-plot/22272358
ax = plt.figure().add_subplot(111)

#plotting
plt.plot(t_vec,height_vec)
#prettifying
plt.title("Rocket height over time")
plt.xlabel("Time")
plt.ylabel("Height")
plt.grid(True)

"""
#"Find the time when the rocket starts to fall back to the ground"
#once plot is generated, its clear that the rocket begins to fall back at around t = 12.5 seconds.
#Labeling x,y position with red dot
plt.plot(12.5,height(12.5),'ro')

#Bit tricky but nothing a google search cant fix. Text is passed and then a coordinate
#is passed in a tuple for whatever reason. Tuples are lists but content is unchangeable (a1,a2...) vs [a1,a2...] 
ax.annotate('Max Height',(12.5,height(12.5)))

#show
plt.show()
"""
#######################################################################

#extra code cause im bored; "Find the time when the rocket starts to fall back to the ground"
#this can also be programmed pretty easily using dy/dt.

#dy/dt is pretty simple algorithim that you can do: out[i] = a[i+1] - a[i]
#however numpy has this natively with np.diff(list/array object)

dh = np.diff(height_vec)

#iterate through dh and see where values go from positive to negative. Bit sloppy but works for this case
#start iterator at 0, remember list indexes start from 0. Stop iterating when negative.
n=0
while dh[n] > 0:
    #n+=1 is the same as n = n + 1
    n+=1

#time vector and height vector are of same length
#use this info to plot location, obtain time and position values from indexer.
plt.plot(t_vec[n],height_vec[n],'ro')
#annotate.
ax.annotate('Max Height',(t_vec[n],height_vec[n]))
#show plot
plt.show()
