def calcular_posicao_absoluta(posicao_relativa, dim_tabuleiro, dim_bloco):
    # Calcular o perímetro total
    perimetro_total = 2 * dim_tabuleiro[0] + 2 * dim_tabuleiro[1]

    # Normalizar a posição relativa
    pos_norm = posicao_relativa % perimetro_total

    # Determinar em qual lado do retângulo estamos
    if pos_norm < dim_tabuleiro[0]:
        # Lado inferior (da esquerda para a direita)
        x = pos_norm * dim_bloco[0]
        y = dim_tabuleiro[1] * dim_bloco[1]
    elif pos_norm < dim_tabuleiro[0] + dim_tabuleiro[1]:
        # Lado direito (de baixo para cima)
        x = dim_tabuleiro[0] * dim_bloco[0]
        y = (dim_tabuleiro[1] - (pos_norm - dim_tabuleiro[0])) * dim_bloco[1]
    elif pos_norm < 2 * dim_tabuleiro[0] + dim_tabuleiro[1]:
        # Lado superior (da direita para a esquerda)
        x = (dim_tabuleiro[0] - (pos_norm - dim_tabuleiro[0] - dim_tabuleiro[1])) * dim_bloco[0]
        y = 0
    else:
        # Lado esquerdo (de cima para baixo)
        x = 0
        y = (pos_norm - 2 * dim_tabuleiro[0] - dim_tabuleiro[1]) * dim_bloco[1]

    # Ajustar para que o primeiro ponto esteja no centro da parte inferior
    centro_x = (dim_tabuleiro[0] * dim_bloco[0]) // 2
    x_absoluto = x - centro_x + centro_x
    y_absoluto = y

    return (x_absoluto, y_absoluto)