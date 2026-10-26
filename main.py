import numpy as np
import matplotlib.pyplot as plt

# P, PI, and PID Controller Comparison
# Computer Engineering - Control Systems
# Simulated first-order dynamic system

DT = 0.01
DURATION = 20
SETPOINT = 1.0

# First-order plant parameters
TAU = 2.0
PLANT_GAIN = 1.0


def simulate_controller(kp, ki, kd):
    time = np.arange(0, DURATION + DT, DT)
    output = np.zeros(len(time))
    control = np.zeros(len(time))

    integral = 0.0
    previous_error = SETPOINT

    for i in range(1, len(time)):
        error = SETPOINT - output[i - 1]
        integral += error * DT

        derivative = (error - previous_error) / DT

        u = kp * error + ki * integral + kd * derivative

        # First-order plant differential equation
        dydt = (-output[i - 1] + PLANT_GAIN * u) / TAU

        output[i] = output[i - 1] + dydt * DT
        control[i] = u

        previous_error = error

    return time, output, control


def calculate_metrics(time, output):
    peak = np.max(output)

    overshoot = max(
        0, (peak - SETPOINT) / SETPOINT * 100
    )

    steady_state_error = abs(SETPOINT - output[-1])

    rise_indices = np.where(output >= 0.9 * SETPOINT)[0]
    rise_time = (
        time[rise_indices[0]]
        if len(rise_indices) else float("nan")
    )

    tolerance = 0.02 * SETPOINT
    outside = np.where(
        np.abs(output - SETPOINT) > tolerance
    )[0]

    if len(outside) == 0:
        settling_time = 0.0
    elif outside[-1] == len(time) - 1:
        settling_time = float("nan")
    else:
        settling_time = time[outside[-1] + 1]

    return {
        "Overshoot (%)": overshoot,
        "Rise to 90% (s)": rise_time,
        "Settling Time (s)": settling_time,
        "Steady-State Error": steady_state_error
    }


def main():
    controllers = {
        "P Controller": (2.0, 0.0, 0.0),
        "PI Controller": (2.0, 1.0, 0.0),
        "PID Controller": (3.0, 1.5, 0.2)
    }

    plt.figure(figsize=(12, 7))

    print("CONTROL SYSTEMS SIMULATION")
    print("=" * 45)

    for name, gains in controllers.items():
        time, output, control = simulate_controller(*gains)
        metrics = calculate_metrics(time, output)

        plt.plot(time, output, linewidth=2, label=name)

        print(f"\n{name}")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")

    plt.axhline(
        SETPOINT,
        color="black",
        linestyle="--",
        label="Desired Setpoint"
    )

    plt.title("P, PI, and PID Controller Comparison")
    plt.xlabel("Time (seconds)")
    plt.ylabel("System Output")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("pid_response.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
