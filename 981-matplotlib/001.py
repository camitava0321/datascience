# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:22:14 2019

@author: AMITAVACHAKRABORTY
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import meshgrid,linspace,zeros,dot,norm,cross,vstack,array,matrix,sqrt


def plane(X1,Y1,X2,Y2,n):
    """ Calculate points of a generic plane 

    Arguments:
    - `X1` : Plane Length first direction
    - `Y1` : Plane Length second direction
    - `X2` : Number of points, first direction
    - `Y2` : Number of points, second direction
    - `n`  : Plane orientation, normal vector
    - `d`  : distance from the origin
    """

    x = linspace(X1,X2,n)
    y = linspace(Y1,Y2,n)
    # Create the mesh grid, of a XY plane sitting on the orgin
    X,Y = meshgrid(x,y)
    Z   = zeros([10,10])
    print(X, X.shape)
    print(Y, Y.shape)
    print(Z, Z.shape)
    return X,Y,Z


if __name__ == "__main__":

    # Plot as many planes as you like
    Nplanes = 2

    # Set color list from a cmap
    colorList = cm.jet(linspace(0,1,Nplanes))

    # List of Distances
    distList = linspace(-10,10,Nplanes)

    # Plane orientation - normal vector
    normalVector = array([0,1,1]) # Y direction

    # Create figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plotting
    for i,ypos in enumerate(linspace(-10,10,10)):

        # Calculate plane
        X,Y,Z = plane(20,20,100,100,10)

        ax.plot_surface(X, Y, Z, rstride=5, cstride=5,
                        alpha=0.8, color=colorList[i])

    # Set plot display parameters    
    ax.set_xlabel('X')
    ax.set_xlim(-10, 10)
    ax.set_ylabel('Y')
    ax.set_ylim(-10, 10)
    ax.set_zlabel('Z')
    ax.set_zlim(-10, 10)

    plt.show()