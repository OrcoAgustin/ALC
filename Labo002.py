import numpy as np
import matplotlib.pyplot as plt

def proyectarPts(x,y):
    plt.plot(x/2,y/2,color='black',linewidth = 2, marker = 'o') 
    plt.axhline(0, color='black',linewidth=2)
    plt.axvline(0, color='black',linewidth=2)   
    plt.show()

proyectarPts([1,2,3],[4,5,6])