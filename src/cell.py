from window import Point, Line, Window

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bot_left), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bot_right), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bot_left, bot_right), "black")

    def draw_move(self, to_cell, undo=False):
        startHorizontalCenter = self._x1 + ((self._x2 - self._x1) / 2)
        startVerticalCenter = self._y1 + ((self._y2 - self._y1) / 2)
        endHorizontalCenter = to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2)
        endVerticalCenter = to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2)

        start = Point(startHorizontalCenter, startVerticalCenter)
        end = Point(endHorizontalCenter, endVerticalCenter)

        if undo:
            self._win.draw_line(Line(start, end), "gray")
        else:
            self._win.draw_line(Line(start, end), "red")


