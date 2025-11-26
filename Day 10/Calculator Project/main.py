from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def print_operations():
    for key in calc_dict:
        print(key)

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
use_result = False

while True:
    if use_result:
        first_number = prev_result
    else:
        first_number = float(input("What is the first number?: "))

    print_operations()
    operation = input("type an operation: ")
    second_number = float(input("type the second number: "))
    prev_result = calc_dict[operation](first_number, second_number)
    print(f"The result of {first_number} {operation} {second_number} "
          f"is {prev_result}")

    use_result = input("use prev result? (y/n): ") == "y"




