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
    media_bits_por_simbolo = len(compressed_text) / len(input_text.replace(" ", "")) 
    razão_compressao = 5 / media_bits_por_simbolo
    print(f"Razão de Compressão: {razão_compressao:.2f}")
