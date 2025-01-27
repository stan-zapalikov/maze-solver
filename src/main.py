from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(1550, 1550)
    num_cols = 30
    num_rows = 30
    m1 = Maze(10,10, num_rows, num_cols, 50, 50, win)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0,0)
    m1._reset_cells_visited()
    m1.solve()
    win.wait_for_close()

main()