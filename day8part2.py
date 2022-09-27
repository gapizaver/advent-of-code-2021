#
# Read input
#
input = []
with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip().split(" | "))

# Split input lines into arrays of digits
lines = []
for line in input:
    lines.append([line[0].split(), line[1].split()])


#
# Decode digits
#

sum_of_numbers = 0
# Go through all entries
for line in lines:
    digits = [set()] * 10       # Sets of segments for digits from 0 to 9
    # Dictionary how signals for segments are mapped
    segments_mapping = {
        "a" : "",
        "b" : "",
        "c" : "",
        "d" : "",
        "e" : "",
        "f" : "",
        "g" : "",
    }

    # Find 1, 4, 7, 8
    for digit in line[0]:
        # 1
        if len(digit) == 2:
            digits[1] = set(digit)
        # 4
        elif len(digit) == 4:
            digits[4] = set(digit)
        # 7
        elif len(digit) == 3:
            digits[7] = set(digit)
        # 8
        elif len(digit) == 7:
            digits[8] = set(digit)
    segments_mapping["a"] = (digits[7] - digits[1]).pop()    # a segment
    
    # Find digit 3 (segments c, f, g are the same as 4 - 3 is only len-5 digit that has 3 same segments as 4)
    for digit in line[0]:
        if len(digit) == 5 and len(set(digit) - digits[1]) == 3:
            digits[3] = set(digit)
            break
    
    # Analyze mapping of the segments
    segments_mapping["b"] = (digits[4] - digits[3]).pop()               # b segment
    segments_mapping["e"] = (digits[8] - digits[3] - digits[4]).pop()   # e segment
    segments_mapping["g"] = (digits[3] - digits[4] - digits[7]).pop()   # g segment
    segments_mapping["d"] = (digits[4] - digits[1] - set(segments_mapping["b"])).pop()    # d segment

    # Find digit 6 & c segment
    for digit in line[0]:
        if len(digit) == 6:
            if len(set(digit) - digits[7]) == 4:
                digits[6] = set(digit)
            elif len(set(digit) - digits[4]) == 2:
                digits[9] = set(digit)

    segments_mapping["c"] = (set("abcdefg") - digits[6]).pop()          # c segment
    segments_mapping["f"] = (digits[1] & digits[6]).pop()          # c segment

    # Compose unknown digits out of segments
    digits[0] = set([segments_mapping["a"], segments_mapping["c"], segments_mapping["f"],
            segments_mapping["g"], segments_mapping["g"], segments_mapping["b"]])
    digits[2] = set([segments_mapping["a"], segments_mapping["c"], segments_mapping["d"],
            segments_mapping["e"], segments_mapping["g"]])
    digits[5] = set([segments_mapping["a"], segments_mapping["b"], segments_mapping["d"],
            segments_mapping["f"], segments_mapping["g"]])
    
    # Compose number in the second part of the input
    for i, digit in enumerate(line[1]):
        true_segments = set()       # The real segments of the digit
        for segment in digit:
            true_segments.add(segments_mapping[segment])
        
        # Find the digit
        for j, digit_to_compare in enumerate(digits):
            if set(digit) == digit_to_compare:      # Digit found (j)
                # Add digit to sum with correct exponent
                sum_of_numbers += j * 10 ** (3 - i)


# Print solution
print("solution:", sum_of_numbers)