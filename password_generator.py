import string 
import random 

#TODO: Can this be refactored into a class now? 

def random_password(lower, upper, num, symbols):
    length = int(input('Enter the length of your password:   '))

    all = lower + upper + num + symbols
    temp = random.sample(all, length)
    password = "".join(temp)
    return password 


random_password(string.ascii_lowercase, 
string.ascii_uppercase,
string.digits, 
string.punctuation)