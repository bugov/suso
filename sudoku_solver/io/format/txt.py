from .base import BaseFormat


class TxtFormat(BaseFormat):
    @classmethod
    def to_data(cls, data):
        lines = []
        for row in data:
            clean = (str(r) if r else '_' for r in row)
            line = ' '.join(clean)
            lines.append(line)

        return '\n'.join(lines)

    @classmethod
    def to_python(cls, data):
        result = []

        for line in data.splitlines():
            row = line.split()
            row = [c if c != '_' else None for c in row]
            result.append(row)

        return result
