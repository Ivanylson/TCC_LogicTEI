import pygame
import sys
import menu
import tabelaVerdade
import logicaProposicional

# Inicialização do Pygame
#pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
#window = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption("Equivalência Lógica")

# Pontuação inicial
score = 2
global classificacao

def classification(classificacao):
    return classificacao

# Função para atualizar a pontuação e verificar o estado do jogo
def update_score(window,font,correct,screen,user_name):
    global score
    if correct:
        score += 2
    else:
        score -= 1

    if score <= 0: 
    	classificacao = 1
    	classification(classificacao)
    	input_active = False
    	score = 2
    	for phase in phases:
    		for row in range(1, 5):
    			phase[row][-1] = "-"
    	current_phase = 0
    	show_game_over_screen(window,font,screen,user_name)

    elif score >= 12:
    	classificacao = 2
    	classification(classificacao)
    	input_active = False
    	score = 2
    	for phase in phases:
    		for row in range(1, 5):
    			phase[row][-1] = "-"
    	current_phase = 0
    	show_congratulations_screen(window,font,screen,user_name)

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Fonte
#font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 24)

# Dimensões da tabela
table_width = 500
table_height = 200
cell_width = table_width // 3
cell_height = table_height // 4

# Centralização da tabela na tela
table_x = (screen_width - table_width) // 2
table_y = (screen_height - table_height) // 2

# Dimensões do botão
button_width = 120
button_height = 40
button_x = screen_width - button_width - 20
button_y = screen_height - button_height - 20

# Fases
phases = [
    [
        ["1º", "2º", "Equivalente"],
        ["p -> q", "~q -> ~p", "-"],
        ["p -> q", "~p v q", "-"],
        ["p -> q", "~p v ~q", "-"],
        ["p v q", "~p -> q", "-"]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["~(~p)", "p", "-"],
        ["p ^ p", "~p", "-"],
        ["p ^ p", "p", "-"],
        ["p v p", "p", "-"]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["p v (p ^ q)", "p", "-"],
        ["p ^ (p v q)", "~p", "-"],
        ["p ^ (p v q)", "p", "-"],
        ["p ^ q", "q ^ p", "-"]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["p v q", "q ^ p", "-"],
        ["p v q", "q v p", "-"],
        ["p <-> q", "q <-> p", "-"],
        ["(p ^ q) ^ r", "p ^ (q ^ r)", "-"]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["(p v q) v r", "p v (q v r)", "-"],
        ["p ^ (q v s )", "(p^q)v(p^s)", "-"],
        ["p v (q ^ s )", "(pvq)^(p^s)", "-"],
        ["p v (q ^ s )", "(pvq)^(pvs)", "-"]
    ]
]
# Respostas corretas para cada fase
respostas = [
    [
        ["1º", "2º", "Equivalente"],
        ["p -> q", "~q -> ~p", True],
        ["p -> q", "~p v q", True],
        ["p -> q", "~p v ~q", False],
        ["p v q", "~p -> q", True]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["~(~p)", "p", True],
        ["p ^ p", "~p", False],
        ["p ^ p", "p", True],
        ["p v p", "p", True]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["p v (p ^ q)", "p", True],
        ["p ^ (p v q)", "p", True],
        ["p ^ (p v q)", "~p", False],
        ["p ^ q", "q ^ p", True]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["p v q", "q ^ p", False],
        ["p v q", "q v p", True],
        ["p <-> q", "q <-> p", True],
        ["(p ^ q) ^ r", "p ^ (q ^ r)", True]
    ],
    [
        ["1º", "2º", "Equivalente"],
        ["(p v q) v r", "p v (q v r)", True],
        ["p ^ (q v s )", "(p ^ q) v (p ^ s)", True],
        ["p v (q ^ s )", "(p v q) ^ (p ^ s)", False],
        ["p v (q ^ s )", "(p v q) ^ (p v s)", True]
    ]
]

# Dicas para cada fase
dicas = [
    "Dica da Fase 1: Não tem dica",
    "Dica da Fase 2: Estude mais",
    "Dica da Fase 3: Caiu na pegadinha",
    "Dica da Fase 4: lembre-se AND,OR e da ordem"
    "Dica da Fase 5: HAHA menos 1pts"
]

current_phase = 0  # Começa na primeira fase

def draw_table(window, font):
    window.fill(white)
    
    for row in range(5):
        for col in range(3):
            cell_x = table_x + col * cell_width
            cell_y = table_y + row * cell_height
            
            pygame.draw.rect(window, black, (cell_x, cell_y, cell_width, cell_height), 1)
            cell_text = font.render(str(phases[current_phase][row][col]), True, black)
            cell_rect = cell_text.get_rect(center=(cell_x + cell_width // 2, cell_y + cell_height // 2))
            window.blit(cell_text, cell_rect)

def show_game_over_screen(window,font, screen,user_name):
    window.fill(red)
    game_over_text = font.render("Game Over", True, white)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    classificacao = 1
    classification(classificacao)
    menu.show_menu(screen,user_name)
    pygame.quit()
    sys.exit()

def show_congratulations_screen(window,font,screen,user_name):
    window.fill(green)
    congrats_text = font.render("Parabéns! Você concluiu o modulo da Equivalência Lógica!", True, white)
    text_rect = congrats_text.get_rect(center=(400, 300))
    window.blit(congrats_text, text_rect)
    congrats_text2 = font.render("Agora vamos para modulo da Lógica Proposicional!", True, white)
    text_rect = congrats_text.get_rect(center=(400, 400))
    window.blit(congrats_text2, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    input_active = False
    score = 2
    for phase in phases:
    	for row in range(1, 5):
    		phase[row][-1] = "-"
    classificacao = 2
    with open('./classificacao.txt','a') as arquivo:
        arquivo.write("2,"+user_name+'\n')
        arquivo.close()
    classification(classificacao)
    logicaProposicional.main(screen,user_name)
    pygame.quit()
    sys.exit()

def show_pause_screen(window,font):
    global input_active  # Adicione essa linha para acessar a variável input_active globalmente
    window.fill(black)
    pause_text = font.render("Jogo Pausado", True, white)
    message_text = font.render("Pressione Espaço para Voltar ao Jogo", True, white)
    text_rect = pause_text.get_rect(center=(screen_width // 2, screen_height // 2 - 30))
    message_rect = message_text.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
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
                if event.key == pygame.K_SPACE:  # Verifica se a tecla Espaço foi pressionada
                    is_paused = False

        pygame.time.delay(100)  # Pequeno atraso para evitar uso excessivo da CPU
        
    input_active = True  # Restaura o estado do input_active

def show_hint_screen(window,font,dica,screen,user_name):
    global score, input_active

    score -= 1  # Perde um ponto ao pedir dica
    window.fill(black)
    dica_text = font.render(dica, True, white)
    text_rect = dica_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(dica_text, text_rect)

    # Mostra a mensagem para pressionar Espaço para voltar ao jogo
    message_text = font.render("Pressione Espaço para voltar ao jogo", True, white)
    message_rect = message_text.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
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
                elif event.key == pygame.K_SPACE:  # Pressione Espaço para voltar ao jogo
                    waiting_for_input = False

        pygame.time.delay(100)  # Pequeno atraso para evitar uso excessivo da CPU

        if score <= 0:
        	classificacao = 1
        	input_active = False
        	score = 2
        	for phase in phases:
        		for row in range(1, 5):
        			phase[row][-1] = "-"
        	current_phase = 0
        	classification(classificacao)
        	show_game_over_screen(window,font,screen,user_name)

    input_active = True  # Restaura o estado do input_active

def zero_fases(screen, user_name):
    score = 2
    for phase in phases:
        for row in range(1, 5):
            phase[row][-1] = "-"   
    current_phase = 0
    input_active = False

def show_correct_screen(window,font):
    window.fill(green)
    congrats_text = font.render("Você acertou!", True, white)
    text_rect = congrats_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(congrats_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

def show_wrong_screen(window,font):
    window.fill(red)
    game_over_text = font.render("Você errou. Tente novamente!", True, white)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

def main(screen,user_name):
    global score, current_phase
    input_active = False
    active_row = None
    # Configurações da tela
    screen_width = 800
    screen_height = 600
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Logic T.E.I - Equivalência Lógica")
    # Fonte 
    font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 24)
    # Cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    table_width = 500
    table_height = 200
    cell_width = table_width // 3
    cell_height = table_height // 4
    table_x = (screen_width - table_width) // 2
    table_y = (screen_height - table_height) // 2
    button_width = 120
    button_height = 40
    button_x = screen_width - button_width - 20
    button_y = screen_height - button_height - 20
    blue = (0, 0, 255)
    gray = (128, 128, 128)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked_row = (y - table_y) // cell_height
                clicked_col = (x - table_x) // cell_width


                if 0 <= clicked_row < 5 and 0 <= clicked_col < 3 and clicked_col == 2 and clicked_row > 0:
                    input_active = True
                    active_row = clicked_row
                if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
                  if input_active:
                        user_answer = phases[current_phase][active_row][2]
                        correct_answer = respostas[current_phase][active_row][2]
                        if user_answer == correct_answer:
                            #phases[current_phase][active_row][2] = True  # Marca a resposta como correta
                            all_correct = all(phases[current_phase][row][2] == respostas[current_phase][row][2] for row in range(1, 5))
                            if all_correct:
                                update_score(window,font,True,screen,user_name)  # Atualiza a pontuação
                                show_correct_screen(window,font)  # Mostra a tela de acerto
                                current_phase += 1  # Avança para a próxima fase
                                if current_phase >= len(phases):
                                    current_phase = 0  # Volta para a primeira fase
                                    show_correct_screen(window,font)  # Mostra a tela de acerto

                            else:
                                    update_score(window,font,False,screen,user_name)  # Atualiza a pontuação
                                    show_wrong_screen(window,font)  # Mostra a tela de erro

                        else:
                            	 update_score(window,font,False,screen,user_name)  # Atualiza a pontuação
                            	 show_wrong_screen(window,font)  # Mostra a tela de erro 
        
                        input_active = False  # Reseta o input_active após resposta

            # Botão de dica
                if button_x - 150 <= x <= button_x - 30 and button_y <= y <= button_y + button_height:
                        show_hint_screen(window,font,dicas[current_phase],screen,user_name)  # Mostra a tela de dica


                # Botão de pausa
                if button_x - 300 <= x <= button_x - 180 and button_y <= y <= button_y + button_height:
                    show_pause_screen(window,font)  # Mostra a tela de pausa

                # Botão de sair
                elif button_x - 450 <= x <= button_x - 330 and button_y <= y <= button_y + button_height:
                    current_phase = 0
                    input_active = False
                    score = 3
                    for phase in phases:
                        for row in range(1, 5):
                            phase[row][-1] = "-"
                    tabelaVerdade.zero_fases(screen,user_name)
                    menu.show_menu(screen,user_name)  # Mostra o menu de sair


            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    phases[current_phase][active_row][2] = ""  # Limpar a célula
                elif event.key == pygame.K_t:
                    phases[current_phase][active_row][2] = True
                elif event.key == pygame.K_f:
                    phases[current_phase][active_row][2] = False
             
        draw_table(window,font)

        if input_active:
            cell_x = table_x + 2 * cell_width
            cell_y = table_y + active_row * cell_height
            pygame.draw.rect(window, black, (cell_x, cell_y, cell_width, cell_height), 2)

        # Botão de validação
        pygame.draw.rect(window, green, (button_x, button_y, button_width, button_height))
        button_text = font.render("Validar", True, white)
        button_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        window.blit(button_text, button_rect)

        # Botão de dica
        pygame.draw.rect(window, blue, (button_x - 150, button_y, button_width, button_height))
        hint_text = font.render("Dica (-1pt)", True, white)
        hint_rect = hint_text.get_rect(center=(button_x - 90, button_y + button_height // 2))
        window.blit(hint_text, hint_rect)

        # Botão de pausa
        pygame.draw.rect(window, gray, (button_x - 300, button_y, button_width, button_height))
        pause_text = font.render("Pausar", True, white)
        pause_rect = pause_text.get_rect(center=(button_x - 240, button_y + button_height // 2))
        window.blit(pause_text, pause_rect)

        # Botão de sair
        pygame.draw.rect(window, red, (button_x - 450, button_y, button_width, button_height))
        quit_text = font.render("Sair", True, white)
        quit_rect = quit_text.get_rect(center=(button_x - 390, button_y + button_height // 2))
        window.blit(quit_text, quit_rect)

        # Exibe a pontuação
        score_text = font.render(f"Score: {score}", True, black)
        window.blit(score_text, (20, 20))

        # Exibe a pontuação
        title_text = font.render("Equivalência Lógica", True, black)
        title_rect = title_text.get_rect(center=(screen_width // 2, table_y - 120))
        window.blit(title_text, title_rect)
        instruction_text = font.render("Clique com mouse em cada caixinha na última coluna", True, black)
        instruction_rect = instruction_text.get_rect(center=(screen_width // 2, table_y - 80))
        window.blit(instruction_text, instruction_rect)
        instruction_text = font.render("Preenchendo com as teclas T(True) ou F(False) e ao final valide", True, black)
        instruction_rect = instruction_text.get_rect(center=(screen_width // 2, table_y - 50))
        window.blit(instruction_text, instruction_rect)
        instruction_text2 = font.render("Para verificar se a setença 1 e 2 são equivalentes", True, black)
        instruction_rect2 = instruction_text2.get_rect(center=(screen_width // 2, table_y - 25))
        window.blit(instruction_text2, instruction_rect2)


        pygame.display.flip()

if __name__ == "__main__":
    current_phase = 0;
    main(screen,user_name)

    # Encerramento do Pygame
    pygame.quit()
    sys.exit()