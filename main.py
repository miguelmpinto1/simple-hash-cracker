from cracker import cracker
from hash_utils import hash_converter
from wordlist_loader import load_wordlist
from bruteforce import bruteforce
import string
import argparse

parser = argparse.ArgumentParser(description="Simple hash cracker")
parser.add_argument("--text", required=True, help="Text to be cracked")
parser.add_argument("--algorithm", required=True, help="Hash algorithm to use (e.g. md5, sha256)")
parser.add_argument("--mode", required=True, choices=["wordlist", "bruteforce"], help="Attack mode")
args = parser.parse_args()

charset = string.ascii_letters + string.digits + string.punctuation
max_size = 3

if(args.mode == "wordlist"):
    cracker(hash_converter(args.text, args.algorithm), args.algorithm, load_wordlist("wordlist.txt"))
elif(args.mode == "bruteforce"):
    cracker(hash_converter(args.text, args.algorithm), args.algorithm, bruteforce(charset, max_size))
