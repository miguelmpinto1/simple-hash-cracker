import time
from hash_utils import hash_converter

def cracker(target_hash, algorithm, candidates):
    cont = 0
    start_time = time.time()
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

