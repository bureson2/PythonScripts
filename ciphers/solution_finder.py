import os

# folder_path = 'caesar_dcryptions'
folder_path = 'affine_decryptions'


common_bigrams = set(['th', 'he', 'in', 'er', 'an', 're', 'nd', 'at', 'on', 'nt', 'ha', 'es', 'st', 'en', 'ed', 'to', 'it', 'ou', 'ea', 'hi'])
common_trigrams = set(['THE', 'AND', 'THA', 'ENT', 'ION', 'TIO', 'FOR', 'NDE', 'HAS', 'NCE', 'EDT', 'TIS', 'OFT', 'STH', 'MEN'])

def has_common_bigrams(text, bigrams):
    for i in range(len(text) - 1):
        if text[i:i+2] in bigrams:
            return True
    return False

def has_common_trigrams(text, trigrams):
    for i in range(len(text) - 2):
        if text[i:i+3] in trigrams:
            return True
    return False

def find_potential_solutions(folder_path, common_bigrams):
    potential_solutions = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r') as file:
            for line in file:
                # if has_common_bigrams(line, common_bigrams):
                if has_common_trigrams(line, common_trigrams):
                    potential_solutions.append((filename, line.strip()))
    return potential_solutions

if __name__ == '__main__':
    potential_solutions = find_potential_solutions(folder_path, common_bigrams)
    for filename, line in potential_solutions:
        print(f"{filename}: {line}")
