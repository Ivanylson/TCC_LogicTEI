import pygame
import menu
import tabelaVerdade 

# Mostrar tela de informações sobre o jogo
def show_instrucoes(screen,user_name):

    pygame.display.set_caption("Logic T.E.I - Instruções")
    
    # Carrega a imagem de fundo
    background_image = pygame.image.load('./imagens/capa/instrucoes.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))

    menu_font = pygame.font.Font(None, 22)
    back_text = menu_font.render("Pressione ESC para voltar ao menu.", True, (0, 0, 0))
    back_text2 = menu_font.render("Pressione ENTER para começar o jogo.", True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.show_menu(screen,user_name)
                if event.key ==pygame.K_RETURN:
                	is_exit = tabelaVerdade.main(screen, user_name)
                	sys.exit()
                	if is_exit:
                		tabelaVerdade.zero_fases(screen, user_name)
                		tabelaVerdade.main(screen, user_name)


        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo

        back_rect = back_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 200))
        screen.blit(back_text, back_rect)

        back_rect2 = back_text2.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 250))
        screen.blit(back_text2, back_rect2)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
