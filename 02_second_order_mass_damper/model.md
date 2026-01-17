# System model: mass–damper

## Governing equation

The plant is modeled as a point mass with viscous damping:

m y¨ + b y˙ = u

where:
- y is position
- y˙ is velocity
- y¨ is acceleration
- u is the applied control force
- m is the mass
- b is the damping coefficient

## Assumptions

- The system is linear
- Damping is proportional to velocity
- No stiffness (no spring term)
- No external disturbances (gravity neglected)

## State definition

The system is rewritten in first-order form by defining the states:

x1 = y  
x2 = y˙  

## State equations

Taking time derivatives:

x˙1 = x2  

From the governing equation:

y¨ = (u - b y˙) / m

Substituting y˙ = x2:

x˙2 = (u - b x2) / m

## State-space form

The final state-space representation is:

x˙1 = x2  
x˙2 = (u - b x2) / m
