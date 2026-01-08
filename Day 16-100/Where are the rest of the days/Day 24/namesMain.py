letter_template = open('input/letters/starting_letter.txt').read()

names = open("input/names/invited_names.txt").read()

path_for_new_files = "output/ReadyToSend/"
for name in names.split("\n"):
    with open(path_for_new_files + name + ".txt", "w") as file:
        file.write(letter_template.replace("[name]", name))

