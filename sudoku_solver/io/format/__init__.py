import os.path
from .txt import TxtFormat
from .csv import CsvFormat
from .xml import XmlFormat
from .json import JsonFormat


class FormatRegistry:
    _formats = {}

    def get_format(self, name):
        klass = self._formats.get(name)

        if not klass:
            raise NotImplementedFormat

        return klass

    def add_format(self, name, klass):
        self._formats[name] = klass


class NotImplementedFormat(Exception):
    pass


def get_formatter(format_name, file_name):
    if format_name:
        fmt = format_name.lower()
    else:
        _, fmt = os.path.splitext(file_name.lower())
        fmt = fmt[1:]

    return format_registry.get_format(fmt)

format_registry = FormatRegistry()
format_registry.add_format('txt', TxtFormat)
format_registry.add_format('csv', CsvFormat)
format_registry.add_format('xml', XmlFormat)
format_registry.add_format('json', JsonFormat)
