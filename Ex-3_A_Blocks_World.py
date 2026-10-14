#IMPLEMENTATION OF BLOCKS WORLD PROGRAM

# Each stack is a list written from bottom to top, e.g. [2, 1, 0] means
# block 2 is on the table, block 1 is on block 2, block 0 is on block 1.

class BlocksWorld:
    def __init__(self, num_blocks):
        # Every block starts on the table in its own stack
        self.stacks = [[block] for block in range(num_blocks)]

    def display_state(self):
        for i, stack in enumerate(self.stacks, start=1):
            print(f"  Stack {i} (bottom -> top): {stack}")

    def find_stack(self, block):
        """Return the stack that contains the block."""
        for stack in self.stacks:
            if block in stack:
                return stack
        return None

    def is_clear(self, block):
        """A block is clear if nothing is on top of it."""
        stack = self.find_stack(block)
        return stack is not None and stack[-1] == block

    def move(self, block, destination):
        """Move a block onto another block, or onto the table ('table')."""
        if self.find_stack(block) is None:
            print(f"Invalid block {block}.")
            return False

        if not self.is_clear(block):
            print(f"Cannot move block {block}: it is not clear.")
            return False

        if destination == "table":
            print(f"Move block {block} onto the table")
            self.find_stack(block).remove(block)
            self.stacks.append([block])
        else:
            if self.find_stack(destination) is None or destination == block:
                print(f"Invalid destination {destination}.")
                return False
            if not self.is_clear(destination):
                print(f"Cannot place block {block} on {destination}: "
                      f"{destination} is not clear.")
                return False
            print(f"Move block {block} onto block {destination}")
            self.find_stack(block).remove(block)
            self.find_stack(destination).append(block)

        # Remove stacks that became empty
        self.stacks = [s for s in self.stacks if s]
        self.display_state()
        return True

    def is_goal(self, goal):
        """Check whether the current state matches the goal configuration."""
        return sorted(self.stacks) == sorted(goal)


def main():
    world = BlocksWorld(3)

    # Goal: block 0 on block 1, block 1 on block 2, block 2 on the table
    goal = [[2, 1, 0]]

    print("Initial state:")
    world.display_state()

    print("\nGoal state:")
    for i, stack in enumerate(goal, start=1):
        print(f"  Stack {i} (bottom -> top): {stack}")

    print("\nPerforming moves:\n")
    world.move(1, 2)       # block 1 onto block 2
    print()
    world.move(0, 1)       # block 0 onto block 1
    print()
    world.move(2, 0)       # invalid: block 2 is not clear

    print()
    if world.is_goal(goal):
        print("Goal state reached.")
    else:
        print("Goal state not reached.")


if __name__ == "__main__":
    main()


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None (number of blocks, goal and moves are fixed in the code)
#
# Output:
#   Initial state:
#     Stack 1 (bottom -> top): [0]
#     Stack 2 (bottom -> top): [1]
#     Stack 3 (bottom -> top): [2]
#
#   Goal state:
#     Stack 1 (bottom -> top): [2, 1, 0]
#
#   Performing moves:
#
#   Move block 1 onto block 2
#     Stack 1 (bottom -> top): [0]
#     Stack 2 (bottom -> top): [2, 1]
#
#   Move block 0 onto block 1
#     Stack 1 (bottom -> top): [2, 1, 0]
#
#   Cannot move block 2: it is not clear.
#
#   Goal state reached.
