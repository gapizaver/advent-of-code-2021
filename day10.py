# Read input
input = []
with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

# Opening characters from closing characters
opening_characters = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}
# Points for closing characters
character_points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
}

# Find illegal characters
error_score = 0
for entry in input:
    stack = []

    for character in entry:
        if character in opening_characters.values():
            stack.append(character)
        else:
            character_from_stack = stack.pop()

            # Check if closing character illegal
            if character not in opening_characters.keys() \
                    or opening_characters[character] != character_from_stack:
                error_score += character_points[character]
                break


# Print solution
print(error_score)