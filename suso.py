import argparse
from sudoku_solver.io.reader import Reader
from sudoku_solver.io.writer import Writer
from sudoku_solver.io.format import get_formatter
from sudoku_solver.solver import BacktrackingSolver
from sudoku_solver.solver.rule import rule_registry

parser = argparse.ArgumentParser(prog='suso.py', usage='%(prog)s [options]')
parser.add_argument('--in-file', required=True, help='Input file. Example: ./example/input_1.json')
parser.add_argument('--out-file', required=True, help='Output file. Example: ./output_1.txt')
parser.add_argument('--in-format', help='Input file format. Example: "json"')
parser.add_argument('--out-format', help='Output file format. Example: "xml"')
parser.add_argument('-f', '--force', nargs='?', type=bool, default=False, help='Force overwrite output file')
parser.add_argument('--rules', default='standard', help='Rules for solver. Example: "standard;color"')
    
args = parser.parse_args()

in_format = get_formatter(args.in_format, args.in_file)
out_format = get_formatter(args.out_format, args.out_file)
reader = Reader(in_format, args.in_file)
writer = Writer(out_format, args.out_file, args.force)

state = reader.read()

rules = [rule_registry.get_rule(name) for name in args.rules.split(';')]
solver = BacktrackingSolver(rules)
state = solver.solve(state)
writer.write(state)
