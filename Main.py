import pygame
import sys
from particle import Firework

pygame.init()
screen_dim = (600, 600)
screen = pygame.display.set_mode(screen_dim, pygame.RESIZABLE)
pygame.display.set_caption("Fireworks")
clock = pygame.time.Clock()

particles = []


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(Firework(screen))

    for particle in particles:
        particle.update()
    clock.tick(120)
    pygame.display.update()