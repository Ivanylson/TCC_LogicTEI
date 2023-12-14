import pygame
import sys
import menu

def show_intro2(screen):
    # Cores
    black = (0, 0, 0)
    white = (255, 255, 255)

         # Carrega a imagem de fundo
    background_image = pygame.image.load('./imagens/intro/intro.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))


    # Texto da introdução
    intro_text = [
        "Bem vindo ao Logic .T.E.I",
    ]

    intro_font = pygame.font.Font(None, 24)

    def display_intro_text(text_lines):
        for line in text_lines:
            current_text = ""
            for letter in line:
                current_text += letter
                screen.fill(white)
                intro_render = intro_font.render(current_text, True, black)
                screen.blit(intro_render, (screen.get_width() / 2 - intro_render.get_width() / 2, 50))
                pygame.display.flip()
                pygame.time.delay(50)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        return

    def get_user_name():
        user_name = ""
        input_active = True
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode

            screen.fill(white)
            intro_render = intro_font.render(intro_text[0], True, black)
            screen.blit(background_image, (0, 0))
            screen.blit(intro_render, (screen.get_width() / 2 - intro_render.get_width() / 2, 50))
            input_text = intro_font.render(f"Digite seu nome: {user_name}", True, black)
            screen.blit(input_text, (screen.get_width() / 2 - input_text.get_width() / 2, 500))
            pygame.display.flip()

        return user_name

    display_intro_text(intro_text)
    user_name = get_user_name()
    return user_name
    menu.userName(user_name)