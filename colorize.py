#!/usr/bin/env python

from os import path
import sys,subprocess

from pygments import highlight
from pygments.lexers import PythonTracebackLexer
from pygments.lexer import bygroups, using
from pygments.token import Text, Keyword, Text, Number, Text, Name, Text
from pygments.formatters import Terminal256Formatter

project_dir = path.abspath(path.dirname(__file__))

#pp_token = Name.Function
pp_token = Name.Builtin
pf_token = Name.Class

class DjangoProjectTracebackLexer(PythonTracebackLexer):
    tokens = PythonTracebackLexer.tokens
    tokens.update({'intb':[
        (r'^(  File )("%s)([^"]+)(")(, line )(\d+)(, in )(.+)(\n)' % project_dir,
             bygroups(Text, pp_token,pf_token,pp_token, Text, Number, Text, Name, Text)
             )
        ]+PythonTracebackLexer.tokens['intb'] })

if '__main__' == __name__:
    try:
        print "-" * 78
        output = subprocess.check_output( sys.argv[1:], stderr=subprocess.STDOUT )
        print output

    except subprocess.CalledProcessError as e:
        print highlight(
                e.output,
                DjangoProjectTracebackLexer(),
                Terminal256Formatter()
                )

    print "-" * 78
