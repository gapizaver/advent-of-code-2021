# Read input
fishbox = []
with open("input.txt") as file:
    fishbox = list(map(int, file.read().split(",")))

# Fish categorized by days left until spawning
fish_days_left = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Categorize input fish by days left
for fish in fishbox:
    fish_days_left[fish] += 1

# go through n (256) days of spawning
for i in range(256):
    # Fish become 1 day closer to spawning (logical shift left)
    fish_days_left_new = fish_days_left[1:] + [0]
    # Fish that just spawned reset timer
    fish_days_left_new[6] += fish_days_left[0]
    # Spawn new fish
    fish_days_left_new[8] += fish_days_left[0]

    fish_days_left = fish_days_left_new

# Print number of fish
print(sum(fish_days_left))