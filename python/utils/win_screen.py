import pygame
from . import *

cont = 0

play_again_button = Button(0, 0, "Jogar de novo?", 60)
play_again_button.set_center(WINDOW_RECT.center[0], WINDOW_HEIGHT - 200)
play_again = False

def draw(win, game, heitor):
    win.blit(game, (0, 0))

    heitor.draw(win)

    # Escurece a tela (1.0s)
    surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    alpha = 150 * (cont / FPS) if cont <= 60 else 150
    surf.fill((0, 0, 0, alpha))
    win.blit(surf, (0, 0))
    if cont > FPS:  # Primeiro texto (1.0s)
        variation = (cont - FPS) / (FPS) if cont <= FPS*2 else 1
        surf = font.render("Parabéns!", True, WHITE)
        rect = surf.get_rect()
        rect.center = (WINDOW_RECT.center[0], WINDOW_HEIGHT + 200 - 700*variation)
        win.blit(surf, rect)
    if cont > FPS*2:  # Segundo texto (1.0s)
        variation = (cont - FPS*2) / (FPS) if cont <= FPS*3 else 1
        surf = font.render("Você salvou o danneto!", True, WHITE)
        rect = surf.get_rect()
        rect.center = (WINDOW_RECT.center[0], WINDOW_HEIGHT + 200 - 620*variation)
        win.blit(surf, rect)
    if cont > FPS*4:
        play_again_button.draw(win)

def events(event):
    global play_again
    if cont > FPS*4:
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if play_again_button.is_inside(x, y):
                    play_again_button.press()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if play_again_button.is_inside(x, y):
                    if play_again_button.is_pressed():
                        play_again = True
                play_again_button.release()        

def update():
    global cont
    cont += 1

    return play_again
    
def reset():
    global play_again, cont
    play_again = False
    cont = 0