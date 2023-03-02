import pygame
import random
import math
pygame.init()


class Firework:
    def __init__(self, screen):
        self.screen = screen
        self.x = pygame.mouse.get_pos()[0]
        self.y = self.screen.get_height()
        self.radius = 7
        self.mouse_y_pos = pygame.mouse.get_pos()[1]
        self.mouse_x_pos = pygame.mouse.get_pos()[0]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particles = []
        self.should_explode = False
        self.exploding_sound = pygame.mixer.Sound("sounds/Fireworks exploding sound.mp3")
        self.whistling_sound = pygame.mixer.Sound("sounds/fireworks whitstling sound.mp3")
        self.whistling_sound.play()

    def draw(self, screen):
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 5, 30))

    def explode(self):
        x = self.mouse_x_pos
        y = self.mouse_y_pos
        for i in range(500):
            color = self.color #(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            radius = 5
            particle = [[x, y], color, radius, [random.randint(-10, 11) - 1, random.randint(-10, 11) - 1]] #[random.randint(-20, 20) / 5 - 1, random.randint(-20, 20) / 5 - 1]
            #[random.randint(2 * math.pi * 10, 2 * math.pi * 30), random.randint(2 * math.pi * 10, 2 * math.pi * 30)]
            self.particles.append(particle)
        if x <= 0 or x >= self.screen.get_width() or y <= 0 or y >= self.screen.get_height():
            self.particles.remove(particle)

    def update(self):
        self.draw(self.screen)
        if self.should_explode:
            self.explode()
            self.should_explode = False

        if self.y >= self.mouse_y_pos:
            self.y -= 5

        if math.hypot((self.x - self.mouse_x_pos), (self.y - self.mouse_y_pos))  <= 2:
            self.should_explode = True
            self.whistling_sound.stop()
            self.exploding_sound.play()
            self.x = -10
            self.y = -10
        else:
            self.should_explode = False

        for particle in self.particles:
            pygame.draw.circle(self.screen, particle[1], [int(particle[0][0]), int(particle[0][1])], particle[2])
            particle[0][0] += particle[3][0]
            particle[0][1] += particle[3][1]
            particle[2] -= 0.02

            if particle[2] <= 0:
                self.particles.remove(particle)



