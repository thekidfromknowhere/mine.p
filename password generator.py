#todo los elementos que puede usar
import random
elements=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
password_length=int(input("cuantos caercters quieres?"))
password=""

for i in range(password_length):
    password+=random.choice(elements)
print(password)