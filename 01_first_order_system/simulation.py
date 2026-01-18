import numpy as np
import matplotlib.pyplot as plt

#Time settings
dt = 0.01
t = np.arange(0, 10, dt)

#System parameters
tau = 1.0
setpoint = 1.0

# PID gains
kp = 4.0
ki = 2.0
kd = 0.6

# Storage
y_p = np.zeros_like(t)
y_pi = np.zeros_like(t)
y_pid = np.zeros_like(t)

# PID states
integral_pi = 0
integral_pid = 0
prev_error_pid = 0

# Simulation loop
for i in range(1, len(t)):

    # -----P only--------
    error_p = setpoint - y_p[i-1]
    u_p = kp * error_p
    y_p[i] = y_p[i-1] + (dt * (u_p - y_p[i-1]) / tau)

    # -----PI only--------
    error_pi = setpoint - y_pi[i-1]
    integral_pi += error_pi * dt
    u_pi = (kp * error_pi) + (ki * integral_pi)
    y_pi[i] = y_pi[i-1] + (dt * (u_pi - y_pi[i-1]) / tau)

    # -----PID--------
    error_pid = setpoint - y_pid[i-1]
    integral_pid += error_pid * dt
    derivative = (error_pid - prev_error_pid) / dt
    u_pid = (kp * error_pid) + (ki * integral_pid) + (kd * derivative)
    y_pid[i] = y_pid[i-1] + (dt * (u_pid - y_pid[i-1]) / tau)
    prev_error_pid = error_pid

    #Plot results
plt.plot(t, y_p, label="P")
plt.plot(t, y_pi, label="PI")
plt.plot(t, y_pid, label="PID")
plt.axhline(setpoint, linestyle="--", label="Setpoint")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.show()
