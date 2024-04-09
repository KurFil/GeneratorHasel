import random

randomCharacters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

counter = -1

for i in randomCharacters:
    counter += 1

passwordLength = int(input("Enter password length: "))
password = ""

for i in range(passwordLength):
    password += randomCharacters[random.randint(0, counter)]

print("Generated password:", password)
