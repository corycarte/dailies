"""
    A Star Pathfinding algorithm.
"""

class Node():
    """
    Node class for A* pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
def astar(maze, start, end):
    """
        Returns a list of tuples as a path from
        start to end
    """

    # Create start and end nodes
    start_node = Node(None, start)
    end_node   = Node(None, end)

    # initialize open and closed lists
    open_list = []
    closed_list = []

    # Add start_node to open_list
    open_list.append(start_node)

    # Loop until the end is found
    while len(open_list) > 0:
        # Get current node
        curr_node = open_list[0]
        curr_index = 0

        for index, item in enumerate(open_list):
            if item.f < curr_node.f:
                curr_node = item
                curr_index = index

        # Pop current off open_list, add to closed_list
        open_list.pop(curr_index)
        closed_list.append(curr_node)

        # Goal found
        if curr_node == end_node:
            path = []
            curr = curr_node
            while curr:
                path.append(curr)
                curr = curr.parent

            return path[::-1] # Return reserved path list

        # Generate children
        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # adjacent squares
            # Get node positioin
            node_position = (curr_node.position[0] + new_position[0], curr_node.position[1] + new_position[1])

            # Bound checks
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new child and append
            new_node = Node(curr_node, node_position)
            children.append(new_node)

        # Loop through children
        for child in children:
            # child is in closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create f, g, and h values
            child.g = curr_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # If child is in open_list
            for open_child in open_list:
                if child == open_child and child.g > open_child.g:
                    continue

            # Add child to open_list
            open_list.append(child)
