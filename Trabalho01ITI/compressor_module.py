from shannon_tree import build_shannon_fano_table

# Frequências fornecidas
frequencies = {
    ' ': 17.00,
    'E': 14.63,
    'A': 13.72,
    'O': 10.73,
    'S': 7.81,
    'R': 6.53,
    'I': 6.18,
    'N': 5.05,
    'D': 4.99,
    'M': 4.74,
    'U': 4.63,
    'T': 4.34,
    'C': 3.88,
    'L': 2.78,
    'P': 2.52,
    'V': 1.67,
    'G': 1.30,
    'H': 1.28,
    'Q': 1.20,
    'B': 1.04,
    'F': 1.02,
    'Z': 0.47,
    'J': 0.40,
    'X': 0.27,
    'K': 0.02,
    'W': 0.01,
    'Y': 0.01,
}

def validate_input(text, allowed_chars):
    validated = []
    previous_char = None
    for char in text:
        if char in allowed_chars:
            if char == ' ' and previous_char == ' ':
                continue
            validated.append(char)
            previous_char = char
    return ''.join(validated)

def encode(text, coding_table):
    return ''.join(coding_table[char] for char in text)

def pad_to_bytes(bit_string):
    """Adiciona bits de preenchimento para que a sequência tenha tamanho múltiplo de 8."""
    padding_size = (8 - len(bit_string) % 8) % 8  # Calcula quantos bits faltam para completar o byte
    padded_bit_string = bit_string + '0' * padding_size
    
    return padded_bit_string, padding_size

def shannon_fano_compress(text):
    # Validar entrada
    allowed_chars = set(frequencies.keys())
    text = validate_input(text.upper(), allowed_chars)

    # Construir tabela de codificação
    symbols = [(char, freq) for char, freq in frequencies.items()]
    coding_table = build_shannon_fano_table(symbols)

    # Codificar o texto
    compressed = encode(text, coding_table)

    # Calcular bits de preenchimento para que seja múltiplo de 8
    padding_size = (8 - len(compressed) % 8) % 8  # Garante que padding_size fique entre 0 e 7
    compressed += "0" * padding_size  # Adiciona os bits extras ao final

    ## return compressed, coding_table
    return compressed, coding_table, padding_size
