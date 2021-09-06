# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:22:14 2019

@author: AMITAVACHAKRABORTY
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import meshgrid,linspace,zeros,dot,norm,cross,vstack,array,matrix,sqrt



def rotmatrix(axis,costheta):
    """ Calculate rotation matrix

    Arguments:
    - `axis`     : Rotation axis
    - `costheta` : Rotation angle
    """
    x,y,z = axis
    c = costheta
    s = sqrt(1-c*c)
    C = 1-c
    return  matrix([[ x*x*C+c,    x*y*C-z*s,  x*z*C+y*s ],
                    [ y*x*C+z*s,  y*y*C+c,    y*z*C-x*s ],
                    [ z*x*C-y*s,  z*y*C+x*s,  z*z*C+c   ]])

def plane(Lx,Ly,Nx,Ny,n,d):
    """ Calculate points of a generic plane 

    Arguments:
    - `Lx` : Plane Length first direction
    - `Ly` : Plane Length second direction
    - `Nx` : Number of points, first direction
    - `Ny` : Number of points, second direction
    - `n`  : Plane orientation, normal vector
    - `d`  : distance from the origin
    """

    x = linspace(-Lx/2,Lx/2,Nx)
    y = linspace(-Ly/2,Ly/2,Ny)
    # Create the mesh grid, of a XY plane sitting on the orgin
    X,Y = meshgrid(x,y)
    Z   = zeros([Nx,Ny])
    n0 = array([0,0,1])

    # Rotate plane to the given normal vector
    if any(n0!=n):
        costheta = dot(n0,n)/(norm(n0)*norm(n))
        axis     = cross(n0,n)/norm(cross(n0,n))
        rotMatrix = rotmatrix(axis,costheta)
        XYZ = vstack([X.flatten(),Y.flatten(),Z.flatten()])
        X,Y,Z = array(rotMatrix*XYZ).reshape(3,Nx,Ny)

    dVec = (n/norm(n))*d
    X,Y,Z = X+dVec[0],Y+dVec[1],Z+dVec[2]
    return X,Y,Z


if __name__ == "__main__":

    # Plot as many planes as you like
    Nplanes = 1

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
        X,Y,Z = plane(20,20,100,100,normalVector,distList[i])

        print(X)
        print (X.shape)
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