# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:01:06 2026

@author: 91837
"""

import numpy as np
import matplotlib.pyplot as plt

# Inputs
#v = 20  # initial velocity (m/s)
#theta = 45  # angle (degrees)

g = 9.8  # gravity
v = float(input("Enter velocity: "))
theta = float(input("Enter angle: "))

# Convert angle to radians
theta_rad = np.radians(theta)

# Time of flight
t_flight = (2 * v * np.sin(theta_rad)) / g

# Time values
t = np.linspace(0, t_flight, num=100)

# Equations
x = v * np.cos(theta_rad) * t
y = v * np.sin(theta_rad) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()

plt.show()
plt.savefig("projectile for v_theta.png")

