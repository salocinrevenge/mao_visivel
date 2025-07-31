from src.jogador import Jogador
from src.terreno import Terreno
from src.camera import Camera

class Tabuleiro:
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(4)]  # Exemplo com 4 jogadores
        self.cartas = []
        self.terrenos = []
        self.vez = 0
        self.dims = (11,11)

        self.escala = 0.25
        self.camera = Camera([1000,0], self.escala)

        self.criar_terrenos("mapas/minecraft1.txt")


    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def distribuir_cartas(self):
        # Lógica para distribuir cartas entre os jogadores
        pass

    def tick(self):
        # Atualizar o estado do tabuleiro
        pass

    def render(self, screen):
        # Renderizar o tabuleiro e os jogadores na tela

        for i in range(len(self.terrenos)//2, 0, -1):

            self.terrenos[i].render(screen, self.camera)
            self.terrenos[-i].render(screen, self.camera)
        self.terrenos[0].render(screen, self.camera)  # Renderizar o terreno central
        for jogador in self.jogadores:
            jogador.render(screen, self.camera)
        pass

    def criar_terrenos(self, path):
        # Lógica para criar terrenos a partir de um arquivo
        try:
            with open(path, "r") as file:
                i = -1
                for linha in file:
                    i += 1
                    adicionando = linha.strip()
                    if adicionando:  # Ignorar linhas vazias
                        adicionando = adicionando.split(" ")
                        self.terrenos.append(Terreno(*adicionando, i, self, self.escala))
                    else:
                        i -= 1  # Não contar linhas vazias

        except FileNotFoundError:
            print("Arquivo de terrenos não encontrado.")
        

    def input(self, event):
        pass