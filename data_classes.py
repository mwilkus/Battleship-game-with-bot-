class Pole:
    def __init__(self, x, y, ship, shot,drowned):
        self.x=x
        self.y=y
        self.ship=ship
        self.shot=shot
        self.drowned=drowned

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.ship}, {self.shot})"

class Ship:
    def __init__(self, start, end, destroy):
        self.start=start
        self.end=end
        self.destroy=destroy

    def __repr__(self):
        return f"({self.start}, {self.end}, {self.destroy}, {self.leng})"

    def __len__(self):
        row1,col1=self.start
        row2,col2=self.end
        return max(abs(row1-row2), abs(col1-col2))+1