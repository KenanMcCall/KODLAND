import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifrenizin uzunluğunu seçiniz: "))
uzunluk2 = int(input("İkinci şifrenizin uzunluğunu seçiniz: "))
sifre = ""
sifre2 = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)
    sifre2 += random.choice(karakterler)

for i in range(uzunluk2):
    sifre2 += random.choice(karakterler)

print("Şifre:", sifre, "Şifre 2:", sifre2)
