from utils import *
import pygame
pygame.init()

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('O Quadrado Heitor')
icon = pygame.Surface((64, 64))
icon.fill(RED)
pygame.display.set_icon(icon)

game_screen = pygame.image.load('assets/game.jpg')
heitor = Heitor(WINDOW_WIDTH - 100, 200, RED)

clock = pygame.time.Clock()

state = {
    "game": True,
    "win_screen": False
}


def draw(win):
    global state
    if state['game']:
        game.draw(win, game_screen, heitor)
    if state['win_screen']:
        win_screen.draw(win, game_screen, heitor)

def main():
    global state
    while True:
        clock.tick(FPS)
        pygame.display.update()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                state['win_screen'] = True
                state['game'] = False
            
            if state['game']:
                game.events(event)
            elif state['win_screen']:
                win_screen.events(event)
        

        # Updates
        if state['game']:
            state['win_screen'] = game.update(heitor)
            state['game'] = not state['win_screen']
        elif state['win_screen']:
            state['game'] = win_screen.update()
            if state['game'] == True:
                state['win_screen'] = False
                heitor.reset()
                game.reset()
                win_screen.reset() 
        
        draw(DISPLAY)


if __name__ == '__main__':
    main()
