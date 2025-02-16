# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:34:50 2025

The purpose of this code is to understand the velocity distribution of hypothetical dark matter particles.
This is crucial for predicting their interaction and detection probabilities from expierments.

@author: Tomi Wang :)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
mass = 1e-27  # Example particle mass in kg
k_B = 1.38e-23  # Boltzmann constant in J/K
temperature = 100  # Temperature in K
velocities = np.linspace(0, 1e4, 1000)  # Velocity range from 0 to 10,000 m/s

# Maxwell-Boltzmann distribution function
def boltzmann_distribution(v):
    return np.sqrt((mass / (2 * np.pi * k_B * temperature))) * np.exp(-mass * v**2 / (2 * k_B * temperature))

# Velocity range (m/s)
velocities = np.linspace(0, 1e4, 1000)
distribution = boltzmann_distribution(velocities)

# Plot the distribution
plt.figure(figsize=(8, 5))
plt.plot(velocities, distribution, label=f'T = {temperature} K')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Probability Density')
plt.title('Maxwell-Boltzmann Velocity Distribution')
plt.legend()
plt.grid(True)
plt.show()

"""
The code first defines constants, then implements the Maxwell-Boltzmann distribution function to calculate the
probability density of particle velocities. It also generates a range of velocities and evaluates the
distribution which is later plotted showing how likely different velocities are for particles at 100K.
"""
