import hashlib

def hash_converter(text, algorithm):
    text_bytes = text.encode('utf-8')
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(text_bytes)
    hash_hex = hash_obj.hexdigest()
    return hash_hex 