import os

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m=26):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt_affine_cipher(text, a, b):
    decrypted_text = ""
    m = 26
    a_inv = mod_inverse(a)
    if a_inv is None:
        raise ValueError("a and m must be disjoint numbers")
    for char in text:
        if char.isalpha():
            shift_amount = b % m
            if char.islower():
                shifted = ord(char) - 97
                decrypted_char = ((a_inv * (shifted - b)) % m) + 97
            elif char.isupper():
                shifted = ord(char) - 65
                decrypted_char = ((a_inv * (shifted - b)) % m) + 65
            decrypted_text += chr(decrypted_char)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == '__main__':
    input_dir = "ciphers"
    output_dir = "affine_decryptions"

    os.makedirs(output_dir, exist_ok=True)

    for task_number in range(1, 7):
        input_filename = f"task{task_number}.txt"
        output_filename = f"task{task_number}_decrypted.txt"

        with open(os.path.join(input_dir, input_filename), "r") as file:
            input_text = file.read()

        with open(os.path.join(output_dir, output_filename), "w") as file:
            for a in range(1, 26):
                if gcd(a, 26) == 1:
                    for b in range(26):
                        try:
                            decrypted_text = decrypt_affine_cipher(input_text, a, b)
                            file.write(f"a={a}, b={b}: {decrypted_text}\n")
                        except ValueError:
                            continue
