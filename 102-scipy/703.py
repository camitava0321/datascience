# -*- coding: utf-8 -*-
"""
Scipy Examples
@author: AMITAVA
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import integrate

#%% - Integrate
#The scipy.integrate sub-package provides several integration techniques 
#including an ordinary differential equation integrator. 
#An overview of the module
help(integrate)
"""
Methods for Integrating Functions given function object.
   quad          -- General purpose integration.
   dblquad       -- General purpose double integration.
   tplquad       -- General purpose triple integration.
   fixed_quad    -- Integrate func(x) using Gaussian quadrature of order n.
   quadrature    -- Integrate with given tolerance using Gaussian quadrature.
   romberg       -- Integrate func using Romberg integration.

Methods for Integrating Functions given fixed samples.
   trapz         -- Use trapezoidal rule to compute integral from samples.
   cumtrapz      -- Use trapezoidal rule to cumulatively compute integral.
   simps         -- Use Simpson's rule to compute integral from samples.
   romb          -- Use Romberg Integration to compute integral from
                    (2**k + 1) evenly-spaced samples.

See the special module's orthogonal polynomials (special) for Gaussian
quadrature roots and weights for other weighting factors and regions.

Interface to numerical integrators of ODE systems.
   odeint        -- General integration of ordinary differential equations.
   ode           -- Integrate ODE using VODE and ZVODE routines.
"""
#%% - General integration (quad) - to integrate a function of one variable between two points. 
#The points can be (+/- inf) to indicate infinite limits. 
#For example, suppose you wish to integrate a bessel function jv(2.5, x) along the interval 
import scipy.special as special
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
print (result)

from numpy import sqrt, sin, cos, pi
I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) +
                 sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])
print (I)
print(abs(result[0]-I))

#The first argument to quad is a ???callable??? Python object (i.e. a function, method, or class instance). 
#Notice the use of a lambda- function in this case as the argument. 
#The next two arguments are the limits of integration. 
#The return value is a tuple, with the first element holding the estimated value of the integral and 
#the second element holding an upper bound on the error. 

#Another example : integration of ax^2 + b from 0 to 1
from scipy.integrate import quad
def integrand(x, a, b):
    return a*x**2 + b
a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print (I)

#Infinite inputs are also allowed in quad by using +/-inf as one of the arguments. 
#For example -
from scipy.integrate import quad
def integrand(t, n, x):
    return np.exp(-x*t) / t**n

def expint(n, x):
    return quad(integrand, 1, np.inf, args=(n, x))[0]

vec_expint = np.vectorize(expint)
vec_expint(3, np.arange(1.0, 4.0, 0.5))

import scipy.special as special
special.expn(3, np.arange(1.0,4.0,0.5))

#The function which is integrated can even use the quad argument 
#(though the error bound may underestimate the error due to possible numerical error in the integrand from the use of quad ). 
#The integral in this case is
result = quad(lambda x: expint(3, x), 0, np.inf)
print(result)

I3 = 1.0/3.0
print(I3)

print(I3 - result[0])

#This last example shows that multiple integration can be handled using repeated calls to quad.

#%% - General multiple integration (dblquad, tplquad, nquad)
The mechanics for double and triple integration have been wrapped up into the functions dblquad and tplquad. These functions take the function to integrate and four, or six arguments, respectively. The limits of all inner integrals need to be defined as functions.

An example of using double integration to compute several values of  is shown below:

>>>
>>> from scipy.integrate import quad, dblquad
>>> def I(n):
...     return dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf, lambda x: 1, lambda x: np.inf)
...
>>>
>>> print(I(4))
(0.2500000000043577, 1.29830334693681e-08)
>>> print(I(3))
(0.33333333325010883, 1.3888461883425516e-08)
>>> print(I(2))
(0.4999999999985751, 1.3894083651858995e-08)
As example for non-constant limits consider the integral

This integral can be evaluated using the expression below (Note the use of the non-constant lambda functions for the upper limit of the inner integral):

>>>
>>> from scipy.integrate import dblquad
>>> area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
>>> area
(0.010416666666666668, 1.1564823173178715e-16)
For n-fold integration, scipy provides the function nquad. The integration bounds are an iterable object: either a list of constant bounds, or a list of functions for the non-constant integration bounds. The order of integration (and therefore the bounds) is from the innermost integral to the outermost one.

The integral from above

can be calculated as

>>>
>>> from scipy import integrate
>>> N = 5
>>> def f(t, x):
...    return np.exp(-x*t) / t**N
...
>>> integrate.nquad(f, [[1, np.inf],[0, np.inf]])
(0.20000000000002294, 1.2239614263187945e-08)
Note that the order of arguments for f must match the order of the integration bounds; i.e. the inner integral with respect to  is on the interval  and the outer integral with respect to  is on the interval .

Non-constant integration bounds can be treated in a similar manner; the example from above

can be evaluated by means of

>>>
>>> from scipy import integrate
>>> def f(x, y):
...     return x*y
...
>>> def bounds_y():
...     return [0, 0.5]
...
>>> def bounds_x(y):
...     return [0, 1-2*y]
...
>>> integrate.nquad(f, [bounds_x, bounds_y])
(0.010416666666666668, 4.101620128472366e-16)
which is the same result as before.

Gaussian quadrature
A few functions are also provided in order to perform simple Gaussian quadrature over a fixed interval. The first is fixed_quad which performs fixed-order Gaussian quadrature. The second function is quadrature which performs Gaussian quadrature of multiple orders until the difference in the integral estimate is beneath some tolerance supplied by the user. These functions both use the module special.orthogonal which can calculate the roots and quadrature weights of a large variety of orthogonal polynomials (the polynomials themselves are available as special functions returning instances of the polynomial class ??? e.g. special.legendre).

Romberg Integration
Romberg???s method [WPR] is another method for numerically evaluating an integral. See the help function for romberg for further details.

Integrating using Samples
If the samples are equally-spaced and the number of samples available is  for some integer , then Romberg romb integration can be used to obtain high-precision estimates of the integral using the available samples. Romberg integration uses the trapezoid rule at step-sizes related by a power of two and then performs Richardson extrapolation on these estimates to approximate the integral with a higher-degree of accuracy.

In case of arbitrary spaced samples, the two functions trapz (defined in numpy [NPT]) and simps are available. They are using Newton-Coates formulas of order 1 and 2 respectively to perform integration. The trapezoidal rule approximates the function as a straight line between adjacent points, while Simpson???s rule approximates the function between three adjacent points as a parabola.

For an odd number of samples that are equally spaced Simpson???s rule is exact if the function is a polynomial of order 3 or less. If the samples are not equally spaced, then the result is exact only if the function is a polynomial of order 2 or less.

>>>
>>> import numpy as np
>>> def f1(x):
...    return x**2
...
>>> def f2(x):
...    return x**3
...
>>> x = np.array([1,3,4])
>>> y1 = f1(x)
>>> from scipy.integrate import simps
>>> I1 = simps(y1, x)
>>> print(I1)
21.0
This corresponds exactly to

whereas integrating the second function

>>>
>>> y2 = f2(x)
>>> I2 = integrate.simps(y2, x)
>>> print(I2)
61.5
does not correspond to

because the order of the polynomial in f2 is larger than two.

Faster integration using low-level callback functions
A user desiring reduced integration times may pass a C function pointer through scipy.LowLevelCallable to quad, dblquad, tplquad or nquad and it will be integrated and return a result in Python. The performance increase here arises from two factors. The primary improvement is faster function evaluation, which is provided by compilation of the function itself. Additionally we have a speedup provided by the removal of function calls between C and Python in quad. This method may provide a speed improvements of ~2x for trivial functions such as sine but can produce a much more noticeable improvements (10x+) for more complex functions. This feature then, is geared towards a user with numerically intensive integrations willing to write a little C to reduce computation time significantly.

The approach can be used, for example, via ctypes in a few simple steps:

1.) Write an integrand function in C with the function signature double f(int n, double *x, void *user_data), where x is an array containing the point the function f is evaluated at, and user_data to arbitrary additional data you want to provide.

/* testlib.c */
double f(int n, double *x, void *user_data) {
    double c = *(double *)user_data;
    return c + x[0] - x[1] * x[2]; /* corresponds to c + x - y * z */
}
2.) Now compile this file to a shared/dynamic library (a quick search will help with this as it is OS-dependent). The user must link any math libraries, etc. used. On linux this looks like:

$ gcc -shared -fPIC -o testlib.so testlib.c
The output library will be referred to as testlib.so, but it may have a different file extension. A library has now been created that can be loaded into Python with ctypes.

3.) Load shared library into Python using ctypes and set restypes and argtypes - this allows Scipy to interpret the function correctly:

import os, ctypes
from scipy import integrate, LowLevelCallable

lib = ctypes.CDLL(os.path.abspath('testlib.so'))
lib.f.restype = ctypes.c_double
lib.f.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.c_void_p)

c = ctypes.c_double(1.0)
user_data = ctypes.cast(ctypes.pointer(c), ctypes.c_void_p)

func = LowLevelCallable(lib.f, user_data)
The last void *user_data in the function is optional and can be omitted (both in the C function and ctypes argtypes) if not needed. Note that the coordinates are passed in as an array of doubles rather than a separate argument.

4.) Now integrate the library function as normally, here using nquad:

>>>
>>> integrate.nquad(func, [[0, 10], [-10, 0], [-1, 1]])
(1200.0, 1.1102230246251565e-11)
The Python tuple is returned as expected in a reduced amount of time. All optional parameters can be used with this method including specifying singularities, infinite bounds, etc.

Ordinary differential equations (odeint)
Integrating a set of ordinary differential equations (ODEs) given initial conditions is another useful example. The function odeint is available in SciPy for integrating a first-order vector differential equation:

given initial conditions , where  is a length  vector and  is a mapping from  to  A higher-order ordinary differential equation can always be reduced to a differential equation of this type by introducing intermediate derivatives into the vector.

For example suppose it is desired to find the solution to the following second-order differential equation:

with initial conditions  and  It is known that the solution to this differential equation with these boundary conditions is the Airy function

which gives a means to check the integrator using special.airy.

First, convert this ODE into standard form by setting  and . Thus, the differential equation becomes

In other words,

As an interesting reminder, if  commutes with  under matrix multiplication, then this linear differential equation has an exact solution using the matrix exponential:

However, in this case,  and its integral do not commute.

There are many optional inputs and outputs available when using odeint which can help tune the solver. These additional inputs and outputs are not needed much of the time, however, and the three required input arguments and the output solution suffice. The required inputs are the function defining the derivative, fprime, the initial conditions vector, y0, and the time points to obtain a solution, t, (with the initial value point as the first element of this sequence). The output to odeint is a matrix where each row contains the solution vector at each requested time point (thus, the initial conditions are given in the first output row).

The following example illustrates the use of odeint including the usage of the Dfun option which allows the user to specify a gradient (with respect to  ) of the function, .

>>>
>>> from scipy.integrate import odeint
>>> from scipy.special import gamma, airy
>>> y1_0 = 1.0 / 3**(2.0/3.0) / gamma(2.0/3.0)
>>> y0_0 = -1.0 / 3**(1.0/3.0) / gamma(1.0/3.0)
>>> y0 = [y0_0, y1_0]
>>> def func(y, t):
...     return [t*y[1],y[0]]
...
>>>
>>> def gradient(y, t):
...     return [[0,t], [1,0]]
...
>>>
>>> x = np.arange(0, 4.0, 0.01)
>>> t = x
>>> ychk = airy(x)[0]
>>> y = odeint(func, y0, t)
>>> y2 = odeint(func, y0, t, Dfun=gradient)
>>>
>>> ychk[:36:6]
array([0.355028, 0.339511, 0.324068, 0.308763, 0.293658, 0.278806])
>>>
>>> y[:36:6,1]
array([0.355028, 0.339511, 0.324067, 0.308763, 0.293658, 0.278806])
>>>
>>> y2[:36:6,1]
array([0.355028, 0.339511, 0.324067, 0.308763, 0.293658, 0.278806])
Solving a system with a banded Jacobian matrix
odeint can be told that the Jacobian is banded. For a large system of differential equations that are known to be stiff, this can improve performance significantly.

As an example, we???ll solve the one-dimensional Gray-Scott partial differential equations using the method of lines [MOL]. The Gray-Scott equations for the functions  and  on the interval  are

where  and  are the diffusion coefficients of the components  and , respectively, and  and  are constants. (For more information about the system, see http://groups.csail.mit.edu/mac/projects/amorphous/GrayScott/)

We???ll assume Neumann (i.e. ???no flux???) boundary conditions:

To apply the method of lines, we discretize the  variable by defining the uniformly spaced grid of  points , with  and . We define  and , and replace the  derivatives with finite differences. That is,

We then have a system of  ordinary differential equations:

(1)
For convenience, the  arguments have been dropped.

To enforce the boundary conditions, we introduce ???ghost??? points  and , and define , ;  and  are defined analogously.

Then

(2)
and

(3)
Our complete system of  ordinary differential equations is (1) for , along with (2) and (3).

We can now starting implementing this system in code. We must combine  and  into a single vector of length . The two obvious choices are  and . Mathematically, it does not matter, but the choice affects how efficiently odeint can solve the system. The reason is in how the order affects the pattern of the nonzero elements of the Jacobian matrix.

When the variables are ordered as , the pattern of nonzero elements of the Jacobian matrix is

The Jacobian pattern with variables interleaved as  is

In both cases, there are just five nontrivial diagonals, but when the variables are interleaved, the bandwidth is much smaller. That is, the main diagonal and the two diagonals immediately above and the two immediately below the main diagonal are the nonzero diagonals. This is important, because the inputs mu and ml of odeint are the upper and lower bandwidths of the Jacobian matrix. When the variables are interleaved, mu and ml are 2. When the variables are stacked with  following , the upper and lower bandwidths are .

With that decision made, we can write the function that implements the system of differential equations.

First, we define the functions for the source and reaction terms of the system:

def G(u, v, f, k):
    return f * (1 - u) - u*v**2

def H(u, v, f, k):
    return -(f + k) * v + u*v**2
Next we define the function that computes the right-hand-side of the system of differential equations:

def grayscott1d(y, t, f, k, Du, Dv, dx):
    """
    Differential equations for the 1D Gray-Scott equations.

    The ODEs are derived using the method of lines.
    """
    # The vectors u and v are interleaved in y.  We define
    # views of u and v by slicing y.
    u = y[::2]
    v = y[1::2]

    # dydt is the return value of this function.
    dydt = np.empty_like(y)

    # Just like u and v are views of the interleaved vectors
    # in y, dudt and dvdt are views of the interleaved output
    # vectors in dydt.
    dudt = dydt[::2]
    dvdt = dydt[1::2]

    # Compute du/dt and dv/dt.  The end points and the interior points
    # are handled separately.
    dudt[0]    = G(u[0],    v[0],    f, k) + Du * (-2.0*u[0] + 2.0*u[1]) / dx**2
    dudt[1:-1] = G(u[1:-1], v[1:-1], f, k) + Du * np.diff(u,2) / dx**2
    dudt[-1]   = G(u[-1],   v[-1],   f, k) + Du * (- 2.0*u[-1] + 2.0*u[-2]) / dx**2
    dvdt[0]    = H(u[0],    v[0],    f, k) + Dv * (-2.0*v[0] + 2.0*v[1]) / dx**2
    dvdt[1:-1] = H(u[1:-1], v[1:-1], f, k) + Dv * np.diff(v,2) / dx**2
    dvdt[-1]   = H(u[-1],   v[-1],   f, k) + Dv * (-2.0*v[-1] + 2.0*v[-2]) / dx**2

    return dydt
We won???t implement a function to compute the Jacobian, but we will tell odeint that the Jacobian matrix is banded. This allows the underlying solver (LSODA) to avoid computing values that it knows are zero. For a large system, this improves the performance significantly, as demonstrated in the following ipython session.

First, we define the required inputs:

In [31]: y0 = np.random.randn(5000)

In [32]: t = np.linspace(0, 50, 11)

In [33]: f = 0.024

In [34]: k = 0.055

In [35]: Du = 0.01

In [36]: Dv = 0.005

In [37]: dx = 0.025
Time the computation without taking advantage of the banded structure of the Jacobian matrix:

In [38]: %timeit sola = odeint(grayscott1d, y0, t, args=(f, k, Du, Dv, dx))
1 loop, best of 3: 25.2 s per loop
Now set ml=2 and mu=2, so odeint knows that the Jacobian matrix is banded:

In [39]: %timeit solb = odeint(grayscott1d, y0, t, args=(f, k, Du, Dv, dx), ml=2, mu=2)
10 loops, best of 3: 191 ms per loop
That is quite a bit faster!

Let???s ensure that they have computed the same result:

In [41]: np.allclose(sola, solb)
Out[41]: True
References
[WPR]	https://en.wikipedia.org/wiki/Romberg???s_method
[NPT]	https://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html
[MOL]	https://en.wikipedia.org/wiki/Method_of_lines
