import os


class Writer:
    def __init__(self, Formatter, file_path, force=False):
        self.formatter = Formatter
        self.force = force
        self.file_path = file_path

        if not self.force and os.path.exists(file_path):
            raise Exception(u'File "%s" already exists. Use the --force to overwrite' % file_path)

    def write(self, grid):
        with open(self.file_path, 'w') as fh:
            data = self.formatter.to_data(grid.to_structure())
            fh.write(data)
