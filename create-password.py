import string
import random

lower = string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz
upper = string.ascii_uppercase
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
symbol = string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
digits = string.digits
# 0123456789
all_letters = lower + upper + symbol + digits
# print(all_letters)
while True:
    print("choose an option:\n\t1)create a password\n\t2)Exit")
    choice = input("your choice: ")
    if choice == "1":
        length = int(input("Enter the length of the password: "))
        password = "".join(random.sample(all_letters, length))
        print("your password is:", password)
    elif choice == "2":
        break
    else:
        print("your choice is wrong!\n")
