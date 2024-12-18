from maze import *
from exception import *
from stack import *

class PacMan:
    def __init__(self, grid: Maze) -> None:
        """
        Initialize the PacMan navigator with the given maze.

        Args:
            grid (Maze): An instance of the Maze class representing the grid layout.
        """
        self.navigator_maze = grid.grid_representation  # Grid representation of the maze
        self.rows = grid._m  # Number of rows in the maze
        self.columns = grid._n  # Number of columns in the maze

    def find_path(self, start: tuple, end: tuple) -> list:
        """
        Find a path from the start position to the end position in the maze.

        Args:
            start (tuple): Starting coordinates (row, column).
            end (tuple): Ending coordinates (row, column).

        Returns:
            list: A list of coordinate pairs representing the path from start to end.

        Raises:
            PathNotFoundException: If no path is found or if the start/end points are invalid.
        """
        # Check if the start or end positions are blocked
        if (self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1):
            raise PathNotFoundException

        # Initialize the visited grid
        visited = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

        # Stack to store the path
        coords = Stack()
        curr = list(start)  # Current position
        answer = curr[:]
        coords.push(tuple(answer))

        # Mark the start position as visited
        visited[curr[0]][curr[1]] = 1

        # If the start and end positions are the same
        if start == end:
            return coords.array

        # Perform depth-first search using the stack
        while curr != list(end):
            if not coords.isEmpty() and list(coords.top()) != curr:
                coords.push(tuple(curr))

            # Try moving left
            if curr[1] > 0 and not visited[curr[0]][curr[1] - 1] and not self.navigator_maze[curr[0]][curr[1] - 1]:
                curr[1] -= 1
                visited[curr[0]][curr[1]] = 1

            # Try moving down
            elif curr[0] < self.rows - 1 and not visited[curr[0] + 1][curr[1]] and not self.navigator_maze[curr[0] + 1][curr[1]]:
                curr[0] += 1
                visited[curr[0]][curr[1]] = 1

            # Try moving up
            elif curr[0] > 0 and not visited[curr[0] - 1][curr[1]] and not self.navigator_maze[curr[0] - 1][curr[1]]:
                curr[0] -= 1
                visited[curr[0]][curr[1]] = 1

            # Try moving right
            elif curr[1] < self.columns - 1 and not visited[curr[0]][curr[1] + 1] and not self.navigator_maze[curr[0]][curr[1] + 1]:
                curr[1] += 1
                visited[curr[0]][curr[1]] = 1

            # Backtrack if no move is possible
            else:
                coords.pop()
                if coords.isEmpty():
                    raise PathNotFoundException
                curr = list(coords.top())

        coords.push(end)

        # Return the path if successfully found
        if not coords.isEmpty():
            return coords.array

        # Raise exception if no path exists
        raise PathNotFoundException
