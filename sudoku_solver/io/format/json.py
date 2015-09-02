from __future__ import absolute_import
import json
from .base import BaseFormat


class JsonFormat(BaseFormat):
    @classmethod
    def to_data(cls, data):
        lines = []
        for row in data:
            clean = [r or '_' for r in row]
            lines.append(clean)

        return json.dumps(lines)

    @classmethod
    def to_python(cls, data):
        result = []

        for row in json.loads(data):
            row = [c if c != '_' else None for c in row]
            result.append(row)

        return result
