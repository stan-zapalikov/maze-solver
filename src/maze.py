import time
from cell import Cell
from window import Window

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for col in range(self.num_cols):
            column = []
            self._cells.append(column)
            for row in range(self.num_rows):
                newCell = Cell(self._win)
                column.append(newCell)
                self._draw_cell(row, col)
    
    def _draw_cell(self, i, j):
        self._cells[j][i].draw(
            self.x1 + (self.cell_size_x * i),
            self.x1 + (self.cell_size_x * (i + 1)),
            self.y1 + (self.cell_size_y * j),
            self.y1 + (self.cell_size_y * (j + 1))
        )

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

