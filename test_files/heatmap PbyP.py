import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import os
import time 
import numpy as np
import imageio

from PIL import Image


#store epi centers as tuples, immutable and just need to call



#getting a colormap, callable by cmap(x), where x is between 0 and 256?
cmap = matplotlib.cm.get_cmap('inferno')

#setting dimension (input as nxm)
#dim[0] = tall dim[1] = long

dim = [500,500]
print('dim: ' + str(dim))
print('ensure animation_test_frames folder is empty!')


#creating the epi_list, contains list of the locations and scalar values of all the epi centers, (location and degree)
#maximum z value in the epi_list should translate a scalar of 256, compare rest to this scalar
epi_list = []



#unitizes the epi_list intensity values to convert to a unit scale (0 to 1)
#if you use this  make sure that epi list is not a tuple!!! 
def unitize(epi_list):
    intensity_values = []
    
    for entry in epi_list:
        intensity_values.append(entry[2])

    max_intensity = max(intensity_values )

    for entry in epi_list:
        entry[2] = float(entry[2])/float(max_intensity)

    return epi_list
    



#effect of epicenter to pixel is a function of both the distance and the intensity
# "point" is a list of length 2 with x,y data, and source is a list of length 3 with x,y,z data 
def intensity_effect(point,source):
    #magnitude 
    mag = (((abs(point[0] - source[0]))**2)+(abs(point[1]-source[1])**2))**0.5

    #source intensity
    si = source[2]
    
    #function relating the two
    #intensity is unitized, between 0 and 1

    
    #modification: magnitude decreases by a root
    intensity = (float(si)**0.75)/(float((0.1*(float(mag)**1))+1))
    
    return intensity 



#steps pixel by pixel and tests the effects of all epicenters in the epilist to the pixel using a function 
#function of dimension as well, sets the m x n size and shape of the image
#returns a m x n array containing intensity values, later to 
def Create_aftermath(epi_list,dim):
    global i_at_point
    global resultant_intensity
    
    #creating empty array containing 0s
    aftermath = np.empty(dim)
    
    for x in range(0,dim[0]):
        for y in range(0,dim[1]):
            #all intensities at the point from resultant epicenters 
            i_at_point = []
            
            for entry in epi_list:
                i_at_point.append(intensity_effect((x,y),entry))

            #need some way to "collide" intensities, resultant intensities
            #sorting effect intensites from high to low, lower index = higher intensity
            list.sort(i_at_point,reverse= True)
            #setting the first resultant_intensity to the highest index
            
            resultant_intensity = i_at_point[0]

            #list comprehension to output a single resultant intensity value 
            for n in range(1,len(i_at_point)):
                resultant_intensity = resultant_intensity + (1-resultant_intensity)*i_at_point[n]**n
            
            
            

            #writing the resultant intensity to the aftermath pixel
            aftermath[x,y] = resultant_intensity 
                
    
    return aftermath


#just displays 
def disp_aftermath(aftermath):
    #im ax show method auto unitizes based on largest value, have to set point [0,0] to 1 because data is already unitized
    aftermath[0][0] = 1
    fig, ax = plt.subplots()
    im = ax.imshow(aftermath,cmap=cmap,)
    plt.show()

#displays with a specified cmap
def disp_aftermath_cmap(aftermath,cmap):
    plt.pcolor(aftermath,cmap=cmap,vmin=0,vmax=1)
    plt.show()


#animates number of frames from an epi_list, starting from 0 to its maximum value 
def animate_aftermath(epi_list,frames):
    global epi_list_interval,n,j
    start = time.time()
    
    #setting working directory to the animation_test_frame folder
    ani_path = os.getcwd() + '\\animation_test_frames'
    os.chdir(ani_path)
    fig = plt.figure()
    
    for n in range(frames):
        plt.clf()
        #reseting the epi_list_interval to its reference 
        epi_list_interval = []
        
        for j in range(len(epi_list)):
            #starting from 0 and increasing, when n = frames, maximum value 
            epi_list_interval.append([epi_list[j][0],epi_list[j][1],(epi_list[j][2]*(float(n)/float(frames)))])


        aftermath = Create_aftermath(epi_list_interval,dim)
        #im ax show method auto unitizes based on largest value, have to set point [0,0] to 1 because data is already unitized
        aftermath[0][0] = 1
    
        
        im = plt.imshow(aftermath,cmap=cmap)
        #saving figure as png
        plt.savefig('animated_' + str(n) + '.png', dpi =600, quality = 95)

    #animating
    filenames = []
    images = []
    for n in range(frames):
        filenames.append('animated_' + str(n) + '.png')

    for filename in filenames:
        images.append(imageio.imread(filename))    
        
    imageio.mimsave('test.mp4',images)


    #removing generated png images
    for n in range(frames):
        os.remove('animated_' + str(n) + '.png')

    print('Done. elapsed time (s):   ' + str(time.time()-start))
           

    

#creating 25 random epicenters with random intensities
#locations random but within bounds of the dim provided 
for n in range(0,30):
    #potential speed impovement, converting epi_list to tuple as information is immutable 
    epi_list.append(tuple([np.random.randint(1,dim[0]),np.random.randint(1,dim[1]),np.random.random(1)[0]]))

epi_list = tuple(epi_list)


start= time.time()
aftermath = Create_aftermath(epi_list,dim)
print('Time for aftermath = ' + str(time.time() - start))

disp_aftermath(aftermath)

"""
start = time.time()
disp_aftermath_cmap(aftermath,cmap)
print('Time for disp_aftermath_cmap = ' + str(time.time() - start))
"""
