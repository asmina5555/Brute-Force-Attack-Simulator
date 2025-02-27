import itertools
import string
import time

def brute_force_attack(target_password, max_length=4):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(f"Attempt {attempts}: {guess}")
            if guess == target_password:
                print(f"Password found: {guess} in {attempts} attempts")
                return
    print("Password not found")

# Simulating attack on a weak password
brute_force_attack("abc1")
