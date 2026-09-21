from cracker import cracker
from hash_utils import hash_converter
from wordlist_loader import load_wordlist
from bruteforce import bruteforce
import string
import argparse

parser = argparse.ArgumentParser(description="Simple hash cracker")
parser.add_argument("--text", required=True, help="Text to be cracked")
parser.add_argument("--max-size", type=int, default=3, help="Maximum length for bruteforce attempts")
parser.add_argument("--algorithm", required=True, help="Hash algorithm to use (e.g. md5, sha256)")
parser.add_argument("--mode", required=True, choices=["wordlist", "bruteforce"], help="Attack mode")
parser.add_argument("--wordlist", default="wordlist.txt", help="Path to the wordlist file")
args = parser.parse_args()

charset = string.ascii_letters + string.digits + string.punctuation

try:
    if(args.mode == "wordlist"):
        cracker(hash_converter(args.text, args.algorithm), args.algorithm, load_wordlist(args.wordlist))
    elif(args.mode == "bruteforce"):
        cracker(hash_converter(args.text, args.algorithm), args.algorithm, bruteforce(charset, args.max_size))
except ValueError:
    print("Invalid algorithm.")
except FileNotFoundError:
    print("Wordlist file not found.")