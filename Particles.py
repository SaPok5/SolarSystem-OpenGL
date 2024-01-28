
import math
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw

# Callback function for window resize
def resize_callback(window, width, height):
    glViewport(0, 0, width, height)
    glOrtho(0, width, height, 0, -1, 1)

def draw_circle(x, y, radius, color, has_ring=False):
    num_segments = 100
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        theta = (2.0 * math.pi * i) / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

    if has_ring:
        # Draw a thin ring around the planet
        ring_radius = radius + 3  # You can adjust the ring size
        glBegin(GL_LINE_LOOP)
        glColor3f(0.8, 0.8, 0.8)  # Ring color
        for i in range(num_segments + 1):
            theta = (2.0 * math.pi * i) / num_segments
            dx = ring_radius * math.cos(theta)
            dy = ring_radius * math.sin(theta)
            glVertex2f(x + dx, y + dy)
        glEnd()

def draw_orbit(center_x, center_y, radius):
    num_segments = 100
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 1, 1)  # White color for orbits
    for i in range(num_segments):
        theta = (2.0 * math.pi * i) / num_segments
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return

    # Set up the window
    width, height = 1200, 800
    window = glfw.create_window(width, height, "Solar System", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, resize_callback)

    glViewport(0, 0, width, height)
    glOrtho(0, width, height, 0, -1, 1)

    # Set clear color
    glClearColor(0, 0, 0, 0)

    # Planet and orbit parameters
    sun_radius = 30
    planet_radius = 10
    planet_radius1 = 13

    sun_x, sun_y = width // 2, height // 2

    # Define distances from the center of the screen for better visibility
    mercury_distance = 50
    venus_distance = 100
    earth_distance = 150
    mars_distance = 200
    jupiter_distance = 250
    saturn_distance = 300
    uranus_distance = 350
    neptune_distance = 400

    # Slowed orbit speeds for better visibility
    mercury_speed = -math.radians(1 / (88 * 0.5))
    venus_speed = -math.radians(2 / (225 * 0.5))
    earth_speed = -math.radians(3 / (365 * 0.5))
    mars_speed = -math.radians(4 / (687 * 0.5))
    jupiter_speed = -math.radians(5 / (11.86 * 365 * 0.25))
    saturn_speed = -math.radians(6 / (29.46 * 365 * 0.25))
    neptune_speed = -math.radians(7 / (164.8 * 365 * 0.25))
    uranus_speed = -math.radians(8 / (84 * 365 * 0.25))

    # Initial angles for planet positions
    mercury_angle = 0
    venus_angle = 0
    earth_angle = 0
    mars_angle = 0
    jupiter_angle = 0
    saturn_angle = 0
    neptune_angle = 0
    uranus_angle = 0

    asteroid_belt_dots = []
    for _ in range(500):  # Number of asteroids
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(mars_distance, jupiter_distance)
        x = sun_x + int(math.cos(angle) * distance)
        y = sun_y + int(math.sin(angle) * distance)
        asteroid_belt_dots.append((x, y))

    running = True
    while running and not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the sun at the center and name it
        draw_circle(sun_x, sun_y, sun_radius, (1, 1, 0))  # Yellow color for the sun

        # Draw orbits
        for distance in [mercury_distance, venus_distance, earth_distance, mars_distance,
                         jupiter_distance, saturn_distance, neptune_distance, uranus_distance]:
            draw_orbit(sun_x, sun_y, distance)

        # Calculate and draw positions of planets 
        mercury_x = sun_x + int(math.cos(mercury_angle) * mercury_distance)
        mercury_y = sun_y + int(math.sin(mercury_angle) * mercury_distance)
        draw_circle(mercury_x, mercury_y, planet_radius, (0.5, 0.5, 0.5))  # Mercury color

        venus_x = sun_x + int(math.cos(venus_angle) * venus_distance)
        venus_y = sun_y + int(math.sin(venus_angle) * venus_distance)
        draw_circle(venus_x, venus_y, planet_radius, (0.9, 0.7, 0.1))  # Venus color

        earth_x = sun_x + int(math.cos(earth_angle) * earth_distance)
        earth_y = sun_y + int(math.sin(earth_angle) * earth_distance)
        draw_circle(earth_x, earth_y, planet_radius, (0, 0, 1))  # Earth color

        mars_x = sun_x + int(math.cos(mars_angle) * mars_distance)
        mars_y = sun_y + int(math.sin(mars_angle) * mars_distance)
        draw_circle(mars_x, mars_y, planet_radius, (1, 0, 0))  # Mars color

        jupiter_x = sun_x + int(math.cos(jupiter_angle) * jupiter_distance)
        jupiter_y = sun_y + int(math.sin(jupiter_angle) * jupiter_distance)
        draw_circle(jupiter_x, jupiter_y, planet_radius1, (0.8, 0.6, 0.1))  # Jupiter color

        saturn_x = sun_x + int(math.cos(saturn_angle) * saturn_distance)
        saturn_y = sun_y + int(math.sin(saturn_angle) * saturn_distance)
        draw_circle(saturn_x, saturn_y, planet_radius1, (0.5, 0.4, 0.2), has_ring=True)  # Saturn color with ring

        neptune_x = sun_x + int(math.cos(neptune_angle) * neptune_distance)
        neptune_y = sun_y + int(math.sin(neptune_angle) * neptune_distance)
        draw_circle(neptune_x, neptune_y, planet_radius1, (0.4, 0.6, 0.9))  # Neptune color

        uranus_x = sun_x + int(math.cos(uranus_angle) * uranus_distance)
        uranus_y = sun_y + int(math.sin(uranus_angle) * uranus_distance)
        draw_circle(uranus_x, uranus_y, planet_radius1, (0.5, 0.8, 0.5))  # Uranus color

        # Update angles for planet positions
        mercury_angle += mercury_speed
        venus_angle += venus_speed
        earth_angle += earth_speed
        mars_angle += mars_speed
        jupiter_angle += jupiter_speed
        saturn_angle += saturn_speed
        neptune_angle += neptune_speed
        uranus_angle += uranus_speed

        # Draw asteroid belt dots
        glBegin(GL_POINTS)
        glColor3f(0.8, 0.8, 0.8)  # Asteroid color
        for dot in asteroid_belt_dots:
            glVertex2f(dot[0], dot[1])
        glEnd()

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
