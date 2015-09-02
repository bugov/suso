class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return unicode(self.value)

    def __unicode__(self):
        return self.__repr__()


class RowSet:
    cells = []

    def __init__(self, data):
        for row in data:
            cells = (Cell(c) for c in row)
            self.cells.append(cells)
