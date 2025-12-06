import pygame

import sys

class application:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))

        pygame.display.set_caption("Color Theory Visualizer")

        self.clock = pygame.time.Clock()

        self.light = lightbulb((150, 200), 40)

        self.sphere = ball((350, 200), 60)

class lightbulb:

    def __init__(self, position, radius, color = (255, 255, 255)):

        self.position = position

        self.radius = radius

        self.color = color

    def self_color(self, color):

        self.color = color

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, self.position, self.radius)

class ball:

    def __init__(self, position, radius, base_color = (150, 150, 150)):

        self.position = position

        self.radius = radius

        self.base_color = base_color

        self.shaded_color = base_color

    def light_applied(self, light_color):

        r = min(255, self.base_color[0] * light_color[0] // 255)

        g = min(255, self.base_color[1] * light_color[1] // 255)

        b = min(255, self.base_color[2] * light_color[2] // 255)

        self.shaded_color = (r, g, b)

    def draw(self, screen):

        pygame.draw.circle(screen, self.shaded_color, self.position, self.radius)




def main():

    visual = application()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    visual.light.self_color((255, 80, 80))

                elif event.key == pygame.K_g:

                    visual.light.self_color((80, 255, 80))

                elif event.key == pygame.K_b:

                    visual.light.self_color((80, 80, 255))

                elif event.key == pygame.K_w:

                    visual.light.self_color((255, 255, 255))

        visual.sphere.light_applied(visual.light.color)

        visual.screen.fill((30, 30, 30))

        visual.light.draw(visual.screen)

        visual.sphere.draw(visual.screen)

        pygame.display.flip()

        visual.clock.tick(60)

    pygame.quit()

    sys.exit()


if __name__ == "__main__":

    main()
