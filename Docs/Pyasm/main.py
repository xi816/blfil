import os
import sys
import math

CPATH = os.path.dirname(__file__) + "/"

def lexCode(code):
    fin = []
    # i1 is index, i2 is line
    for i1, i2 in enumerate(code.split("\n")):
        fin.append({"line": i1, "contents": i2})
    return fin

def compileLexed(lexed, outfile):
    out = "global _start"
    for line, cont in lexed:
        pass


if len(sys.argv) != 4:
    raise ValueError("Expected format python main.py -c <in> <out>")
if sys.argv[1] == "-c":
    with open(CPATH + sys.argv[2], "r") as code:
        cdr = code.read()
    lexed = lexCode(cdr)
    compileLexed(lexed, sys.argv[3])

