"""
Dylan Copley
MAE 5020
Homework 1
Problem 2

Animation function added to show not only the function polygon(s) works but also how to do animations in python.
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os


#function that plots the polygon, then returns the decoded rgb and image property info
def polygon_anim(s):
    #defining angles
    angles = [(360/s)*n for n in range(0,s)]

    #defining points from angles, list comprehension except each value is a list itself. index 0 and 1 are x and y.
    points = [[np.cos(n * (np.pi / 180)), np.sin(n * (np.pi / 180))] for n in angles]

    #simply appending the last point as the initial point. This way when lines are needed to be drawn the last points
    #and the initial point will have its line drawn.
    points.append(points[0])

    #defining a subplot to play around with draw modes
    fig, ax = plt.subplots()

    #for each point,
    for n in range(0,len(points)-1):
        #bit tricky to read,
        #plt.plot([x1,x2],[y1,y2],'red line solid dot points')
        #points[n][0] are x value, points[n][1] are y value.
        #have to do a ax subplot plot to send current frame
        ax.plot([points[n][0],points[n+1][0]],[points[n][1],points[n+1][1]],'ro-')


    #pretifying
    ax.set_title("Number of sides: " + str(s))
    ax.grid(True)
    ax.set_xlim([-2,2])
    #took an image of plot window, discovered that the scaling ratio of x to y was about 1.343
    #this makes the x and y scales the same, and a prettier image.
    ax.set_ylim([-2/1.343,2/1.343])
    #showing origin
    ax.plot([0],[0],'bo')

    #maximize and grab current frame. I have no clue how I got this code, I borrowed it from an old program.
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    #return frame generated
    return image

#getting root directory, need to save the gif file somewhere
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#very scary function
#imageio.mimsave((PATH),[list comprehension with each value being a current frame image],fps=n)
#create a gif file stored in the root directory of the program.
#list comprehension generating 27 polygons from 3 to 14. defined fps as 4.
#image is saved as animated_polygon.gif. file will overwrite if program ran again

imageio.mimsave((ROOT_DIR + "\\animated_polygon.gif"),[polygon_anim(s) for s in range(3,15)], fps=4)