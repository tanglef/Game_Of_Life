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
    image = plt.imread(name_picture)
    plt.figure(num=title)
    plt.imshow(image)
    plt.axis('off')
    
def display_one_plot(array,title):
    plt.figure(num=title)
    plt.imshow(array)
    plt.show()
    
def anim_game(im_init,fct_update,frames_nb,title):
    plt.figure(num=title)
    fig = plt.gcf()
    im = plt.imshow(im_init,cmap='cool')
    plt.show()
    def animate(frame):
        im.set_data(fct_update(im_init))
        return im,
    anim = animation.FuncAnimation(fig, animate,frames=frames_nb)
    return(anim)
