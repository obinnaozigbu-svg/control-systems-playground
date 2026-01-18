import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation parameters
# -----------------------------
dt = 0.001
t_end = 5.0
t = np.arange(0, t_end, dt)

# -----------------------------
# Plant parameters
# -----------------------------
m = 1.0      # mass
b = 0.4      # damping coefficient

# -----------------------------
# Controller gains (PD)
# -----------------------------
Kp = 20.0
Kd = 0.0

# -----------------------------
# Reference
# -----------------------------
r = 1.0      # desired position

# -----------------------------
# State initialization
# -----------------------------
x1 = 0.0     # position
x2 = 0.0     # velocity

# Data storage
y = []

# -----------------------------
# Simulation loop
# -----------------------------
for _ in t:
    # Control error
    error = r - x1

    # PD control law
    u = Kp * error - Kd * x2

    # State derivatives (from model.md)
    x1_dot = x2
    x2_dot = (u - b * x2) / m

    # Euler integration
    x1 += x1_dot * dt
    x2 += x2_dot * dt

    # Store output
    y.append(x1)

# -----------------------------
# Plot result
# -----------------------------
plt.plot(t, y, label="Position")
plt.axhline(r, linestyle="--", label="Setpoint")
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.legend()
plt.show()

