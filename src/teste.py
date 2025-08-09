def imprimir_diagonais_secundarias(A):
    linhas = len(A)
    colunas = len(A[0])

    # Começa nas colunas da última para a primeira (linha inicial sempre 0)
    for start_col in range(colunas - 1, -1, -1):
        i, j = 0, start_col
        while i < linhas and j < colunas:
            print(A[i][j], end=", ")
            i += 1
            j += 1

    # Depois começa nas linhas (a partir da segunda linha) com coluna 0
    for start_row in range(1, linhas):
        i, j = start_row, 0
        while i < linhas and j < colunas:
            print(A[i][j], end=", ")
            i += 1
            j += 1

# Exemplo
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

imprimir_diagonais_secundarias(A)
