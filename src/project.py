# Pseudocode:

# Define 3 classes, An application class that defines the other 2 classes named lightbulb and ball.
# Make an event to use keyboard command keys to change lightbulb colors.
# Set the resolution for both the windowed and full screen display window.
# Utilize a conditional statement to move the position of the lightbulb to the position of the mouse cursor if the left mouse button is pressed.
# Calculate the sise of a highlight and set it to a white color so it dynamically follows the position of the lightbulb.
# Draw both the lightbulb and ball shapes on the window display.
# Flip the display screen to showcase the final output.

import pygame

import math

import sys

class application:

    def __init__(self):

        pygame.init()

        self.is_fullscreen = False

        self.windowed_size = (600, 400)  # Defines the resolution of the program window display.

        self.screen = pygame.display.set_mode(self.windowed_size)  # Sets the window output resolution to the windowed_size value.

        pygame.display.set_caption("Color Theory Visualizer")  # Sets the title of the window display.

        self.clock = pygame.time.Clock()

        self.light = lightbulb((150, 200), 40)    # Creates a size for the lightbulb class.

        self.sphere = ball((350, 200), 60)        # Creates a size for the ball class.

    def fullscreen_toggle(self):     # Controls the full screen transition functionality.

        if self.is_fullscreen:

            self.screen = pygame.display.set_mode(self.windowed_size)

            self.is_fullscreen = False

        else:

            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

            self.is_fullscreen = True

class lightbulb:

    def __init__(self, position, radius, color = (255, 255, 255)):

        self.position = list(position)

        self.radius = radius

        self.color = color

        self.light_on = True

        self.dragging = False

        self.cord_start = (position[0], 50)

    def self_color(self, color):

        self.color = color

    def move_to(self, pos):

        self.position[0], self.position[1] = pos

    def cord_event(self, event):     # Controls the movement of the lightbulb cord.

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            bx, by = self.position

            if (mx - bx) ** 2 + (my - by) ** 2 <= self.radius ** 2:

                self.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:

            self.dragging = False

            if self.position[1] < 50:

                self.light_on = not self.light_on

                self.position[1] = 100

        elif event.type == pygame.MOUSEMOTION and self.dragging:

            mx, my = pygame.mouse.get_pos()

            self.move_to((mx, my))

    def draw(self, screen):   # Draws the cord line on the window display screen.

        pygame.draw.line(screen, (100, 100, 100), self.cord_start, self.position, 4)

        bulb_color = self.color if self.light_on else (50, 50, 50)

        pygame.draw.circle(screen, bulb_color, self.position, self.radius)



class ball:

    def __init__(self, position, radius, base_color = (150, 150, 150)):

        self.position = position

        self.radius = radius

        self.base_color = base_color

        self.light_surface = pygame.Surface((radius * 7, radius * 7), pygame.SRCALPHA)

    def update_shading(self, light_position, light_color):

        self.light_surface.fill((0, 0, 0, 0))

        sx, sy = self.position

        lx, ly = light_position

        dx = lx - sx

        dy = ly - sy

        angle = math.atan2(dy, dx)

        for n in range(self.radius):

            falling = 1 - (n / self.radius)

            falling = max(0, falling)


            offset_x = int(math.cos(angle) * (self.radius - n) * 0.3)

            offset_y = int(math.sin(angle) * (self.radius - n) * 0.3)

            color = (int(light_color[0] * falling), int(light_color[1] * falling), int(light_color[2] * falling), int(180 * falling))

            pygame.draw.circle(self.light_surface, color, (self.radius + offset_x, self.radius + offset_y), self.radius - n)

        highlight_radius = self.radius // 4

        highlight_offset_x = int(math.cos(angle) * self.radius * 0.6)

        highlight_offset_y = int(math.sin(angle) * self.radius * 0.6)

        pygame.draw.circle(self.light_surface, (255, 255, 255, 200), (self.radius + highlight_offset_x, self.radius + highlight_offset_y), highlight_radius)

        

    def draw(self, screen):

        screen.blit(self.light_surface, (self.position[0] - self.radius, self.position[1] - self.radius))




def main():

    visual = application()    # Stores the called application class in a variable named visual

    running = True

    mouse_pressed = False

    while running:                               # runs the program on a display

        for event in pygame.event.get():           # allows the user to exit the opened program window when executed.

            if event.type == pygame.QUIT:         # Closes the program by pressing the x button.

                running = False

            visual.light.cord_event(event)        # Calls the class event that draws and manipulates the lightbulb cord.

            if event.type == pygame.MOUSEBUTTONDOWN:     # if the left mouse button is pressed

                mx, my = pygame.mouse.get_pos()          # Gets the position of the mouse cursor

                lx, ly = visual.light.position           # Gets the position of the lightbulb shape

                if(mx - lx) ** 2 + (my - ly) ** 2 <= visual.light.radius ** 2:     # Checks to see if the mouse cursor is on the lightbulb shape.

                    mouse_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:       # The above action stops once the left mouse button is no longer pressed.

                mouse_pressed = False

            if event.type == pygame.KEYDOWN:          # The list of keyboard commands.

                if event.key == pygame.K_q:           # When the q keyboard key is pressed, the lightbulb and ball colors change to Red.

                    visual.light.self_color((255, 80, 80))

                elif event.key == pygame.K_w:          # When the w keyboard key is pressed, the lightbulb and ball colors change to Green.

                    visual.light.self_color((80, 255, 80))

                elif event.key == pygame.K_e:          # When the e keyboard key is pressed, the lightbulb and ball colors change to Blue.

                    visual.light.self_color((80, 80, 255))

                elif event.key == pygame.K_r:           # When the r keyboard key is pressed, the lightbulb and ball colors change to White.

                    visual.light.self_color((255, 255, 255))

                elif event.key == pygame.K_f:           # When the f keyboard key is pressed, the display screen transitions to full screen.

                    visual.fullscreen_toggle()

        if mouse_pressed:

            visual.light.move_to(pygame.mouse.get_pos())     # moves the position of the lightbulb shape to the position of the mouse cursor when the left mouse button is pressed.

        if visual.light.light_on:

           visual.sphere.update_shading(visual.light.position, visual.light.color)   # dynamically changes the light and shadow presented on the ball shape.

        else:

            visual.sphere.update_shading(visual.light.position, (0, 0, 0))

        visual.screen.fill((30, 30, 30))   # Fills the background of the display screen with black.

        visual.light.draw(visual.screen)   # Draws the lightbulb shape on the display screen.

        visual.sphere.draw(visual.screen)   # Draws the ball shape on the display screen.

        pygame.display.flip()               # Flips the screen to display the display output instead of the background layer.

        visual.clock.tick(60)               # Gives a delay.

    pygame.quit()             # Quits the program

    sys.exit()                # exits the system


if __name__ == "__main__":

    main()
