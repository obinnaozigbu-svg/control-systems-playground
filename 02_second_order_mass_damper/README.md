# Second-order mass–damper system

This experiment studies a simple inertial system modeled as a mass with viscous
damping, controlled using classical feedback controllers.

## Plant model

The system is described by the equation:

m y¨ + b y˙ = u

where:
- y is position
- u is the applied control force
- m is the mass
- b is the damping coefficient

The model assumes:
- linear viscous damping
- no stiffness (no spring)
- no external disturbances (gravity added later)

## State-space representation

To enable time-domain simulation, the system is rewritten in first-order form:

x1 = y  
x2 = y˙  

x˙1 = x2  
x˙2 = (u - b x2) / m

## Control objective

The goal is to regulate the position y to a constant reference using:
- P control
- PD control
- PID control

The effect of inertia and damping on overshoot, settling time, and stability
will be examined.
