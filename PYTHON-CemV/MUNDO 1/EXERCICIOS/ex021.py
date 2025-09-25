#Faça um progama em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('Faixa20.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''Faixa20.mp3'''
