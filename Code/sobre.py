import pygame
import menu

# Mostrar tela de informações sobre o jogo
def show_sobre(screen,user_name):

    pygame.display.set_caption("Logic T.E.I - Sobre")
    
    # Carrega a imagem de fundo
    background_image = pygame.image.load('./imagens/capa/capa.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))

    menu_font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 22)
    text = menu_font.render("Este jogo foi feito pelo Ivanylson Honorio Gonçalves.", True, (0, 0, 0))
    text2 = menu_font.render("TCC de S.I - UFJF", True, (0, 0, 0))
    text3 = menu_font.render("Orientador pela Profa. Regina Maciel Braga", True, (0, 0, 0))
    back_text = menu_font.render("Pressione ESC para voltar ao menu.", True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.show_menu(screen,user_name)

        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(text, text_rect)

        text_rect2 = text2.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 12))
        screen.blit(text2, text_rect2)


        text_rect3 = text3.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 60))
        screen.blit(text3, text_rect3)

        back_rect = back_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(back_text, back_rect)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
