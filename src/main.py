from window import Window, Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(12, 12), Point(222, 89))
    line2 = Line(Point(400, 231), Point(56, 300))
    win.draw_line(line1, "black")
    win.draw_line(line2, "blue")
    win.wait_for_close()

main()