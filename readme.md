# Решатель судоку

На вход программе подаётся файл с нерешённой головоломкой
([подробнее о судоку](https://en.wikipedia.org/wiki/Sudoku)).

Решение выводится также в файл.

Пример:
```
suso.py --in=./example/input1.json --out=./output.xml
```

# Параметры

* `--in` -- входной файл.
* `--out` -- результирующий файл.
* `--rules` -- список правил, по которым решается судоку.

Правила:

* `standard` -- обычные правила решения судоку: "требуется заполнить свободные
клетки цифрами от 1 до 9 так, чтобы в каждой строке, в каждом столбце и в каждом
 малом квадрате 3×3 каждая цифра встречалась бы только один раз."

# Поддерживаемые форматы

txt, csv, json, xml

Входной файл:

![sudoku](https://upload.wikimedia.org/wikipedia/commons/f/ff/Sudoku-by-L2G-20050714.svg)

## txt

    5 3 _ _ 7 _ _ _ _
    6 _ _ 1 9 5 _ _ _
    _ 9 8 _ _ _ _ 6 _
    8 _ _ _ 6 _ _ _ 3
    4 _ _ 8 _ 3 _ _ 1
    7 _ _ _ 2 _ _ _ 6
    _ 6 _ _ _ _ 2 8 _
    _ _ _ 4 1 9 _ _ 5
    _ _ _ _ 8 _ _ 7 9

## csv

    5,3,_,_,7,_,_,_,_
    6,_,_,1,9,5,_,_,_
    _,9,8,_,_,_,_,6,_
    8,_,_,_,6,_,_,_,3
    4,_,_,8,_,3,_,_,1
    7,_,_,_,2,_,_,_,6
    _,6,_,_,_,_,2,8,_
    _,_,_,4,1,9,_,_,5
    _,_,_,_,8,_,_,7,9

## json

    [
    ["5", "3", "_", "_", "7", "_", "_", "_", "_"],
    ["6", "_", "_", "1", "9", "5", "_", "_", "_"],
    ["_", "9", "8", "_", "_", "_", "_", "6", "_"],
    ["8", "_", "_", "_", "6", "_", "_", "_", "3"],
    ["4", "_", "_", "8", "_", "3", "_", "_", "1"],
    ["7", "_", "_", "_", "2", "_", "_", "_", "6"],
    ["_", "6", "_", "_", "_", "_", "2", "8", "_"],
    ["_", "_", "_", "4", "1", "9", "_", "_", "5"],
    ["_", "_", "_", "_", "8", "_", "_", "7", "9"]
    ]

## xml

    <?xml version="1.1" encoding="UTF-8" ?>
    <field>
        <row> <cell value="5"/> <cell value="3"/> <cell value="_"/> <cell value="_"/> <cell value="7"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> </row>
        <row> <cell value="6"/> <cell value="_"/> <cell value="_"/> <cell value="1"/> <cell value="9"/> <cell value="5"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> </row>
        <row> <cell value="_"/> <cell value="9"/> <cell value="8"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="6"/> <cell value="_"/> </row>
        <row> <cell value="8"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="6"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="3"/> </row>
        <row> <cell value="4"/> <cell value="_"/> <cell value="_"/> <cell value="8"/> <cell value="_"/> <cell value="3"/> <cell value="_"/> <cell value="_"/> <cell value="1"/> </row>
        <row> <cell value="7"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="2"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="6"/> </row>
        <row> <cell value="_"/> <cell value="6"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="2"/> <cell value="8"/> <cell value="_"/> </row>
        <row> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="4"/> <cell value="1"/> <cell value="9"/> <cell value="_"/> <cell value="_"/> <cell value="5"/> </row>
        <row> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="_"/> <cell value="8"/> <cell value="_"/> <cell value="_"/> <cell value="7"/> <cell value="9"/> </row>
    </field>

