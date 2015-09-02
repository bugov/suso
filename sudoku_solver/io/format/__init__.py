from .txt import TxtFormat
from .csv import CsvFormat
from .xml import XmlFormat
from .json import JsonFormat


class FormatRegistry:
    formats = {}

    def get_format(self, name):
        klass = self.formats.get(name)

        if not klass:
            raise NotImplementedFormat

        return klass

    def add_format(self, name, klass):
        self.formats[name] = klass


class NotImplementedFormat(Exception):
    pass


format_registry = FormatRegistry()
format_registry.add_format('txt', TxtFormat)
format_registry.add_format('csv', CsvFormat)
format_registry.add_format('xml', XmlFormat)
format_registry.add_format('json', JsonFormat)
