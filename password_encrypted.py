import random

print("Hello, I am a software password manager")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}*;/,._- "

all = lower + upper + number + symbols

length = input("How many characters do you want in the password?\n" + "ps: max 60 characters\n")

if int(length) <= 60:
    password = "".join(random.sample(all, int(length)))
    print("Your password is:\n" + password)
else:
    print("The maximum number of characters I can generate is 60. Please reduce the character count so I can create your password.")
    exit()

encrypt = input("Do you want to encrypt the password?\n")
if encrypt.lower() == "yes":
    password_encrypted = ""
    
    for i in password:
        encrypted_char = chr(ord(i) + 5)
        password_encrypted += encrypted_char
    
    while len(password_encrypted) < 100:
        password_encrypted += random.choice(all)
    
    print(password_encrypted)
