import pygame

# Mostrar introdução com letras aparecendo gradualmente e texto no rodapé
def show_intro(screen):

        # Carrega a imagem de fundo
    background_image = pygame.image.load('./imagens/capa/capa.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))

    intro_font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 24)
    title = "Logic T.E.I"
    subtitle = "Tecnologia Educacional Interativa"
    footer_line1 = "Desenvolvido por Ivanylson HG"
    footer_line2 = "Projeto de TCC"

    title_text = ""
    subtitle_text = ""
    footer_text1 = ""
    footer_text2 = ""

    for letter in title:
        title_text += letter
        screen.fill((0, 0, 0))
        title_render = intro_font.render(title_text, True, (0, 0, 0))  # Renderiza o texto em preto
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        screen.blit(title_render, (screen.get_width() / 2 - title_render.get_width() / 2, 250))
        pygame.display.flip()
        pygame.time.delay(100)
    
    pygame.time.delay(1000)
    
    for letter in subtitle:
        subtitle_text += letter
        screen.fill((0, 0, 0))
        title_render = intro_font.render(title_text, True, (0, 0, 0))  # Renderiza o texto em preto
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        subtitle_render = intro_font.render(subtitle_text, True, (0, 0, 0))
        screen.blit(title_render, (screen.get_width() / 2 - title_render.get_width() / 2, 250))
        screen.blit(subtitle_render, (screen.get_width() / 2 - subtitle_render.get_width() / 2, 300))
        pygame.display.flip()
        pygame.time.delay(100)
    
    pygame.time.delay(2000)

    for letter in footer_line1:
        footer_text1 += letter
        screen.fill((0, 0, 0))
        title_render = intro_font.render(title_text, True, (0, 0, 0))  # Renderiza o texto em preto
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        subtitle_render = intro_font.render(subtitle_text, True, (0, 0, 0))
        footer_render1 = intro_font.render(footer_text1, True, (0, 0, 0))
        screen.blit(title_render, (screen.get_width() / 2 - title_render.get_width() / 2, 250))
        screen.blit(subtitle_render, (screen.get_width() / 2 - subtitle_render.get_width() / 2, 300))
        screen.blit(footer_render1, (screen.get_width() / 2 - footer_render1.get_width() / 2, screen.get_height() - 60))
        pygame.display.flip()
        pygame.time.delay(100)

    pygame.time.delay(500)

    for letter in footer_line2:
        footer_text2 += letter
        screen.fill((0, 0, 0))
        title_render = intro_font.render(title_text, True, (0, 0, 0))  # Renderiza o texto em preto
        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        subtitle_render = intro_font.render(subtitle_text, True, (0, 0, 0))
        footer_render1 = intro_font.render(footer_text1, True, (0, 0, 0))
        footer_render2 = intro_font.render(footer_text2, True, (0, 0, 0))
        screen.blit(title_render, (screen.get_width() / 2 - title_render.get_width() / 2, 250))
        screen.blit(subtitle_render, (screen.get_width() / 2 - subtitle_render.get_width() / 2, 300))
        screen.blit(footer_render1, (screen.get_width() / 2 - footer_render1.get_width() / 2, screen.get_height() - 100))
        screen.blit(footer_render2, (screen.get_width() / 2 - footer_render2.get_width() / 2, screen.get_height() - 60))
        pygame.display.flip()
        pygame.time.delay(100)

    pygame.time.delay(2000)
