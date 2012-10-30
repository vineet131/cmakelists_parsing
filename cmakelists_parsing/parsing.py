# -*- coding: utf-8 -*-

'''A CMakeLists parser using funcparserlib.

The parser is based on [examples of the CMakeLists format][1].

  [1]: http://www.vtk.org/Wiki/CMake/Examples

'''

from __future__ import unicode_literals, print_function
import re
import pypeg2 as p

class CmParsingError(Exception):
    pass

class Arg(p.str):
    grammar = re.compile(r'[${}_a-zA-Z0-9]+')

class Command(p.List):
    grammar = p.name(), '(', p.some(Arg), ')'

class File(p.List):
    grammar = p.some(Command)

def parse(s):
    tree = p.parse(s, File, comment=p.comment_sh)
    return tree

def main():
    import sys
    ENCODING = 'utf-8'
    input = sys.stdin.read().decode(ENCODING)
    tree = parse(input)
    print(str(tree).encode(ENCODING))

if __name__ == '__main__':
    main()
