
# Solar System Visualization

Solar System Visualization is a Python-based application that simulates a simple solar system model using OpenGL and GLFW. This program visualizes the orbits and movements of planets around the sun, including an asteroid belt.

## Features

- Simulates the sun and eight planets with accurate relative orbital speeds.
- Displays each planet in a distinct color.
- Draws circular orbits for each planet.
- Includes an asteroid belt between Mars and Jupiter.
- Uses OpenGL for rendering and GLFW for window management.

## Requirements

- Python 3.x
- OpenGL
- GLFW

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/solar-system-visualization.git
    cd solar-system-visualization
    ```

2. Install the required Python packages:
    ```bash
    pip install PyOpenGL glfw
    ```

## Usage

1. Run the application:
    ```bash
    python solar_system.py
    ```

2. The application will open a window displaying the solar system model. Resize the window to see the visualization adjust accordingly.

## Description

- The `resize_callback` function adjusts the viewport and orthographic projection when the window is resized.
- The `draw_circle` function draws a filled circle representing a planet or the sun.
- The `draw_orbit` function draws a circular orbit for a planet.
- In the `main` function, the program sets up the window, initializes OpenGL settings, and enters the main rendering loop.
- Planet positions and angles are updated in each iteration of the loop to simulate orbiting.

## Code Details

### Solar System Parameters

- The sun is drawn at the center with a fixed radius.
- Each planet's distance from the sun, size, and orbital speed are defined relative to the sun.
- The asteroid belt is created with randomly placed dots between the orbits of Mars and Jupiter.

### Main Loop

- The main loop handles rendering, including clearing the screen, drawing the sun, drawing orbits, calculating and drawing planet positions, and swapping buffers.
- Planet positions are updated based on their respective orbital speeds.

