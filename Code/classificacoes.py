import pygame
import menu

# Mostrar tela de informações sobre o jogo
def show_classificacoes(screen,user_name):
    
        # Carrega a imagem de fundo
    background_image = pygame.image.load('./imagens/capa/capa.jpg')

    # Redimensiona a imagem de fundo para corresponder à tela
    background_image = pygame.transform.scale(background_image, (800, 600))

    largura_tela = 800
    altura_tela = 600

    pygame.display.set_caption("Classificação de Módulos")
    menu_font = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 22)
    
    back_text = menu_font.render("Pressione ESC para voltar ao menu.", True, (0, 0, 0))

    # Cores
    cor_fundo = (255, 255, 255)
    cor_texto = (0, 0, 0)

    # Fonte e tamanho do texto
    fonte = pygame.font.Font('./fontes/DalekPinpointBold.ttf', 22)

    # Dicionário de mapeamento de números de módulos para nomes
    modulo_nomes = {
        0: "Não começou",
        1: "Tabela Verdade",
        2: "Equivalência Lógica",
        3: "Lógica Proposicional",
        4: "Inferência Lógica"
    }

    # Lê o arquivo de classificação
    classificacao = []
    try:
        with open("classificacao.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                if len(partes) == 2:
                    modulo = int(partes[0])
                    usuario = partes[1]
                    classificacao.append((modulo, usuario))
    except FileNotFoundError:
        print("O arquivo 'classificacao.txt' não foi encontrado.")

    # Ordena a classificação pelo módulo
    classificacao.sort(reverse=True)
    maior_modulo, nome_maior_modulo = classificacao[0] if classificacao else (None, None)

    # Texto a ser exibido
    if maior_modulo is not None:
        nome_modulo = modulo_nomes.get(maior_modulo, "Módulo Desconhecido")
        texto = f" {maior_modulo} - {nome_modulo} - Usuário: {nome_maior_modulo}"
    else:
        texto = "Nenhum módulo encontrado"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                    menu.show_menu(screen,user_name)

        
        screen.fill((255, 255, 255))

        screen.blit(background_image, (0, 0))  # Desenha a imagem de fundo
        
        #Renderiza o texto na tela
        texto_surface = fonte.render(texto, True, cor_texto)
        texto_rect = texto_surface.get_rect()
        texto_rect.center = (largura_tela // 2, altura_tela // 2)
        screen.blit(texto_surface, texto_rect)

        back_rect = back_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
        screen.blit(back_text, back_rect)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))