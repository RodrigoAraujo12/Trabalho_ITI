def build_shannon_fano_table(symbols):
    if len(symbols) == 1:
        return {symbols[0][0]: ""}

    # Ordenar por frequência
    symbols.sort(key=lambda x: x[1], reverse=True)

    # Encontrar ponto de divisão ideal
    def find_best_split(symbols):
        total = sum(freq for _, freq in symbols)
        cumulative = 0
        best_split = 0
        min_diff = float("inf")

        for i, (_, freq) in enumerate(symbols):
            cumulative += freq
            diff = abs((total - cumulative) - cumulative)  # Diferença entre os grupos

            if diff < min_diff:
                min_diff = diff
                best_split = i

        return best_split

    split_index = find_best_split(symbols)

    # Recursão para os dois grupos
    left = build_shannon_fano_table(symbols[:split_index + 1])
    right = build_shannon_fano_table(symbols[split_index + 1:])

    # Adicionar prefixos 0 e 1
    for symbol in left:
        left[symbol] = "0" + left[symbol]
    for symbol in right:
        right[symbol] = "1" + right[symbol]

    # Combinar as tabelas
    left.update(right)
    return left
