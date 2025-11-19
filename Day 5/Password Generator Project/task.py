import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password = ""

def add_chars_to_password(char_list, number_of_chars):
  response = ""
  for _ in range(number_of_chars):
    response += random.choice(char_list)

  return response


password += add_chars_to_password(letters, nr_letters)
password += add_chars_to_password(numbers, nr_numbers)
password += add_chars_to_password(symbols, nr_symbols)

print(''.join(random.sample(password, len(password))))
print(''.join(random.sample(password, len(password))))
print(''.join(random.sample(password, len(password))))