from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(10, 50, 10, 50)

    cell2 = Cell(win)
    cell2.draw(10, 50, 50, 90)

    cell1.draw_move(cell2, True)
    win.wait_for_close()

main()