# First-Order System Model

## System Equation

The canonical first-order linear system is defined by:

\[
\tau \dot y + y = u
\]

or equivalently,

\[
\dot y = \frac{1}{\tau}(u - y)
\]

where:
- \( y \) is the system output
- \( u \) is the control input
- \( \tau > 0 \) is the system time constant

---

## Physical Interpretation

This model represents systems with:
- A single energy storage mechanism
- No inertia
- No oscillatory modes

Common physical examples include:
- Thermal systems (temperature dynamics)
- Fluid level tanks
- RC electrical circuits

Energy is stored and dissipated, but never exchanged between multiple storage elements.

As a result, the system response is always monotonic.

---

## State-Space Representation

Define the state variable:

\[
x = y
\]

Then the state equation becomes:

\[
\dot x = \frac{1}{\tau}(u - x)
\]

This system has:
- One state
- One pole
- No internal coupling

This structure fundamentally limits the behaviors the system can exhibit.

---

## Control Implications

### Proportional (P) Control

\[
u = K_p (r - x)
\]

- Increases response speed
- Reduces steady-state error
- Cannot eliminate steady-state error entirely

The closed-loop system remains first-order and cannot overshoot.

---

### Proportional–Integral (PI) Control

\[
u = K_p e + K_i \int e \, dt
\]

- Eliminates steady-state error
- Introduces an additional controller state
- Still does not create oscillatory plant behavior

Overshoot, if observed, is due to controller dynamics rather than plant physics.

---

### Derivative Action

Derivative control is not physically meaningful for a true first-order plant.

Because the system has:
- No inertia
- No oscillatory modes

Derivative action does not improve performance and primarily amplifies noise.

For this reason, PID control is intentionally omitted for first-order systems in this repository.

---

## Discretization and Simulation

All simulations use forward Euler integration of the continuous-time model:

\[
x_{k+1} = x_k + \Delta t \cdot \frac{(u_k - x_k)}{\tau}
\]

This update equation is a direct numerical implementation of the differential equation,
not an abstract algorithm.

---

## Transition to Second-Order Systems

This system contains a single state and cannot exhibit overshoot or oscillations.

To study:
- Inertia
- Damping
- Overshoot
- Energy exchange between states

a second-order model is required. This motivates the transition to mass–damping systems
in the next section of the repository.
