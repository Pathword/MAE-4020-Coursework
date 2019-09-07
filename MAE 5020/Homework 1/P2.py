"""
Dylan Copley
MAE 5020
Homework 1
Problem 2

This problem was a lot easier than expected, simply generate rays outward from the origin. Number of rays defined by
number of angles, or number of sides. Each ray then had its x and y components taken to achieve all of the polygon's
vertices. From there, simply needed to iterate over the point vertices and draw a line between each vertice.

Animation function added to show not only the function polygon(s) works but also how to do animations in python.
"""

import numpy as np
import matplotlib.pyplot as plt


def polygon(s):
    #defining angles
    angles = [(360/s)*n for n in range(0,s)]

    #defining points from angles, list comprehension except each value is a list itself. index 0 and 1 are x and y.
    points = [[np.cos(n * (np.pi / 180)), np.sin(n * (np.pi / 180))] for n in angles]

    #simply appending the last point as the initial point. This way when lines are needed to be drawn the last points
    #and the initial point will have its line drawn.
    points.append(points[0])

    #for each point,
    for n in range(0,len(points)-1):
        #bit tricky to read,
        #plt.plot([x1,x2],[y1,y2],'red line solid dot points')
        #points[n][0] are x value, points[n][1] are y value.
        plt.plot([points[n][0],points[n+1][0]],[points[n][1],points[n+1][1]],'ro-')

    #pretifying
    plt.title("Number of sides: " + str(s))
    plt.grid(True)
    plt.xlim([-2,2])
    #took an image of plot window, discovered that the scaling ratio of x to y was about 1.81
    #this makes the x and y scales the same, and a prettier image. Fullscreen image.
    plt.ylim([-2/1.81,2/1.81])
    #showing origin
    plt.plot([0],[0],'bo')
    plt.show()

polygon(5)