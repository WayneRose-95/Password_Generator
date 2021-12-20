import string 
import random 

#TODO: Base code. Refactor this into a function. 

print("Welcome to Password Generator")

length = int(input('Enter the length of your password: '))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols 

temp = random.sample(all,length)

password = "".join(temp)

print(password)