password = input("Input Password: ")

password_length = len(password)

has_lowercase = False
has_uppercase = False
has_digit = False

if password_length < 8:
    print("Password must be at least 8 characters!")
    exit()

for i in range(0, password_length):
    if password[i].islower():
        has_lowercase = True
    if password[i].isupper():
        has_uppercase = True
    if password[i].isdigit():
        has_digit = True

if has_lowercase == False:
    print("Password must have at least one lowercase letter!")
    exit()

if has_uppercase == False:
    print("Password must have at least one uppercase letter!")
    exit()

if has_digit == False:
    print("Password must have at least one digit!")
    exit()

if has_lowercase == True and has_uppercase == True and has_digit == True:
    print(f"Password {password} successfully added!")
