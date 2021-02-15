import pygame
import Settings

pygame.init()


screen = pygame.display.set_mode((Settings.Window_settings[0], Settings.Window_settings[1]))
pygame.display.set_caption(Settings.Window_settings[2])

running = True

game_objects = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in game_objects:
        if obj:
            obj.update()
    pygame.display.update()


