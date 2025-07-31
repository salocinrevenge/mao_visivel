from src.jogador import Jogador
from src.terreno import Terreno
import os

class Tabuleiro:
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.jogadores = [Jogador(f"Jogador {i+1}") for i in range(4)]  # Exemplo com 4 jogadores
        self.cartas = []
        self.terrenos = []
        self.vez = 0
        self.dims = (11,11)

        self.escala = 0.22
        self.menor_dim_imagens = (540-200) * self.escala

        self.criar_terrenos("mapas/minecraft1.txt")

        self.contador = 0

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def distribuir_cartas(self):
        # Lógica para distribuir cartas entre os jogadores
        pass

    def tick(self):
        # Atualizar o estado do tabuleiro
        self.contador +=1
        pass

    def render(self, screen, camera):
        # Renderizar o tabuleiro e os jogadores na tela
        i = 0
        for terreno in self.terrenos:
            i += 1
            if self.contador / 10 < i:
                continue
            terreno.render(screen, camera)
        for jogador in self.jogadores:
            jogador.render(screen, camera)
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
        # Processar eventos de entrada, como cliques ou teclas pressionadas
        for terreno in self.terrenos:
            terreno.input(event)