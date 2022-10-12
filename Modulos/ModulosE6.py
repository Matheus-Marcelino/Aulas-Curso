import pygame

pygame.init()
pygame.mixer.music.load('Música de elevador.mp3')
pygame.mixer.music.play()
pygame.event.wait()
