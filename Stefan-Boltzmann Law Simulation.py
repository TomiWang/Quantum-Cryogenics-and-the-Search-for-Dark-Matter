# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:53:19 2025

The purpose of this code is to calculate the power radiated by a surface
due to thermal emission, following the Stefan-Boltzmann Law.

@author: Tomi Wang
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
sigma = 5.67e-8  # Stefan-Boltzmann constant in W/m^2/K^4
emissivity = 0.9  # Example emissivity
area = 1.0  # Radiator surface area in m^2
T_min = 1    # Minimum temperature in K
T_max = 300  # Maximum temperature in K
num_points = 100  # Number of temperature samples

# Stefan-Boltzmann power radiated
def radiative_power(T):
    return emissivity * sigma * area * T**4

# Temperature range (K)
temperatures = np.linspace(1, 300, 100)

# Calculate radiative power
power = radiative_power(temperatures)

# Plot the power vs. temperature
plt.figure(figsize=(8, 5))
plt.plot(temperatures, power, color='purple', label='Radiative Power')
plt.xlabel('Temperature (K)')
plt.ylabel('Power Radiated (W)')
plt.title('Stefan-Boltzmann Law: Radiative Power vs. Temperature')
plt.grid(True)
plt.legend()
plt.show()

"""
The surface is assumed to have a given emissivity and area.
The radiative power for temperatures ranging from 1K to 300 K
is then computed. Power is plotted as a function of temperature,
showing how much thermal radiation increases with temperature.
"""