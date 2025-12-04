from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)