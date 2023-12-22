import random

# lists for storing required elements for password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# inputs
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Input Validation
if num_letters < 0 or num_symbols < 0 or num_numbers < 0:
    print("Please enter non-negative values for the password components.")
    exit()

# variables
generated_password = ''
num_flag = 0
sym_flag = 0
prev = -1       # symbols or numbers should not get printed consecutively.

# generation
for key in range(0, num_letters + num_numbers + num_symbols):
    defining_num = random.randint(0, 2)
    if defining_num == 0:
        generated_password += letters[random.randint(0, len(letters) - 1)]
    elif prev != 1 and defining_num == 1 and num_flag < num_numbers:
        generated_password += numbers[random.randint(0, len(numbers) - 1)]
        num_flag += 1
        prev = defining_num
    elif prev != 2 and defining_num == 2 and sym_flag < num_symbols:
        generated_password += symbols[random.randint(0, len(symbols) - 1)]
        sym_flag += 1
        prev = defining_num
    else:
        generated_password += letters[random.randint(0, len(letters) - 1)]

# output
print(f" The generated password is: {generated_password}")
