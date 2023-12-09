import pygame
import sys
import random
import menu
import inferenciaLogica

# Inicialização do Pygame
#pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
#window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Lógica Proposicional")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte
#font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 18)


global classificacao

def classification(classificacao):
    return classificacao

# Dimensões do botão
button_width = 120
button_height = 40
button_x = WIDTH - button_width - 20  # Correção aqui
button_y = HEIGHT - button_height - 20

# Dicas para cada fase
dicas = [
    "Dica da Fase 1: Lembre-se AND,OR, NOT",
    "Dica da Fase 2: Menos 1pt, HAHA",
    "Dica da Fase 3: Lembre-se AND,OR, NOT",
    "Dica da Fase 4: Menos 1pt, HAHA",
    "Dica da Fase 5: Menos 1pt, HAHA",
    "Dica da Fase 6: Lembre-se AND,OR, NOT",
    "Dica da Fase 7: Lembre-se AND,OR, NOT",
    "Dica da Fase 8: Menos 1pt, HAHA",
    "Dica da Fase 9: Lembre-se AND,OR, NOT",
    "Dica da Fase 10: Menos 1pt, HAHA"
]


# Perguntas e respostas
questions = [
    {
        "question_image": "./questoesLP/q1.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesLP/q2.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesLP/q3.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesLP/q4.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesLP/q5.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "D"
    },
	{
        "question_image": "./questoesLP/q6.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "C"
    },
	{
        "question_image": "./questoesLP/q7.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "C"
    },
	{
        "question_image": "./questoesLP/q8.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesLP/q9.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesLP/q10.png",
        "options": ["Letra A", "Letra B", "Letra C", "Letra D", "Letra E"],
        "correct_answer": "A"
    }

]

# Variáveis do jogo
score = 3
question_index = 0

# Função para exibir uma pergunta na tela, incluindo a imagem
def show_question(window,font,index):
    window.fill(WHITE)

    # Exibe a pontuação
    score_text = font.render(f"Score: {score}", True, BLACK)
    window.blit(score_text, (20, 20))

    # Cabeçalho da pergunta "Inferência Lógica"
    question_header = font.render("Lógica Proposicional", True, BLACK)
    header_rect = question_header.get_rect(center=(WIDTH // 2, 40))
    window.blit(question_header, header_rect)

    # Cabeçalho da pergunta "Qual é essa regra, com base na imagem a seguir:"
    question_header = font.render("Responda essa questão abaixo:", True, BLACK)
    window.blit(question_header, (60, 80))
    
    # Carrega a imagem da pergunta
    question_image = pygame.image.load(questions[index]["question_image"])
    window.blit(question_image, (75, 110))

    # Cabeçalho da pergunta "Qual é essa regra, com base na imagem a seguir:"
    question_header = font.render("Escolha uma das opções abaixo, utilize as teclas (A,B,C,D ou E) para resposta:", True, BLACK)
    window.blit(question_header, (60, 385))
    
    option_y = 410
    for option in questions[index]["options"]:
        option_text = font.render(option, True, BLACK)
        window.blit(option_text, (60, option_y))
        option_y += 25

    pygame.draw.rect(window, (0, 0, 255), (button_x - 150, button_y, button_width, button_height))
    hint_text = font.render("Dica (-1pt)", True, (255, 255, 255))
    hint_rect = hint_text.get_rect(center=(button_x - 90, button_y + button_height // 2))
    window.blit(hint_text, hint_rect)

    pygame.draw.rect(window, (128, 128, 128), (button_x - 300, button_y, button_width, button_height))
    pause_text = font.render("Pausar", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(button_x - 240, button_y + button_height // 2))
    window.blit(pause_text, pause_rect)

    pygame.draw.rect(window, (255, 0, 0), (button_x - 450, button_y, button_width, button_height))
    quit_text = font.render("Sair", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(button_x - 390, button_y + button_height // 2))
    window.blit(quit_text, quit_rect)


def show_game_over_screen(window,font,screen,user_name):
    window.fill((255, 0, 0))  # Vermelho
    game_over_text = font.render("Game Over", True, (255, 255, 255))  # Branco
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    classificacao = 2
    score = 3
    question_index = 0
    classification(classificacao)
    menu.show_menu(screen,user_name)  # Mostra o menu de sair
    pygame.quit()
    sys.exit()

def show_congratulations_screen(window,font,screen,user_name):
    window.fill((0, 255, 0))  # Verde
    congrats_text = font.render("Parabéns! Você concluiu o modulo da lógica Proposicional!", True, WHITE)
    text_rect = congrats_text.get_rect(center=(400, 300))
    window.blit(congrats_text, text_rect)
    congrats_text2 = font.render("Agora vamos para modulo da Inferência Lógica!", True, WHITE)
    text_rect = congrats_text.get_rect(center=(400, 400))
    window.blit(congrats_text2, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    classificacao = 3
    with open('./classificacao.txt','a') as arquivo:
        arquivo.write("3,"+'\n')
        arquivo.close()
    inferenciaLogica.main(screen,user_name)
    pygame.quit()
    sys.exit()

def show_pause_screen(window,font):
    global input_active
    window.fill((0, 0, 0))  # Preto
    pause_text = font.render("Jogo Pausado", True, (255, 255, 255))  # Branco
    message_text = font.render("Pressione Espaço para Voltar ao Jogo", True, (255, 255, 255))  # Branco
    text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    window.blit(pause_text, text_rect)
    window.blit(message_text, message_rect)
    pygame.display.flip()
    
    is_paused = True
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = False

        pygame.time.delay(100)
    
    input_active = True

def show_hint_screen(window,font,dica,screen,user_name):
    global score, input_active

    score -= 1
    window.fill((0, 0, 0))  # Preto
    dica_text = font.render(dica, True, (255, 255, 255))  # Branco
    text_rect = dica_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(dica_text, text_rect)

    message_text = font.render("Pressione Espaço para voltar ao jogo", True, (255, 255, 255))  # Branco
    message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    window.blit(message_text, message_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting_for_input = False
                elif event.key == pygame.K_SPACE:
                    waiting_for_input = False

        pygame.time.delay(100)

        if score <= 0:
            classificacao = 2
            score = 3
            question_index = 0
            menu.show_menu(screen,user_name)  # Mostra o menu de sair

    input_active = True

def show_correct_screen(window,font):
    window.fill((0, 255, 0))  # Verde
    congrats_text = font.render("Você acertou!", True, (255, 255, 255))  # Branco
    text_rect = congrats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(congrats_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

def show_wrong_screen(window,font):
    window.fill((255, 0, 0))  # Vermelho
    game_over_text = font.render("Você errou. Tente novamente!", True, (255, 255, 255))  # Branco
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)


# Função principal do jogo
def main(screen,user_name):
    global score, question_index

    score = 3  # Adicione essa linha para inicializar a variável score
    # Configurações da tela
    WIDTH, HEIGHT = 800, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Logic T.E.I - Lógica Proposicional")

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fonte
    font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 18)

    # Dimensões do botão
    button_width = 120
    button_height = 40
    button_x = WIDTH - button_width - 20  # Correção aqui
    button_y = HEIGHT - button_height - 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    check_answer("A",window,font,screen,user_name)
                elif event.key == pygame.K_b:
                    check_answer("B",window,font,screen,user_name)
                elif event.key == pygame.K_c:
                    check_answer("C",window,font,screen,user_name)
                elif event.key == pygame.K_d:
                    check_answer("D",window,font,screen,user_name)
                elif event.key == pygame.K_e:
                    check_answer("E",window,font,screen,user_name)

        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if question_index < len(questions):
                	# Botão de dica
                	    if button_x - 150 <= x <= button_x - 30 and button_y <= y <= button_y + button_height:
                	            show_hint_screen(window,font,dicas[question_index],screen,user_name)  # Mostra a tela de dica


                	    # Botão de pausa
                	    if button_x - 300 <= x <= button_x - 180 and button_y <= y <= button_y + button_height:
                	        show_pause_screen(window,font)  # Mostra a tela de pausa

                	    # Botão de sair
                	    elif button_x - 450 <= x <= button_x - 330 and button_y <= y <= button_y + button_height:
                                score = 3
                                question_index = 0
                                menu.show_menu(screen,user_name)  # Mostra o menu de sair
                 

        if question_index < len(questions):
            show_question(window,font,question_index)
        elif score >= 33:
            classificacao = 4
            classification(classificacao)
            show_congratulations_screen(window,font,screen,user_name)
        else:
            classificacao = 2
            question_index = 0
            show_question(window,font,question_index)
            # Fim do jogo
            #window.fill(WHITE)
            #game_over_text = font.render(f"Game Over!", True, BLACK)
            #window.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
            #pygame.display.flip()
            #pygame.time.delay(3000)  # Delay de 3 segundos antes de sair do jogo
            #running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Função para verificar a resposta do jogador
def check_answer(selected_option,window,font,screen,user_name):
    global score, question_index

    if selected_option == questions[question_index]["correct_answer"]:
        score += 3
        show_correct_screen(window,font)
        question_index += 1
    else:
        score -= 1
        show_wrong_screen(window,font)
    if score <= 0:
        classificacao = 2
        classification(classificacao)
        show_game_over_screen(window,font,screen,user_name)
    elif score >= 33:
        classificacao = 4
        classification(classificacao)
        show_congratulations_screen(window,font,screen,user_name)

    

# Iniciar o jogo
if __name__ == "__main__":
    main(screen,user_name)

    # Encerramento do Pygame
    pygame.quit()
    sys.exit()