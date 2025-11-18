import random
import my_module

print(random.randint(1,10))
print(my_module.my_favourite_number)

random_float = round(random.uniform(1, 10), 2)

print(random_float)

if random.randint(0,1) == 0:
  print("heads")
else:
  print("tails")