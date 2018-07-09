#coding=utf-8
"""Breadth-First Search"""
# Breadth-First searches are a way to find if two nodes in a graph are connected.
# Graphs are represented as follows:
# {
# "A": ["B", "C"]
# "B": ["A", "C"]
# "C": ["A", "B"]
# }

# Becomes:
# (A) --
#  |    \
#  |   (B)
# (C) -/

# Basically, the nodes are stored in a dictionary, with each node equalling a list of the connected nodes.

# The example graph look like so:
# +---+A+
# +     +---+
# B+--+     C
# +   |     +
# +   |     +
# D   +----+E
# +     +---+
# +---+F+


example_graph = {
"A": ["B", "C"],
"B": ["A", "E", "D"],
"C": ["A", "E"],
"D": ["B", "F"],
"E": ["B", "C", "F"],
"F": ["D", "E"]
}

def difference(ls1, ls2):
    new_list = []

    for item in ls1:
        if not item in ls2:
            new_list.append(item)

    return new_list

def breadth_first(graph, root):
    queue = [root]
    visited = []

    while queue:
        current = queue.pop(0)

        if current not in visited:
            visited.append(current)
            queue += difference(graph[current], visited)


    return visited

print(breadth_first(example_graph, "A"))
