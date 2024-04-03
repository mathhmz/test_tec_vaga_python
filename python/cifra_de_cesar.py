if __name__ == '__main__':
    
    def decode_caesar_cipher(cipher, shift):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decoded = ''
    
        for char in cipher:
            if char in alphabet:
                og_index = (alphabet.index(char) - shift) % 26
                decoded += alphabet[og_index]
            else:
                decoded += char
    
        return decoded
    
    #Foi necessario avaliar a quantidade de casos de teste
    n = int(input())
    
    for _ in range(n):
        encoded_message = input()
        shift = int(input())
    
        decoded_message = decode_caesar_cipher(encoded_message, shift)
        print(decoded_message)