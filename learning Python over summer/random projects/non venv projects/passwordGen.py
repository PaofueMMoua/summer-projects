# password generator. 
# make configurable
# minimum and max length of password
# choose a random number
# user tells if to include or exclude uppercase lowercase nums and symbols
# validate to check if it meets reqs
# tell how strong the password is and why it is strong or weak.
#  password given or generated 

# password generator

# imports
import random
import string
import math
import time

class Password:
    def __init__(self, minimum, maximum, upper, lower, nums, symbol):
        try:
            self.min = int(minimum)
        except ValueError:
            raise ValueError("Minimum number must be an integer.")
        
        self.max = maximum
        
        try:
            self.max = int(maximum)
        except ValueError:
            raise ValueError("Maximum number must be an integer.")
        
        self.upper = bool(upper)
        self.lower = bool(lower)
        self.nums = bool(nums)
        self.symbol = bool(symbol)
        self.characters = self._build_character_set()
        self.gen_number = 0
    
# the generate function is to generate a password using the information established within the initialization function.
    
    def generate(self):
        self.gen_number += 1
        # this if statement is checking that the minimum and maximum are greater than the amount of character requirements
        
        if self.min < sum([self.lower, self.upper, self.nums, self.symbol]) and self.max < sum([self.lower, self.upper, self.nums, self.symbol]):
            raise ValueError("your minimum and max must be greater than the amount of character requirements")

        elif self.min < sum([self.lower, self.upper, self.nums, self.symbol]):
            self.min = sum([self.lower, self.upper, self.nums, self.symbol])

        length = random.randint(self.min, self.max)
        password =  ''.join(random.choice(self.characters) for _ in range(length))

        # this if statement is checking if you put hte password through the function of is valid password and it returns true then it would return the generated password else it would generate a new password.

        if self.is_valid_password(password) == True:
            return password

        else:
            self.generate()
        # Password.check(self)
        
        # this function is checking if the user decides to include lowercase letters, uppercase letters, numbers, and symbols. and adds them to the avaliable character set.
        
    def _build_character_set(self):
        char_set = ""
        char_nums = 0
        
        # checking if the user has selected the options and if they did then the character set is updated to include the character options.
        
        if self.lower:
            char_set += string.ascii_lowercase
            char_nums +=1 
        
        if self.upper:
            char_set += string.ascii_uppercase
            char_nums +=1 
        
        if self.nums:
            char_set += string.digits
            char_nums +=1 
        
        if self.symbol:
            char_set += string.punctuation
            char_nums +=1 
        
        if not char_set:
            raise ValueError("At least one character type must be selected.")
        
        if self.min < char_nums and self.max < char_nums:
            raise ValueError('Password needs to contain at least the amount of character types you have selected.')
        
        return char_set
        
# The function is_valid_password is checking if the input called password contains a character type if the character type is selected.
        
    def is_valid_password(self, password):
        
        if self.lower and not any(c.islower() for c in password):
            return False
        if self.upper and not any(c.isupper() for c in password):
            return False
        if self.nums and not any(c.isdigit() for c in password):
            return False
        if self.symbol and not any(c in string.punctuation for c in password):
            return False
        return True

        
# function for the user to input a password and to check how strong the password is.
        
def analyze_user_password(password):
    password_length = len(password)
    char_set = ''
    weak = "Your password's weaknesses are because you dont have "
    strong = "Your password's strengths include having "
    
    if any(character in string.ascii_lowercase for character in password):
        char_set += string.ascii_lowercase
        strong += "lowercase characters "
    else:
        weak += "lowercase characters "

    if any(character in string.ascii_uppercase for character in password):
        char_set += string.ascii_uppercase
        strong += "uppercase characters "
    else:
        weak += "uppercase characters "

    if any(character in string.digits for character in password):
        char_set += string.digits
        strong += "numbers "
    else:
        weak += "numbers "

    if any(character in string.punctuation for character in password):
        char_set += string.punctuation
        strong += "symbols "
    else:
        weak += "symbols "

    if len(password) > 8:
        strong += "longer than 8 characters "
    else:
        weak += "shorter than 8 characters "

# using entropy to find the password strength.
    # more specifically doing a log base 2 with x being the total possible characters and with the 

    entropy = password_length * math.log2(len(char_set))
    
    if entropy >= 128:
        return f"Very Strong \n {weak} \n {strong} \n and you scored a {entropy} bits of entropy"
    
    elif entropy >= 96:
        return f"Strong \n {weak} \n {strong} \n and you scored a {entropy} bits of entropy"
    
    elif entropy >= 64:
        return f"Moderate \n {weak} \n {strong} \n and you scored a {entropy} bits of entropy"
    
    elif entropy >= 32:
        return f"Weak \n {weak} \n {strong} \n and you scored a {entropy} bits of entropy"
    
    else:
        return f"Very Weak \n {weak} \n {strong} \n and you scored a {entropy} bits of entropy"

start_time = time.time()
for i in range(1000000):
    _ = i * 2

upper = True
lower = True
nums = True
symbol = True

result = Password(8,22,upper, lower, nums,symbol)
print(result.generate())
# print(result.get_password_strength())
# print(analyze_user_password(input('Password : \n')))
print()
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the runtime
print(f"Runtime: {elapsed_time:.4f} seconds")