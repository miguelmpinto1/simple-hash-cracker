def load_wordlist(path):
    with open(path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            yield clean_line