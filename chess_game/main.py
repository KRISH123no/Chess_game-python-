import pygame, sys
from settings import Settings
from menu import Menu
from game import GameController
from ui import UI

def main():
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.WINDOW_WIDTH, s.WINDOW_HEIGHT), pygame.RESIZABLE)
    clock, ui, menu = pygame.time.Clock(), UI(screen, s), Menu(screen, s, None)
    menu.ui = ui
    ctrl, state, run = None, 'MENU', True

    while run:
        pygame.event.pump()
        evs = pygame.event.get()
        for e in evs:
            if e.type == pygame.QUIT: run = False
            if e.type == pygame.VIDEORESIZE: screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: state = 'MENU'

        menu.draw_wood_bg()
        if state == 'MENU':
            sel = menu.update(evs)
            if sel == 'VS_AI': state = 'DIFF'
            elif sel == 'VS_FRIEND': ctrl, state = GameController(screen, s, ui, 'FRIEND'), 'PLAY'
            menu.draw_main_menu()
        elif state == 'DIFF':
            d = menu.update_difficulty(evs)
            if d == 'BACK': state = 'MENU'
            elif d: ctrl, state = GameController(screen, s, ui, 'AI', d), 'PLAY'
            menu.draw_difficulty_menu()
        elif state == 'PLAY' and ctrl:
            ctrl.update(evs)
            ctrl.draw(*screen.get_size())
            if ctrl.game_over:
                for e in evs:
                    if e.type == pygame.MOUSEBUTTONDOWN and ui.go_back_btn.collidepoint(e.pos): state = 'MENU'

        pygame.display.flip()
        clock.tick(60)

    if ctrl: ctrl.cleanup()
    pygame.quit()

if __name__ == "__main__": main()