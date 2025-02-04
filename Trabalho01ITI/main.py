from compressor_module import shannon_fano_compress
from descompressor import decode


if __name__ == "__main__":
    input_text = "Exemplo de texto para compressao Shannon-Fano!"
    
    # Compressão
    compressed_text, table = shannon_fano_compress(input_text)
    print("Texto Original:", input_text)
    print("Texto Comprimido:", compressed_text)
    print("Tabela de Codificação:")
    for char, code in table.items():
        print(f"{char}: {code}")

    # Descompressão
    decompressed_text = decode(compressed_text, table)
    print("Texto Descomprimido:", decompressed_text)

    # Cálculo da razão de compressão
    tamanho_original = len(input_text) * 8  # Cada caractere tem 8 bits no texto original
    tamanho_comprimido = len(compressed_text)  # Já está em bits
    razão_compressao = tamanho_original / tamanho_comprimido
    print(f"Razão de Compressão: {razão_compressao:.2f}")
