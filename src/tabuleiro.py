from src.jogador import Jogador
from src.terreno import Terreno

class Tabuleiro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(4)]  # Exemplo com 4 jogadores
        self.cartas = []
        self.terrenos = []
        self.vez = 0
        self.dims = (11,11)

        self.criar_terrenos("mapas/minecraft1.txt")

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def distribuir_cartas(self):
        # Lógica para distribuir cartas entre os jogadores
        pass

    def tick(self):
        # Atualizar o estado do tabuleiro
        pass

    def render(self, screen, camera):
        # Renderizar o tabuleiro e os jogadores na tela
        for terreno in self.terrenos:
            terreno.render(screen, camera)
        for jogador in self.jogadores:
            jogador.render(screen, camera)
        pass

    def criar_terrenos(self, path):
        # Lógica para criar terrenos a partir de um arquivo
        try:
            with open(path, "r") as file:
                for i, linha in enumerate(file):
                    adicionando = linha.strip().split(" ")
                    if adicionando:  # Ignorar linhas vazias
                        print(f"Adicionando terreno: {adicionando}")
                        self.terrenos.append(Terreno(*adicionando, i, self))
        except FileNotFoundError:
            print("Arquivo de terrenos não encontrado.")
        

    def input(self, event):
        # Processar eventos de entrada, como cliques ou teclas pressionadas
        pass