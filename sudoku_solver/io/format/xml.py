from __future__ import absolute_import
from xml.etree import ElementTree
from .base import BaseFormat


class XmlFormat(BaseFormat):
    @classmethod
    def to_data(cls, data):
        rowset_el = ElementTree.Element('rowset')

        for row in data:
            row_el = ElementTree.SubElement(rowset_el, 'row')
            clean_row = (str(r) if r else '_' for r in row)

            for cell in clean_row:
                ElementTree.SubElement(row_el, 'cell', {'value': cell})

        return ElementTree.tostring(rowset_el)

    @classmethod
    def to_python(cls, data):
        rowset_el = ElementTree.fromstring(data)
        result = []

        for row_el in rowset_el.findall('row'):
            row = (cell_el.get('value') for cell_el in row_el.findall('cell'))
            row = [c if c != '_' else None for c in row]
            result.append(row)

        return result
