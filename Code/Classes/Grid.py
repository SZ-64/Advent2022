class Grid:

    def __init__(self, rows, cols):
        self._grid = []

        for x in range(rows):
            self._grid.append([])
            for y in range(cols):
                self._grid[x].append([])
