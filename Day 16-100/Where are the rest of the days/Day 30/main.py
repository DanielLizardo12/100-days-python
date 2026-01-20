
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
    file.close()
    print("file closed")