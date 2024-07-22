# Mass Spring Damper Simulation

This repository contains a Python simulation for a Mass-Spring-Damper system, originally inspired by MatLab simulations popular at Ohio State University during my Control System Engineering studies. The simulation solves the system's equations of motion and plots the system's response to both impulse and steady-state inputs.

![System Preview](preview.png)

## Background
The simulation is based on the transfer function obtained from the Laplace transform of the system's differential equation. This approach assumes the system is linear and time-invariant. While most physical systems exhibit non-linear behaviors like varying friction, the simulation provides accurate results within typical operating conditions. These simplifications make transfer function analysis a valuable tool for preliminary system behavior predictions.

## Transfer Function Assumptions
- **Linearity**: The system must be linear, meaning its response at any instant depends only on its current state, not its history.
- **Time Invariance**: The system's characteristics do not change over time.

Understanding the foundational assumptions of the Laplace transform is crucial for applying it correctly in practical scenarios. [Learn more about these assumptions.](https://example.com/laplace_assumptions)

## Simulation Preview
<div align="center">
  <img src="docs/preview.gif" width="800">
</div>

## Connect with Me

Feel free to follow my social media for updates and more projects:

<div align="center">
  <a href="https://twitter.com/BrianJosephLeko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-white/twitter-logo-white.svg" width="30" alt="Twitter Logo"></a> &#8195;
  <a href="https://github.com/BrianLesko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-white/github-mark-white.svg" width="30" alt="GitHub"></a> &#8195;
  <a href="https://www.linkedin.com/in/brianlesko/"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-white/linkedin-icon-white.svg" width="30" alt="LinkedIn"></a>
</div>

Thank you for visiting, and enjoy simulating!

