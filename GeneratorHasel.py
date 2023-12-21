import random

losoweZnaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

licznik = -1

for i in losoweZnaki:
    licznik += 1

dlugoscHasla = int(input("Podaj dlugosc hasla: "))
haslo = ""

for i in range(dlugoscHasla):
    haslo += losoweZnaki[random.randint(0, licznik)]

print(haslo)