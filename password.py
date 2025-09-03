import random

length = int(input("Enter length of the password: "))
char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-_=+[]{}|()`~;:',<.>/?"

password_list = []

for i in range(length):
    password_list.append(random.choice(char))

password = ''.join(password_list)
print("Random Password:", password)