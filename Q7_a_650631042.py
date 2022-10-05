# -*- coding: utf-8 -*-
"""Q7_a

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eBFhfMI3OyL10qEkt66OAiMi0tsFMjDN
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 5) #Plot from -pi to pi with point.
plt.plot(x, np.sin(x)) # 'plot' use with "continues data".
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.show()