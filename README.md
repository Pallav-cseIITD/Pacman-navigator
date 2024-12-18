# PacMan-Navigator

## Project Overview
Pac-Man is trapped in a haunted maze and needs help navigating to his favorite destination while avoiding ghosts. This project implements a navigation system for Pac-Man using a 2D grid representation of the maze and stack-based traversal.

The solution ensures Pac-Man finds a path from the start to the destination (if one exists) while avoiding blocked cells occupied by ghosts. The implementation follows the constraints and requirements outlined in the assignment.

---

## Features

1. **Maze Representation**:
   - Vacant cells are represented as `0`.
   - Blocked cells (ghosts) are represented as `1`.

2. **Core Functionalities**:
   - **Maze Class**: Manages the grid, adding/removing ghosts, and verifying cell states.
   - **Navigator Class**: Computes the path from start to destination using depth-first search.
   - **Stack Class**: A custom stack implementation for tracking the path.

3. **Error Handling**:
   - Raises a `PathNotFoundException` if no valid path exists or the start/destination points are invalid.

4. **Efficiency**:
   - The pathfinding algorithm has a time complexity of O(n * m), where `n` is the number of rows and `m` is the number of columns.

---

## File Structure

- **maze.py**: Implements the Maze class for managing the grid and ghost cells.
- **navigator.py**: Contains the PacMan class and the `find_path` function for pathfinding.
- **stack.py**: Implements the Stack class to store and manage the path.
- **exception.py**: Defines the `PathNotFoundException` class for handling invalid paths.
- **main.py**: Provides an entry point for testing the project.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PacMan-Navigator.git
   cd PacMan-Navigator
   ```

2. Set up your environment with Python 3.x.

3. Run the `main.py` file to test the navigation system:
   ```bash
   python3 main.py
   ```

4. Use the provided Maze, Stack, and Navigator classes to create custom tests.

---

## Example Usage

```python
from maze import Maze
from navigator import PacMan

# Create a 4x4 maze
maze = Maze(4, 4)
maze.add_ghost(1, 1)
maze.add_ghost(2, 2)

# Print the maze layout
maze.print_grid()

# Initialize the PacMan navigator
navigator = PacMan(maze)

# Find path from (0, 0) to (3, 3)
try:
    path = navigator.find_path((0, 0), (3, 3))
    print("Path:", path)
except PathNotFoundException:
    print("No valid path found!")
```

---




