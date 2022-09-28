import collections

# Read input
cave_connections = collections.defaultdict(set)
with open("input2.txt") as file:
    for line in file:
        # Add cave to cave_connections if not yet present
        # Add cave connection
        connection = line.rstrip().split("-")
        cave_connections[connection[0]].add(connection[1])
        cave_connections[connection[1]].add(connection[0])


# Already visited caves
visited = set()

# Count number of paths
def count_paths(node):
    # End reached
    if node == "end":
        return 1

    # If small cave and visited -> cancel search
    global visited
    if node.islower():
        if node in visited:
            return 0
        else:
            visited.add(node)

    # Find number of paths from this node
    num_of_paths_from_node = 0
    for node_connection in cave_connections[node]:
        if node_connection == "start":
            continue
        num_of_paths_from_node += count_paths(node_connection)
    
    visited.discard(node)
    return num_of_paths_from_node

# Start search with "start"
print("Number of paths through the cave system that visit small caves at most once:",\
        count_paths("start"))
