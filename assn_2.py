# Assignment 2
#
# Implement A star Algorithm for any game search problem.

class Node:
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, o):
        return self.position == o.position


def astar(maze, start, end):

    start_node = Node(position=start)
    end_node = Node(position=end)

    open_list = [start_node]
    closed_list = []

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0

        for idx, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = idx

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_postition in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0),
                              (1, 1), (1, -1), (-1, 1)]:
            node_position = (current_node.position[0] + new_postition[0],
                             current_node.position[1] + new_postition[1])

            if (node_position[0] >= len(maze)) or (node_position[1] >= len(
                    maze[0])) or (node_position[0] < 0) or (node_position[1] <
                                                            0):
                print(node_position)
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            children.append(Node(position=node_position, parent=current_node))

        for child in children:
            for closed in closed_list:
                if child == closed:
                    continue

            child.g = current_node.g + 1
            child.h = (child.position[0] - end_node.position[0])**2 + (
                child.position[1] - end_node.position[1])**2
            child.f = child.g + child.h

            for node in open_list:
                if child == node or child.f > node.f:
                    continue

            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
