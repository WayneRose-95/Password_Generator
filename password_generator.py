import string 
import random 

# TODO: clean up the variable names. 

class Random_Password:

    def __init__(self):

        self.lower  = string.ascii_lowercase 
        self.upper = string.ascii_uppercase
        self.digits = string.digits
        self.puncutation = string.punctuation
        

    def get_user_input(self):
        # print("Welcome to Password Generator! ")
        self.user_input = int(input("Please enter your password length :"))

        return self.user_input


    def create_the_password(self, password_length : int):
        letters = ""
        for letter in range(0,password_length):
            letters += random.choice(self.lower + self.upper + self.digits + self.puncutation)
        print(f'Your new password: {letters}')
        return letters  
        
        

    def choose_again(self):
        restart = input("Would you like to restart this program? Yes or No?")
        if restart == "yes" or restart == "y":
            new_password.create_the_password(new_password.get_user_input()) 
            return True 

        if restart == "n" or restart == "no":
            print ("Enjoy your new password :)" )
            return False 
        
   

if __name__ == "__main__":
    new_password = Random_Password()
    new_password.create_the_password(new_password.get_user_input())

    while new_password.choose_again() is True:
        print(f'................................................')