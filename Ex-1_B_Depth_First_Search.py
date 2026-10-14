# To implement depth first search

#DFS for Graph
def dfs_graph():
    graph = {}

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input("Enter node name: ")
        neighbours = input("Enter neighbours of node " + node + ": ").split()
        graph[node] = neighbours

    def is_valid(node):
        return node in graph

    def dfs(current, visited, path):
        if current == goal:
            path.append(current)
            return True

        visited.add(current)

        for neighbour in graph[current]:
            if is_valid(neighbour) and neighbour not in visited:
                if dfs(neighbour, visited, path):
                    path.append(current)
                    return True

        return False

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    visited = set()
    path = []

    if dfs(start, visited, path):
        path.reverse()
        print("\nDFS Path\n")
        for node in path:
            print(node)
    else:
        print("No Path Found")


#DFS for Maze
def dfs_maze():
    maze_size = 6

    start = (0, 0)
    goal = (0, 5)

    obstacles = {(0, 1), (1, 1), (4, 1), (3, 2), (4, 2),
                 (3, 3), (4, 3), (0, 4), (3, 4), (3, 5)}

    def is_valid(x, y):
        return 0 <= x < maze_size and 0 <= y < maze_size and (x, y) not in obstacles

    def dfs(current, visited, path):
        if current == goal:
            path.append(current)
            return True

        visited.add(current)
        x, y = current

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny) and (nx, ny) not in visited:
                if dfs((nx, ny), visited, path):
                    path.append(current)
                    return True

        return False

    visited = set()
    path = []

    if dfs(start, visited, path):
        path.reverse()

        print("\nDFS Path\n")
        for step in path:
            print(step)

        print("\nMaze Representation\n")
        for y in range(maze_size):
            for x in range(maze_size):
                if (x, y) == start:
                    print("S", end=" ")
                elif (x, y) == goal:
                    print("G", end=" ")
                elif (x, y) in obstacles:
                    print("X", end=" ")
                elif (x, y) in path:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No Path Found")


# Main
if __name__ == "__main__":
    print("===== DFS for Graph =====")
    dfs_graph()

    print("\n===== DFS for Maze =====")
    dfs_maze()


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   Enter number of nodes: 4
#   Enter node name: A
#   Enter neighbours of node A: B C
#   Enter node name: B
#   Enter neighbours of node B: D
#   Enter node name: C
#   Enter neighbours of node C:
#   Enter node name: D
#   Enter neighbours of node D:
#   Enter start node: A
#   Enter goal node: D
#
# Output:
#   ===== DFS for Graph =====
#
#   DFS Path
#
#   A
#   B
#   D
#
#   ===== DFS for Maze =====
#
#   DFS Path
#
#   (0, 0)
#   (1, 0)
#   (2, 0)
#   (3, 0)
#   (3, 1)
#   (2, 1)
#   (2, 2)
#   (1, 2)
#   (0, 2)
#   (0, 3)
#   (1, 3)
#   (2, 3)
#   (2, 4)
#   (1, 4)
#   (1, 5)
#   (0, 5)
#
#   Maze Representation
#
#   S * * * . .
#   X X * * X .
#   * * * X X .
#   * * * X X .
#   X * * X . .
#   G * . X . .
