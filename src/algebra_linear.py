def calcular_posicao_absoluta(posicao_relativa_absoluta, dim_bloco):
    # Calcula a posição isométrica para plotar na tela
    x = (posicao_relativa_absoluta[0] - posicao_relativa_absoluta[1]) * (dim_bloco[0] // 2)
    y = (posicao_relativa_absoluta[0] + posicao_relativa_absoluta[1]) * (dim_bloco[1] // 2)
    return (x, y)

def obter_posicao_relativa_absoluta(posicao_relativa_unidimensional, dim_tabuleiro):
    """
    Converte uma posição relativa unidimensional em uma posição relativa bidimensional.
    """
    pos = [dim_tabuleiro[0]-1, dim_tabuleiro[1]-1]  # Inicia com a posição máxima
    dir = [0, -1]
    for _ in range(posicao_relativa_unidimensional):
        pos_alvo = [pos[0] + dir[0], pos[1] + dir[1]]
        # se cair para fora do tabuleiro, rotaciona 90 graus da direcao
        if pos_alvo[0] < 0 or pos_alvo[0] >= dim_tabuleiro[0] or pos_alvo[1] < 0 or pos_alvo[1] >= dim_tabuleiro[1]:
            dir = [dir[1], -dir[0]]
            pos_alvo = [pos[0] + dir[0], pos[1] + dir[1]]
        pos = pos_alvo
    return pos
        