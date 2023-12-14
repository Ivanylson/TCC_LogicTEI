import pygame
import sys
import menu
import tabelaVerdade  # Importe o módulo sobre
import equivalenciaLogica
import logicaProposicional
import inferenciaLogica

# Mostrar tela de informações sobre o jogo

# Função para ação do botão "B - tabela verdade"
def acao_botao_tabela_verdade():
    print("Botão 'Iniciante : Tabela Verdade' clicado")

# Função para ação do botão "Intermediário: equivalência lógica"
def acao_botao_equivalencia_logica():
    print("Botão 'Intermediário: Equivalência Lógica' clicado")

# Função para ação do botão "Avançado: Lógica Proposicional"
def acao_botao_logica_proposicional():
    print("Botão 'Avançado: Lógica Proposicional' clicado")

# Função para ação do botão "Especialista: Inferência Lógica"
def acao_botao_inferencia_logica():
    print("Botão 'Especialista: Inferência Lógica' clicado")


def show_escolhaDificuldade(screen,user_name):
	pygame.display.set_caption("Nível de dificuldade")

	largura_tela = 800
	altura_tela = 600
	
	# Cores
	cor_fundo = (255, 255, 255)
	cor_botao = (0, 128, 255)
	cor_texto = (255, 255, 255)

	# Fonte e tamanho do texto
	fonte = pygame.font.Font(None, 22)
	back_text = fonte.render("Pressione ESC para voltar ao menu.", True, (0, 0, 0))

	# Carrega a imagem de fundo
	background_image = pygame.image.load('./imagens/capa/capa.jpg')
	# Redimensiona a imagem de fundo para corresponder à tela
	background_image = pygame.transform.scale(background_image, (800, 600))

	# Textos dos botões
	textos = ["Iniciante: Tabela Verdade", "Intermediário: Equivalência Lógica", "Avançado: Lógica Proposicional", "Especialista: Inferência Lógica"]

	# Largura e altura dos botões
	largura_botao = 500
	altura_botao = 80

	# Posição x centralizada dos botões
	posicao_x_botao = (largura_tela - largura_botao) // 2

	# Retângulos dos botões
	botoes = []
	for i, texto in enumerate(textos):
	    botao = pygame.Rect(posicao_x_botao, 100 + i * 100, largura_botao, altura_botao)
	    botoes.append(botao)

	# Loop principal
	rodando = True
	while rodando:
	    for evento in pygame.event.get():
	        if evento.type == pygame.QUIT:
	            rodando = False
	        if evento.type == pygame.MOUSEBUTTONDOWN:
	            posicao_mouse = pygame.mouse.get_pos()
	            for i, botao in enumerate(botoes):
	                if botao.collidepoint(posicao_mouse):
	                    if i == 0:
	                        acao_botao_tabela_verdade()
	                        tabelaVerdade.main(screen, user_name)
	                    elif i == 1:
	                        acao_botao_equivalencia_logica()
	                        equivalenciaLogica.main(screen,user_name)
	                    elif i == 2:
	                        acao_botao_logica_proposicional()
	                        logicaProposicional.main(screen,user_name)
	                    elif i == 3:
	                        acao_botao_inferencia_logica()
	                        inferenciaLogica.main(screen,user_name)

	        elif evento.type == pygame.KEYDOWN:
	        	if evento.key == pygame.K_ESCAPE:
	        		menu.show_menu(screen,user_name)

	    screen.fill(cor_fundo)
	    screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
	    
	    for i, botao in enumerate(botoes):
	        pygame.draw.rect(screen, cor_botao, botao)
	        
	        # Centralize o texto no botão
	        texto = fonte.render(textos[i], True, cor_texto)
	        texto_rect = texto.get_rect()
	        texto_rect.center = botao.center
	        
	        # Desenhe o texto no botão
	        screen.blit(texto, texto_rect)

	        back_rect = back_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 220))
        	screen.blit(back_text, back_rect)
	    

	    pygame.display.flip()

if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    # Encerramento do Pygame
    pygame.quit()
    sys.exit()