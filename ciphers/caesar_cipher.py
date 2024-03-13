import os

def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted = ord(char) - shift_amount
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                shifted = ord(char) - shift_amount
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == '__main__':
    input_dir = "ciphers"
    output_dir = "caesar_decryptions"

    os.makedirs(output_dir, exist_ok=True)

    for task_number in range(1, 7):
        input_filename = f"task{task_number}.txt"
        output_filename = f"task{task_number}_decrypted.txt"

        with open(os.path.join(input_dir, input_filename), "r") as file:
            input_text = file.read()

        with open(os.path.join(output_dir, output_filename), "w") as file:
            for i in range(26):
                decrypted_text = decrypt_caesar_cipher(input_text, i)
                file.write(f"S {i}: {decrypted_text}\n")
