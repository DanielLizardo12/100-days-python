print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))

    bill = 0

    if age < 12:
      print("pay $5 dlls")
    elif age >= 12 and age <= 18:
      print("pay $7 dlls")
    else:
      print("pay $12 dlls")

else:
    print("Sorry you have to grow taller before you can ride.")
