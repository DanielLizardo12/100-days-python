import math

if False:
    new_word = "asdasd"

def is_prime(num):
    if num < 2:
        return False

    for number in range(2, int(math.sqrt(num)) + 1):
        if num % number == 0:
            return False
    return True


print(is_prime(75))