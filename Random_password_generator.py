#importing the necessary modules
import random
import string

#defining the password generator function
def generate_password():

    length=int(input('Enter the desired length of the password : ').strip())

    # check if password length satisfy the minimum length condition
    if length < 4:
        print("Password length must be at least 4!")
        return

    include_uppercase=input('Would you like to include uppercase letters? (yes/no): ').strip().lower()
    include_special = input('Would you like to include special characters? (yes/no): ').strip().lower()
    include_digit = input('Would you like to include digits? (yes/no): ').strip().lower()

    # stores all lowercase letters
    lowercase=string.ascii_lowercase

    # stores all uppercase,special characters and digits if condition is matched
    uppercase=string.ascii_uppercase if include_uppercase=='yes' else ""
    special=string.punctuation if include_special=='yes' else ""
    digits=string.digits if include_digit=='yes' else ""

    #storing all characters
    all_character= lowercase + uppercase + special + digits
    required_char=[]

    #at first randomly picking one character
    if include_uppercase=='yes':
        required_char.append(random.choice(uppercase))

    if include_special=='yes':
        required_char.append(random.choice(special))

    if include_digit=='yes':
        required_char.append(random.choice(digits))

    required_char.append(random.choice(lowercase))
    remaining_length=length-len(required_char)
    password=required_char

    #randomly picking and adding character one by one until required length is matched
    for i in range(remaining_length):
        character=random.choice(all_character)
        password.append(character)

    #shuffling the obtained password
    random.shuffle(password)
    password="".join(password) #converting the password list to string
    print(password)


#calling the generator function
generate_password()