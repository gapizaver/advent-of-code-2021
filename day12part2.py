import collections

# Read input
cave_connections = collections.defaultdict(set)
with open("input.txt") as file:
    for line in file:
        # Add cave to cave_connections if not yet present
        # Add cave connection
        connection = line.rstrip().split("-")
        cave_connections[connection[0]].add(connection[1])
        cave_connections[connection[1]].add(connection[0])


# Already visited caves
visited = []
# Flag if small cave is visited twice
two_small_caves_visited = False

# Count number of paths
def count_paths(node):
    global visited
    global two_small_caves_visited

    # End reached
    if node == "end":
        return 1

    # Handle if small cave and already visited
    if node.islower():
        if two_small_caves_visited and visited.count(node) >= 1:
            return 0
        if not two_small_caves_visited:
            if visited.count(node) >= 2:
                return 0
            elif visited.count(node) == 1:
                two_small_caves_visited = True

    visited.append(node)        # Visit node

    # Find number of paths from this node
    num_of_paths_from_node = 0
    for node_connection in cave_connections[node]:
        if node_connection == "start":
            continue
        num_of_paths_from_node += count_paths(node_connection)
    
    # Leave node
    left_node = visited.pop()
    # If left node was small cave on second visit, reset flag
    if left_node.islower() and visited.count(left_node) > 0:
        two_small_caves_visited = False

    return num_of_paths_from_node

# Start search with "start"
print("Number of paths through the cave system that visit small caves at most twice:",\
        count_paths("start"))
