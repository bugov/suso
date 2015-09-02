from __future__ import absolute_import
import csv
from StringIO import StringIO
from .base import BaseFormat


class CsvFormat(BaseFormat):
    @classmethod
    def to_data(cls, data):
        buf = StringIO()
        writer = csv.writer(buf)

        for row in data:
            clean = [r or '_' for r in row]
            writer.writerow(clean)

        result = buf.getvalue()
        buf.close()

        return result

    @classmethod
    def to_python(cls, data):
        buf = StringIO(data)
        reader = csv.reader(buf, delimiter=',')
        result = []

        for row in reader:
            row = [c if c != '_' else None for c in row]
            result.append(row)

        buf.close()

        return result
