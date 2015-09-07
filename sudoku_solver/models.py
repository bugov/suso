from copy import deepcopy


class State:
    _size = 9
    _segment_size = 3

    def __init__(self, data, x=0, y=0):
        self._data = [[int(c) if c else None for c in row] for row in data]
        self.x = x
        self.y = y

    def __repr__(self):
        str_list = []
        for row in self._data:
            row_str = ', '.join([str(c) for c in row])
            str_list.append('[%s]' % row_str)

        return '[' + ',\n'.join(str_list) + ']'

    def __getitem__(self, pos):
        x, y = pos
        return self._data[x][y]

    def __setitem__(self, pos, val):
        x, y = pos
        self._data[x][y] = val

    def to_structure(self):
        return deepcopy(self._data)

    def set_cell(self, val):
        self._data[self.x][self.y] = val

    def get_cell(self):
        return self._data[self.x][self.y]

    def clone(self):
        return State(self._data, self.x, self.y)

    def get_segment_pos(self):
        size = self.get_segment_size()
        return self.x / size, self.y / size

    def get_size(self):
        return self._size

    def get_segment_size(self):
        return self._segment_size

    def get_row(self, index):
        return self._data[index]

    def get_col(self, index):
        return (row[index] for row in self._data)

    def get_segment(self, x, y):
        size = self.get_segment_size()

        for i in xrange(x * size, (x+1) * size):
            for j in xrange(y * size, (y+1) * size):
                yield self._data[i][j]
