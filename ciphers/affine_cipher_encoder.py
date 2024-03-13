import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def affine_cipher_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        return None
    encrypted_text = ''
    for char in text.lower():
        if char in string.ascii_lowercase:
            x = ord(char) - ord('a')
            encrypted_char = chr(((a * x + b) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def generate_affine_variants(text):
    for a in range(1, 26, 2):
        if gcd(a, 26) == 1:
            for b in range(26):
                encrypted_text = affine_cipher_encrypt(text, a, b)
                if encrypted_text:
                    print(f'a={a}, b={b}: {encrypted_text}')

if __name__ == '__main__':
    text = "AQMEQEAOMFWOBEEBRESBZQEXHTFFRBGBBTFHQRFOGRAJOVIXFEROBMFJMFJOVJTQOXFVQQRPLGBQSHVOZVDWQEBRVVJDORBFAEMPXRDQQOEZJMXBZXDMBRFXQBUBGVJMRMMHHBOMHDGEJMWJ"
    generate_affine_variants(text)
