import os


class Writer:
    def __init__(self, Formatter, file_path, force=False):
        self.formatter = Formatter
        self.force = force
        self.file_path = file_path

        if not self.force and os.path.exists(file_path):
            raise Exception('File "%s" already exists. Use the --force=True to overwrite' % file_path)

    def write(self, state):
        with open(self.file_path, 'w') as fh:
            data = self.formatter.to_data(state.to_structure())
            fh.write(data)
