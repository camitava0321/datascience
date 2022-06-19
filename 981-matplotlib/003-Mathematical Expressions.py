# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Mathematical Expressions
"""
"""
You can use a subset TeXmarkup in any Matplotlib text string by placing it inside a pair of dollar signs ($).
e.g., plt.title(r'$\alpha > \beta$')

#To make subscripts and superscripts, use the '_' and '^' symbols −
e.g., r'$\alpha_i> \beta_i$'
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)
plt.title(r'$\alpha_i> \beta_i$', fontsize=20)

plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize = 20)
plt.text(0.1, -0.5, r'$\sqrt{2}$', fontsize=10)
plt.xlabel('time (s)')
plt.ylabel('volts (mV)')
plt.show()