# Implementation of A* Search Algorithm

import heapq

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g            # Cost to reach this node
        self.h = h            # Heuristic cost to the goal
        self.f = g + h        # Total cost

    def __lt__(self, other):
        return self.f < other.f


def heuristic(state, goal):
    """Manhattan distance."""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def neighbors(state):
    """Adjacent grid cells (right, left, up, down), each with cost 1."""
    x, y = state
    return [((x + 1, y), 1), ((x - 1, y), 1), ((x, y + 1), 1), ((x, y - 1), 1)]


def a_star_search(start, goal):
    open_list = [Node(start, None, 0, heuristic(start, goal))]
    closed_list = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        closed_list.add(current.state)

        for neighbor, cost in neighbors(current.state):
            if neighbor in closed_list:
                continue

            g = current.g + cost
            node = Node(neighbor, current, g, heuristic(neighbor, goal))

            if not any(n.state == neighbor and n.f <= node.f for n in open_list):
                heapq.heappush(open_list, node)

    return None


if __name__ == "__main__":
    start = (0, 0)
    goal = (3, 3)

    path = a_star_search(start, goal)
    print("Path from start to goal:", path)


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None (start = (0, 0) and goal = (3, 3) are fixed in the code)
#
# Output:
#   Path from start to goal: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
