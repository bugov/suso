import os.path
import json
import pytest
from xml.etree import ElementTree
from . import PROJECT_ROOT
from sudoku_solver.io.format import format_registry


fixture = {}
for fmt in ['txt', 'xml', 'csv', 'json']:

    def wrapper(ext):
        @pytest.fixture
        def func():
            file_name = 'input_1.%s' % ext
            txt_file = os.path.join(PROJECT_ROOT, 'example', file_name)
            with open(txt_file, 'r') as fh:
                return fh.read()

        return func

    fixture[fmt] = wrapper(fmt)

input_txt = fixture['txt']
input_csv = fixture['csv']
input_xml = fixture['xml']
input_json = fixture['json']


def test_txt(input_txt):
    fmt = format_registry.get_format('txt')
    struct = fmt.to_python(input_txt)
    assert struct[1][4] == '9'

    assert struct[8][1] is None

    struct[1][4] = '8'
    data = fmt.to_data(struct)
    line = data.splitlines()[1]
    assert line == '6 _ _ 1 8 5 _ _ _'


def test_csv(input_csv):
    fmt = format_registry.get_format('csv')
    struct = fmt.to_python(input_csv)
    assert struct[2][2] == '8'

    assert struct[8][1] is None

    struct[2][2] = '9'
    data = fmt.to_data(struct)
    line = data.splitlines()[2]
    assert line == '_,9,9,_,_,_,_,6,_'


def test_json(input_json):
    fmt = format_registry.get_format('json')
    struct = fmt.to_python(input_json)
    assert struct[1][3] == '1'

    assert struct[2][3] is None

    struct[1][3] = '3'
    data = fmt.to_data(struct)
    assert json.loads(data)[1][3] == '3'


def test_xml(input_xml):
    fmt = format_registry.get_format('xml')
    struct = fmt.to_python(input_xml)
    assert struct[6][1] == '6'

    assert struct[2][3] is None

    struct[6][1] = '7'
    data = fmt.to_data(struct)
    assert ElementTree.fromstring(data)[6][1].get('value') == '7'
