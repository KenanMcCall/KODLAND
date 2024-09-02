import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def yazitura():
    yazi = "Yazı", "Tura"
    money = random.randint(1, 2)
    if money == 1:
        return("Yazı")
    elif money == 2:
        return("Tura")

def emoji():
    emoji = [":crown:", ":eyes:", ":heart:", ":zap:"]
    return random.choice(emoji)
