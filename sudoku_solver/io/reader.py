from ..models import RowSet


class Reader:
    def read(self, file_path, Formatter):
        with open(file_path, 'r') as fh:
            data = fh.read()
            structure = Formatter.to_python(data)

        row_set = RowSet(structure)

        return row_set
