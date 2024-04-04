import random

def generate_password(pass_length, complexity):
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    
    if complexity == 'strong':
        characters = small_letters + capital_letters + numbers
    elif complexity == 'medium':
        characters = small_letters + capital_letters + numbers
    else:
        characters = small_letters + numbers

    generated_password = ''.join(random.choice(characters) for i in range(pass_length))
    return generated_password

pass_length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity (weak, medium, or strong): ").lower()

password = generate_password(pass_length, complexity)
print("The Generated password is:", password)