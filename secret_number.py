def secret_normal(secret_number):
    for i in range(0, secret_number + 1):
        if i == secret_number: print(f"Found {secret_number} in {i} guesses!"); return
    print(f"Couldn't find {secret_number}")

def secret_evens(secret_number):
    i = 0
    guesses = 0
    while i <= secret_number:
        if i == secret_number: print(f"Found {secret_number} in {guesses} guesses!"); return
        i += 2
        guesses += 1
    print(f"Couldn't find {secret_number}")

secret_normal(73)
secret_evens(74)
