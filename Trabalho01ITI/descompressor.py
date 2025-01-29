def decode(encoded_text, coding_table):
    # Inverter a tabela de codificação
    decoding_table = {v: k for k, v in coding_table.items()}
    
    decoded_text = []
    buffer = ""
    for bit in encoded_text:
        buffer += bit
        if buffer in decoding_table:
            decoded_text.append(decoding_table[buffer])
            buffer = ""

    return ''.join(decoded_text)
