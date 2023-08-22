# -*- coding: utf-8 -*-
"""
Scipy Examples - constants
@author: AMITAVA
"""

"""
Scipy documentation for all the constants
https://docs.scipy.org/doc/scipy/reference/constants.html
"""
#%% - 
from scipy import constants
print (constants.value('elementary charge'))
from scipy import constants
print(constants.unit('proton mass'))
from scipy import constants
print(constants.precision('proton mass'))


from scipy.constants import find, physical_constants
#Which keys in the physical_constants dictionary contain ‘boltzmann’?

find('boltzmann')

#Get the constant called ‘Boltzmann constant in Hz/K’:
physical_constants['Boltzmann constant in Hz/K']

#Find constants with ‘radius’ in the key:

find('radius')

physical_constants['classical electron radius']

from scipy.constants import convert_temperature
import numpy as np
convert_temperature(np.array([-40, 40]), 'Celsius', 'Kelvin')

from scipy.constants import lambda2nu, speed_of_light
import numpy as np
lambda2nu(np.array((1, speed_of_light)))

from scipy.constants import nu2lambda, speed_of_light
import numpy as np
nu2lambda(np.array((1, speed_of_light)))
