# PID Control Systems Simulator

### Feedback Control Analysis | P, PI & PID Controllers
### CPE - Marian University


## Project Overview

This project explores feedback control systems through a Python-based simulation of proportional (P), proportional-integral (PI), and proportional-integral-derivative (PID) controllers.

Inspired by my Control Systems coursework, this simulation investigates how controller gains influence system response, including rise time, overshoot, settling time, and steady-state error.

The objective is to connect mathematical modeling and control theory with practical software-based engineering analysis.

## Mathematical Model

The simulation uses a simplified first-order plant:

\[
\tau\frac{dy(t)}{dt}+y(t)=Ku(t)
\]

Where:

- \(\tau=2\) seconds is the plant time constant.
- \(K=1\) is the plant gain.
- \(u(t)\) is the control input.
- \(y(t)\) is the system output.

The PID control law is:

\[
u(t)=K_pe(t)+K_i\int e(t)\,dt+K_d\frac{de(t)}{dt}
\]

## Controller Configurations

| Controller | Kp | Ki | Kd |
|---|---:|---:|---:|
| P | 2.0 | 0.0 | 0.0 |
| PI | 2.0 | 1.0 | 0.0 |
| PID | 3.0 | 1.5 | 0.2 |

## Technologies

- Python
- NumPy
- Matplotlib
- Numerical Integration
- Feedback Control Theory

## Simulation Results

The program compares the three controllers using a unit-step reference input.

![P, PI, and PID Step Response](pid_response.png)

The simulation calculates:

- Percentage overshoot
- Time to reach 90% of the setpoint
- Settling time within a 2% tolerance
- Steady-state error estimated at the end of the simulation

## Engineering Analysis

The proportional controller responds to the reference input but generally retains steady-state error for the modeled plant.

Adding integral control allows the controller to eliminate steady-state error under suitable stable operating conditions.

Derivative control responds to changes in error and can improve transient performance when appropriately tuned. Its effects depend on the selected gains and plant dynamics.

The purpose of comparing these configurations is to evaluate the tradeoffs between response speed, accuracy, and stability.

## Running the Project

Install the required Python libraries:

`pip install -r requirements.txt`

Execute the simulation:

`python main.py`

The program generates a step-response plot and saves it as `pid_response.png`.

## Development Roadmap

- [x] Implement P, PI, and PID controllers
- [x] Model first-order plant dynamics
- [x] Calculate response performance metrics
- [x] Generate step-response visualizations
- [ ] Experiment with additional controller gains
- [ ] Model second-order dynamic systems
- [ ] Investigate disturbance rejection
- [ ] Explore physical hardware integration

## Limitations

This is an educational simulation based on a simplified first-order model. It does not include actuator saturation, sensor noise, or experimental hardware validation.

The reported steady-state error is an estimate at the simulation's final time rather than a proof of asymptotic behavior.
