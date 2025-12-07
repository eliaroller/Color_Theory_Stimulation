import pygame

import math

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

        self.position = list(position)

        self.radius = radius

        self.color = color

    def self_color(self, color):

        self.color = color

    def move_to(self, pos):

        self.position[0], self.position[1] = pos

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, self.position, self.radius)

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

    visual = application()

    running = True

    mouse_pressed = False

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx, my = pygame.mouse.get_pos()

                lx, ly = visual.light.position

                if(mx - lx) ** 2 + (my - ly) ** 2 <= visual.light.radius ** 2:

                    mouse_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:

                mouse_pressed = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:

                    visual.light.self_color((255, 80, 80))

                elif event.key == pygame.K_w:

                    visual.light.self_color((80, 255, 80))

                elif event.key == pygame.K_e:

                    visual.light.self_color((80, 80, 255))

                elif event.key == pygame.K_r:

                    visual.light.self_color((255, 255, 255))

        if mouse_pressed:

            visual.light.move_to(pygame.mouse.get_pos())

        visual.sphere.update_shading(visual.light.position, visual.light.color)

        visual.screen.fill((30, 30, 30))

        visual.light.draw(visual.screen)

        visual.sphere.draw(visual.screen)

        pygame.display.flip()

        visual.clock.tick(60)

    pygame.quit()

    sys.exit()


if __name__ == "__main__":

    main()
