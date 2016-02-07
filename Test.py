#!/usr/bin/env python

from antlr4 import *
from SQLiteLexer import SQLiteLexer
from SQLiteParser import SQLiteParser
from SQLiteListener import SQLiteListener
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

import sys

def main(argv):
    print "Parsing: " + argv[1] + "\n"

    input = FileStream(argv[1])
    lexer = SQLiteLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SQLiteParser(stream)

    tree = parser.parse()

    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)
