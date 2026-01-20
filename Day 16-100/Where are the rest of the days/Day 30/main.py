
try:
    file = open('data.txt')
    dictionary = {"key": "value"}
    print(dictionary["key"])
except FileNotFoundError:
    file = open('data.txt', 'w')
    file.write("something")
except KeyError as e:
    print(f"key error: {e}")
else:
    content = file.read()
    print(content)
finally:
    #raise KeyError("this is an error i created")
    print("finally")

heigth = float(input("Height in metres: "))
weight = float(input("Weight in pounds: "))

if heigth > 3:
    raise ValueError("Height is greater than 3")
raise I

bmi = weight / (heigth * heigth)