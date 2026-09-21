# Simple Hash Cracker
Educational hash cracker implemented in Python with bruteforce and wordlist attacks.

## Features
- Dictionary attack using wordlist
- Brute-force attack with configurable charset and max length
- Support for any hash algorithm available in Python's `hashlib`
- Real-time progress reporting (attempts and elapsed time)
- Configurable via command-line arguments

## Usage
The cracker is run through `main.py`, using command-line arguments to configure the attack.

**Dictionary attack:**
```bash
python main.py --text test --algorithm md5 --mode wordlist --wordlist wordlist.txt
```

**Brute-force attack:**
```bash
python main.py --text test --algorithm md5 --mode bruteforce --max-size 4
```

### Available arguments

| Argument       | Required | Default        | Description                                      |
|----------------|----------|----------------|---------------------------------------------------|
| `--text`       | Yes      | —              | The plaintext to hash and attempt to crack        |
| `--algorithm`  | Yes      | —              | Hash algorithm to use (e.g. `md5`, `sha1`, `sha256`) |
| `--mode`       | Yes      | —              | Attack mode: `wordlist` or `bruteforce`           |
| `--wordlist`   | No       | `wordlist.txt` | Path to the wordlist file (used in `wordlist` mode) |
| `--max-size`   | No       | `3`            | Maximum candidate length (used in `bruteforce` mode) |

## Libraries Used
- hashlib -> for hash converting
- itertools -> for combination generation
- argparse -> for CLI
- string -> for charset
- time -> for cracking time counter
  
## Project structure
```
simple-hash-cracker/
├── main.py              # CLI argument parsing and orchestration
├── cracker.py           # Core cracking loop (dictionary & bruteforce)
├── hash_utils.py        # Hash generation using hashlib
├── wordlist_loader.py   # Memory-efficient wordlist reader
├── bruteforce.py        # Combination generator
├── wordlist.txt         # Sample wordlist for testing
├── .gitignore
└── README.md
```

## Installation

### Requirements
- Python 3.8 or higher (no external dependencies — only the standard library is used)

### Clone the repository
```bash
git clone https://github.com/miguelmpinto1/simple-hash-cracker.git
cd simple-hash-cracker
```

## Known Limitations
- Brute-force attacks scale exponentially — impractical for long passwords or large charsets
- No support for salted hashes
- Performance is limited by pure Python execution (no multiprocessing yet)
  
## Hashes Consideration
_Fast hashes (like MD5 or SHA-256) are not recommended for storing passwords._ Their speed, which is ideal for data integrity checks, becomes a weakness against attackers and allows millions of guesses per second in brute-force or dictionary attacks.

Modern algorithms like bcrypt, scrypt, and Argon2 resolve this by being intentionally slow and memory-intensive, making large-scale password cracking significantly more expensive for attackers.

> *This tool is only for educational purposes in controlled or approved environments.
