# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:09:20 2025

The purpose of this code is to calculate the thermal noice and signal-to-noise ratio (SNR) in a detector
which helps to visualize how temperatures and esistance affect detector sensitivity.

@author: Tomi Wang
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.38e-23  # Boltzmann constant in J/K
bandwidth = 1e3  # Detector bandwidth in Hz (1 kHz)
R = 1000 # Resistance in ohms (Ω)
signal_amplitude = 1e-6 # Signal amplitude in volts (V)
temperatures = np.linspace(1, 300, 100) # Temperature range from 1 K to 300 K

# Functions
def thermal_noise(T, R):
    """Calculates the thermal (Johnson–Nyquist) noise voltage for a given temperature and resistance."""
    return np.sqrt(4 * k_B * T * R * bandwidth)

def calculate_snr(T, R, signal_amplitude):
    """Calculates SNR using thermal noise and a fixed signal amplitude."""
    noise_voltage_rms = thermal_noise(T, R)
    return signal_amplitude / noise_voltage_rms

# Simulation parameters
temperatures = np.linspace(1, 300, 100)
signal_amplitude = 1e-6  # Signal amplitude in volts

# Fixed resistance for SNR demonstration
R_fixed = 1000

# Compute SNR for fixed resistance
snr = calculate_snr(temperatures, R_fixed, signal_amplitude)

# Example resistances for noise demonstration
resistances = [10, 100, 1000]

# Plotting
plt.figure(figsize=(12, 5))

# Subplot 1: SNR vs Temperature
plt.subplot(1, 2, 1)
plt.plot(temperatures, snr, label=f'SNR (R = {R_fixed} Ω)', color='blue')
plt.xlabel('Temperature (K)')
plt.ylabel('SNR')
plt.title('Effect of Temperature on SNR')
plt.grid(True)
plt.legend()

# Subplot 2: Thermal Noise vs Temperature for Different Resistances
plt.subplot(1, 2, 2)
for R in resistances:
    noise = thermal_noise(temperatures, R)
    plt.plot(temperatures, noise, label=f'R = {R} Ω')
plt.xlabel('Temperature (K)')
plt.ylabel('Thermal Noise Voltage (V)')
plt.title('Thermal Noise vs Temperature')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

"""
The code computes thermal noise and SNR across a range of temperatures to show how temperature affects
detector sensitivity.
"""