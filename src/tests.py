import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(10,10, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[m1.num_cols-1][m1.num_rows-1].has_bottom_wall, False)
        win.wait_for_close()
        
    
if __name__=="__main__":
    unittest.main()