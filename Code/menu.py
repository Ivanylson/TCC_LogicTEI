import pygame
import sys
import os
import sobre  # Importe o módulo sobre
import tabelaVerdade  # Importe o módulo sobre
import escolhaDificuldade
import classificacoes
import instrucoes

# Mostrar menu
def show_menu(screen, user_name):
    menu_font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 29)
    menu_options = ["INICIAR", "INSTRUÇÕES","ESCOLHER A DIFICULDADE" ,"CLASSIFICAÇÕES", "SOBRE", "SAIR"]
    selected_option = 0

    pygame.display.set_caption("Logic - T.E.I - Menu")

    background_image = pygame.image.load('./imagens/capa/capaMenu.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                      is_exit = instrucoes.show_instrucoes(screen, user_name)
                      sys.exit()
                      if is_exit:
                        instrucoes.show_instrucoes(screen, user_name)
                        tabelaVerdade.zero_fases(screen, user_name)
                        tabelaVerdade.main(screen, user_name)
                        
                    elif selected_option == 1:
                         instrucoes.show_instrucoes(screen, user_name)
                    elif selected_option == 2:
                        escolhaDificuldade.show_escolhaDificuldade(screen, user_name)
                    elif selected_option == 3:
                        classificacoes.show_classificacoes(screen, user_name)
                        sys.exit()
                    elif selected_option == 4:
                       sobre.show_sobre(screen, user_name)  # Mostrar informações sobre o jogo
                    elif selected_option == 5:
                        nome_arquivo = './classificacao.txt'
                        if os.path.exists(nome_arquivo):
                            os.remove(nome_arquivo)
                        sys.exit()
                        sys.exit()

        screen.fill((255, 255, 255))
        
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo

        for i, option in enumerate(menu_options):
            color = (0, 0, 0) if i == selected_option else (128, 128, 128)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen.get_width() / 2, 200 + i * 50))
            screen.blit(text, text_rect)

        # Exiba o nome do usuário
        user_font = pygame.font.Font('./fontes/DalekPinpointBold.ttf',24)
        user_text = user_font.render(f"Jogador(a): {user_name}", True, (0, 0, 0))
        user_rect = user_text.get_rect(topleft=(20, 20))
        screen.blit(user_text, user_rect)

        pygame.display.flip()