import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Uzunluk seçiniz: "))
sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)
