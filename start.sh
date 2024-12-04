#!/bin/bash

mkdir -p $1/$2
cd $1/$2

echo 'from helpers import read_input' > code.py
echo >> code.py
echo 'sample=""""""' >> code.py
echo >> code.py
echo "puzzle=read_input($1,$2)" >> code.py
echo >> code.py
echo 'def solve1(puzzle):' >> code.py
echo '    pass' >> code.py
echo >> code.py
echo 'print(solve1(sample))' >> code.py
ruff --fix code.py
touch input_$2.txt

