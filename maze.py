class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        self._m = m
        self._n = n
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    
    def add_ghost(self, x : int, y: int) -> None:
        self.grid_representation[x][y] = 1
        
    def remove_ghost(self, x : int, y: int) -> None:
        self.grid_representation[x][y] = 0
        
    def is_ghost(self, x : int, y: int) -> bool:
        if(self.grid_representation[x][y] == 1):
            return True
        return False
        
    def print_grid(self) -> None:
        for row in range(self._m):
            for column in range(self._n):
                print(self.grid_representation[row][column], end = " ")
            print()
        