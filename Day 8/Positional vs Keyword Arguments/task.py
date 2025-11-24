# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("daniel", "unknown")
greet_with("unknown", "daniel")
greet_with(location="unknown", name="daniel")

a = "asdasdDD"

print(a.lower())