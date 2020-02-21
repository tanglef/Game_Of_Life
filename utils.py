# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:08:08 2020

@author: tanguy
description: calculation and display functions
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

def display_sub(lst,title,nrow,ncol):
    """Display the subplots for the iterations from a list in a nrow x ncol grid.
    
    Keyword arguments:
        lst -- list of the arrays to plot
        title -- a string for the title of the main plot
        nrow -- number of rows in the grid (integer)
        ncol -- number of columns in the grid (integer)
    """
    fig, axes = plt.subplots(nrow,ncol, num=title)
    for i, ax in enumerate(axes.ravel()):   
        im = ax.imshow(lst[i], cmap='cool')
        ax.set_title("iteration "+str(i))
    plt.tight_layout()
    
def display_pic(name_picture,title):
    """Display a saved picture using pyplot imread() function.
    
    Keyword arguments:
        name_picture -- string for the path (or just name) of the picture
        title -- a string for the title of the picture
    """
    image = plt.imread(name_picture)
    plt.figure(num=title)
    plt.imshow(image)
    plt.axis('off')
    
def display_one_plot(array,title, cmap='viridis'):
    """Display a created plot from a numpy array (a heatmap).
    
    Keyword arguments:
        array -- 2D numpy array to display
        title -- a string for the title of the plot
        cmap -- matplotlib usual cmap, viridis as default
    """
    plt.figure(num=title)
    plt.imshow(array,cmap=cmap)
    plt.show()
    
def anim_game(im_init,fct_update,frames_nb,title):
    """Display the animation for the game from an initial grid.
    
    Keyword arguments:
        im_init -- 2D numpy array (binary for the game of life)
        fct_update -- the function which will update the data in the grid for each iteration
        frames_nb -- int or iterable (or more : see matplotlib.animation.FuncAnimation help)
        title -- a string for the title of the movie.
    """
    plt.figure(num=title)
    fig = plt.gcf()
    im = plt.imshow(im_init,cmap='cool')
    plt.show()
    def animate(frame):
        im.set_data(fct_update(im_init))
        return im,
    anim = animation.FuncAnimation(fig, animate,frames=frames_nb)
    return(anim)

def plot_ten_iterations(grid,title,func):
    """Display the first ten iterations of a grid.
    
    Keyword arguments:
        grid -- 2D numpy array to display (binary for the game of life)
        title -- a string for the title of the plot
        func -- a function that will update the data in the grid
    """
    iterations = [0] * 10  #initialize the stocking device
    iterations[0] = grid 
    for i in range(1, 10):
        iterations[i] = func(np.copy(iterations[i-1]))
    display_sub(iterations, title, 2, 5)

    
### stable configs --------------
first_config = np.zeros((50,50))
inside = np.array([[1,1],[1,1]])
first_config[35:37,35:37] = first_config[6:8,6:8] = first_config[25:27,25:27] = inside

second_config = np.zeros((50,50))
stable_2 = np.array([[0,1,1,0],[1,0,0,1],[0,1,0,1],[0,0,1,0]])
second_config[32:36,32:36] = second_config[6:10,6:10] = second_config[25:29,25:29] = stable_2

stable_3 = np.array([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])
third_config = np.zeros((50,50))
third_config[14:18,14:17] = third_config[6:10,6:9] = third_config[25:29,25:28] = stable_3

### 2-periodic configs ------------
inside_pattern = np.zeros((7,7))
inside_pattern[0,2:5] = inside_pattern[-1,2:5] = inside_pattern[2:5,0] = inside_pattern[2:5,-1] = 1
fourth_config = np.zeros((50,50))
fourth_config[30:37,30:37] = fourth_config[2:9,2:9] = fourth_config[15:22,15:22] = inside_pattern


