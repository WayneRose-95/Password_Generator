import string 
import random 


class Random_Password:

    def __init__(self):

        self.lower  = string.ascii_lowercase 
        self.upper = string.ascii_uppercase
        self.digits = string.digits
        self.puncutation = string.punctuation
        

    def get_user_input(self):

        '''

        Method to collect the input from the user 

        Returns: 
        self.user_input (int):
        An integer which corresponds to the length of the users' password 

        '''
        # print("Welcome to Password Generator! ")
        self.user_input = int(input("Please enter your password length :"))

        return self.user_input


    def create_the_password(self, password_length : int):

        '''
        Method to create the password using a mixture of characters 

        Parameters: 
        password_length (int): 
        The number of characters which represent the length of the password 

        Returns: 
        letters (str): 
        The users' password as a string 

        '''

        letters = ""
        for letter in range(0,password_length):
            letters += random.choice(self.lower + self.upper + self.digits + self.puncutation)
        print(f'Your new password: {letters}')
        return letters  
        
        

    def choose_again(self):

        '''
        Method to allow the user to re-run the program after choosing their 
        password 

        Returns: 
        True if the user inputs "yes" or "y" 

        False if the user inputs "no" or n" 
        '''

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