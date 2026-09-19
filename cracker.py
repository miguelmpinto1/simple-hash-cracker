import time
import hashlib


text = str(input("Enter the text to be cracked: "))
algorithm = str(input("Enter the algorithm you want to use: "))

def hash_converter(text, algorithm):
    text_bytes = text.encode('utf-8')
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text_bytes)
    hash_hex = hash_obj.hexdigest()
    return hash_hex 

def load_wordlist(path):
    with open(path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            yield clean_line

def cracker(target_hash, algorithm, candidates):
    cont = 0
    for candidate in candidates:
        cont += 1
        actual_hash = hash_converter(candidate, algorithm)
        if actual_hash == target_hash:
            actual_time = time.time()
            past_time = actual_time - start_time
            print("Found the target hash!")
            print(actual_hash)
            print("Time used:", past_time)
            print("Attempts:", cont)
            break
    
        if(cont % 1000 == 0):
            actual_time = time.time()
            past_time = actual_time - start_time
            print("Attempts so far:", cont)
            print("Past seconds:", past_time)
    else:
        print("Hash not found.")

start_time = time.time()
cracker(hash_converter(text, algorithm), algorithm, load_wordlist("wordlist.txt"))
