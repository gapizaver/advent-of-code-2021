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
# Points for characters
character_points = {
    "(" : 1,
    "[" : 2,
    "{" : 3,
    "<" : 4,
}

# Complete the legal entries, calculate their score
scores = []
for entry in input:
    stack = []
    illegal = False

    # Fill the stack
    for character in entry:
        if character in opening_characters.values():
            stack.append(character)
        else:
            character_from_stack = stack.pop()

            # Check if closing character illegal -> skip
            if character not in opening_characters.keys() \
                    or opening_characters[character] != character_from_stack:
                illegal = True
                break
    
    if illegal: continue
    
    # Find missing characters and calculate score
    score = 0
    while len(stack) > 0:
        score *= 5
        score += character_points[stack.pop()]
    scores.append(score)        


# Print solution
scores.sort()
print(scores[int(len(scores) / 2)])