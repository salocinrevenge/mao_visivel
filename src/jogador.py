class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 1000  # Exemplo de valor inicial
        self.terrenos = []
        self.cartas = []

    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def __str__(self):
        return f"{self.nome} - Dinheiro: {self.dinheiro} - Terrenos: {len(self.terrenos)} - Cartas: {len(self.cartas)}"
    
    def render(self, screen, camera):
        # Renderizar o jogador na tela
        pass

    def tick(self):
        # Atualizar o estado do jogador, se necessário
        pass