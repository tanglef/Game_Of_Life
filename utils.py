# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:08:08 2020

@author: tanguy
description: calculation and display functions
"""
import matplotlib as plt

def display_sub(lst,title,nrow,ncol):
    fig, axes = plt.subplots(nrow, ncol, num=title)
    for i, ax in enumerate(axes.ravel()):   
        im = ax.imshow(lst[i], cmap='cool')
        ax.set_title("iteration "+str(i))
    plt.tight_layout()


