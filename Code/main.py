import pygame
import intro
import intro2
import menu


# Inicialização do Pygame
pygame.init()

# Configurações de tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Logic T.E.I")

# Loop principal
def main():
    intro.show_intro(screen)
    res = intro2.show_intro2(screen)  # Mostra a segunda introdução
    menu.show_menu(screen, res)
    pygame.quit()
    pygame.exit()

if __name__ == "__main__":
    main()