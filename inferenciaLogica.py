import pygame
import sys
import random
import menu

# Inicialização do Pygame
#pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
#window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Inferência Lógica")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte
#font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 24)

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
    "Dica da Fase 1: Lembre-se negação, afirmar, técnica, implica, se somente se",
    "Dica da Fase 2: Caiu na pegadinha",
    "Dica da Fase 3: Menos 1pt, HAHA",
    "Dica da Fase 4: Não tem dica",
    "Dica da Fase 5: Lembre-se negação, afirmar, técnica, implica, se somente se",
    "Dica da Fase 6: Menos 1pt, HAHA",
    "Dica da Fase 7: Não tem dica",
    "Dica da Fase 8: Caiu na pegadinha",
    "Dica da Fase 9: Lembre-se negação, afirmar, técnica, implica, se somente se",
    "Dica da Fase 10: Não tem dica",
    "Dica da Fase 11: Menos 1pt, HAHA",
    "Dica da Fase 12: Não tem dica",
    "Dica da Fase 13: Menos 1pt, HAHA",
    "Dica da Fase 14: Lembre-se negação, afirmar, técnica, implica, se somente se",
    "Dica da Fase 15: Não tem dica",
    "Dica da Fase 16: Menos 1pt, HAHA",
    "Dica da Fase 17: Lembre-se negação, afirmar, técnica, implica, se somente se",
    "Dica da Fase 18: Caiu na pegadinha",
    "Dica da Fase 19: Lembre-se negação, afirmar, técnica, implica, se somente se"
]


# Perguntas e respostas
questions = [
    {
        "question_image": "./questoesIL/mp.png",
        "options": ["A) Modus tollens", "B) Modus ponens", "C) Resolução", "D) Absorção", "E) Associativa"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesIL/mt.png",
        "options": ["A) Modus tollens", "B) Modus ponens", "C) Resolução", "D) Absorção", "E) Exportação"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesIL/ass.png",
        "options": ["A) Introdução da conjunção - Conjunção", "B) Distributiva", "C) Resolução", "D) Silogismo disjuntivo", "E) Associativa"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesIL/adicao.png",
        "options": ["A) Adição", "B) Absorção", "C) Resolução", "D) Comutativa", "E) Associativa"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesIL/com.png",
        "options": ["A) Adição", "B) Dupla negação", "C) Resolução", "D) Comutativa", "E) Silogismo hipotético"],
        "correct_answer": "D"
    },
	{
        "question_image": "./questoesIL/introbi.png",
        "options": ["A) Introdução da disjunção", "B) Distributiva", "C) Introdução do bicondicional", "D) Introdução da conjunção - Conjunção", "E) Silogismo hipotético"],
        "correct_answer": "C"
    },
	{
        "question_image": "./questoesIL/export.png",
        "options": ["A) Absorção", "B) Resolução", "C) Exportação", "D) Transposição da contrapositiva", "E) Implicação material"],
        "correct_answer": "C"
    },
	{
        "question_image": "./questoesIL/transcontra.png",
        "options": ["A) Simplificação da disjunção", "B) Introdução do bicondicional", "C) Introdução da conjunção - Conjunção", "D) Eliminação da conjunção - Simplificação", "E) Transposição da contrapositiva"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesIL/silohipo.png",
        "options": ["A) Simplificação da disjunção", "B) Silogismo hipotético", "C) Implicação material", "D) Distributiva", "E) Absorção"],
        "correct_answer": "B"
    },
	{
        "question_image": "./questoesIL/impliMaterial.png",
        "options": ["A) Implicação material", "B) Resolução", "C) Introdução da disjunção", "D) Eliminação da conjunção - Simplificação", "E) Simplificação da disjunção"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesIL/distri.png",
        "options": ["A) Absorção", "B) Resolução", "C) Introdução da disjunção", "D) Distributiva", "E) Simplificação da disjunção"],
        "correct_answer": "D"
    },
	{
        "question_image": "./questoesIL/absorcao.png",
        "options": ["A) Associativa", "B) Silogismo disjuntivo", "C) Introdução da disjunção", "D) Absorção", "E) Modus ponens"],
        "correct_answer": "D"
    },
	{
        "question_image": "./questoesIL/silogdisj.png",
        "options": ["A) Silogismo disjuntivo", "B) Introdução da disjunção", "C) Resolução", "D) Exportação", "E) Modus tollens"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesIL/introdisj.png",
        "options": ["A) Introdução da disjunção", "B) Silogismo disjuntivo", "C) Introdução do bicondicional", "D) Introdução da conjunção - Conjunção", "E) Introdução do bicondicional"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesIL/elimiconj.png",
        "options": ["A) Introdução da conjunção - Conjunção", "B) Silogismo disjuntivo", "C) Silogismo hipotético", "D) Introdução da conjunção - Conjunção", "E) Eliminação da conjunção - Simplificação"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesIL/introconj.png",
        "options": ["A) Silogismo hipotético", "B) Transposição da contrapositiva", "C) Silogismo disjuntivo", "D) Simplificação da disjunção", "E) Introdução da conjunção - Conjunção"],
        "correct_answer": "E"
    },
	{
        "question_image": "./questoesIL/duplaneg.png",
        "options": ["A) Dupla negação", "B) Simplificação da disjunção", "C) Distributiva", "D) Comutativa", "E) Introdução do bicondicional"],
        "correct_answer": "A"
    },
	{
        "question_image": "./questoesIL/simplidisj.png",
        "options": ["A) Silogismo hipotético", "B) Implicação material ", "C) Simplificação da disjunção", "D) Silogismo disjuntivo", "E) Resolução"],
        "correct_answer": "C"
    },
	{
        "question_image": "./questoesIL/resolucao.png",
        "options": ["A) Simplificação da disjunção", "B) Silogismo hipotético", "C) Silogismo disjuntivo", "D) Resolução", "E) Introdução da conjunção - Conjunção"],
        "correct_answer": "D"
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
    question_header = font.render("Inferência Lógica", True, BLACK)
    header_rect = question_header.get_rect(center=(WIDTH // 2, 40))
    window.blit(question_header, header_rect)


    # Cabeçalho da pergunta "Qual é essa regra, com base na imagem a seguir:"
    question_header = font.render("Escolha uma das opções abaixo, utilize as teclas (A,B,C,D ou E) para resposta:", True, BLACK)
    window.blit(question_header, (60, 70))

    # Cabeçalho da pergunta "Qual é essa regra, com base na imagem a seguir:"
    question_header = font.render("Qual é essa regra, com base na imagem a seguir:", True, BLACK)
    window.blit(question_header, (60, 100))
    
    # Carrega a imagem da pergunta
    question_image = pygame.image.load(questions[index]["question_image"])
    window.blit(question_image, (60, 140))

    option_y = 260
    for option in questions[index]["options"]:
        option_text = font.render(option, True, BLACK)
        window.blit(option_text, (50, option_y))
        option_y += 50

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
    classificacao = 3
    classification(classificacao)
    score = 3
    question_index = 0
    menu.show_menu(screen,user_name)  # Mostra o menu de sair
    pygame.quit()
    sys.exit()

def show_congratulations_screen(window,font,screen,user_name):
    window.fill((0, 255, 0))  # Verde
    congrats_text = font.render("Parabéns! Você concluiu o jogo!", True, (255, 255, 255))  # Branco
    text_rect = congrats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(congrats_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    classificacao = 4
    with open('./classificacao.txt','a') as arquivo:
        arquivo.write("4,"+user_name+'\n')
        arquivo.close()
    menu.show_menu(screen,user_name)  # Mostra o menu de sair
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
            classificacao = 3
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
    pygame.display.set_caption("Logic T.E.I - Inferência Lógica")

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fonte
    font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 19)

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
            classificacao = 3
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
        classificacao = 3
        classification(classificacao)
        show_game_over_screen(window,font,screen,user_name)
    elif score >= 57:
        classificacao = 4
        classification(classificacao)
        show_congratulations_screen(window,font,screen,user_name)

    

if __name__ == "__main__":
    main(screen,user_name)

    # Encerramento do Pygame
    pygame.quit()
    sys.exit()