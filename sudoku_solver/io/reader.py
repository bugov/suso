from ..models import State


class Reader:
    def __init__(self, Formatter, file_path):
        self.formatter = Formatter
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as fh:
            data = fh.read()
            structure = self.formatter.to_python(data)

        return State(structure)
