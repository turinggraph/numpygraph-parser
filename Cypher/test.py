__author__ = 'hp027'

import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from CypherLexer import CypherLexer
from CypherParser import CypherParser
from NPGVistor import NPGVisitor
from pprint import pprint


# this is a python version of TestRig
def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' '*indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i+1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     input_stream = FileStream(sys.argv[1])
    # else:
    #     input_stream = InputStream(sys.stdin.readline())
    s = "match  (n:Person)-[:HAS_PHONE]->(p:Phone) where n.name=\"姓名6\" return n,p limit 20"
    s = "MATCH (n) RETURN n"
    s = '''MATCH (n { name: "Anders" })--(m) WHERE n.age=13
WITH m
ORDER BY m.name DESC LIMIT 1
MATCH (m)--(o)
RETURN o.name
'''
    s = '''MATCH (n:Author { name: "Anders" })--(m:Movie) WHERE rand()<0.1 and n.age=13
WITH m
MATCH (m)--(o)
RETURN o.name
'''
# ORDER BY m.name DESC LIMIT 1
    # s = '''MATCH p=(n)--(m) WHERE n.label IN ['ACTION', 'MOVIE', 'DEVICE'] AND m.label IN ['ACTION', 'MOVIE', 'DEVICE'] RETURN p'''
    input_stream = InputStream(s)
    lexer = CypherLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CypherParser(token_stream)
    tree = parser.oC_Cypher()
    
    lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)
    # lisp_tree_str = tree.toPrettyTree(recog=parser)
    print(lisp_tree_str)

    def strprintlen(s):
        return sum([2 if ord(w) > 255 else 1 for w in s])
    lines = []
    lnum = 0
    line = ""
    tokens = []
    tokens_level = []
    
    for i, s in enumerate(lisp_tree_str.replace("( (", "〖 (").replace(") )", ") 〗")):
        ns = lisp_tree_str[i + 1] if (i != len(lisp_tree_str) - 1) else None
        if s == ')' and (ns != '(' or (i == len(lisp_tree_str) - 1)):
            lnum -= 1
        if (s == '(' and ns != '(') or (i == len(lisp_tree_str) - 1):
            if (s == '(' and ns != '('):
                lnum += 1
            if i == len(lisp_tree_str) - 1:
                line += ")"
            if len(line.split(" ")) > 2:
                token = " ".join([s.split(")")[0] for s in line.split(" ")[1:]]).replace("〖", "(").replace("〗", ")")
                tokens_level.append(len(line.split("¥")))
                line += " " * (70 - len(line)) + "\t\t……\t" + token + (20 - len(token)) * " " + "\t……\t" + str(len(line.split("¥")))
                tokens.append(token)
            # else:
            #     token = None
            # line += (" " * (70 - len(line)) + "\t\t……\t" + "".join([s.split(")")[0] for s in line.split(" ")[1:]])) if len(line.split(" ")) > 2 else ""
            lines.append(line.replace("〖", "(").replace("〗", ")").replace("¥", " "))
            # assert lnum >= 0
            line = "\n" + '¥' * lnum
        
            # r.append("\n" + ' ' * l)
        line += s
    # lines.append(line.replace("〖", "(").replace("〗", ")").replace("¥", " "))
    
    print("".join(lines))
    print("".join(tokens))
    levels = []
    current_level = 0
    level_map = {v: k for k, v in enumerate(sorted(set(tokens_level)))}
    tokens_level_new = [level_map[level] for level in tokens_level]
    # print("".join([len(token) * str(level) for token, level in zip(tokens, tokens_level_new)]))
    # print("".join([strprintlen(token) * '-' for token, level in zip(tokens, tokens_level_new)]))
    for i in range(max(tokens_level_new))[::-1]:
        print("".join([strprintlen(token) * ('-' if level >= i else ' ') for token, level in zip(tokens, tokens_level_new)]))
    # print(strprintlen("".join(tokens)) * "-")
    print("():", lnum)
    visitor = NPGVisitor()
    visitor.visit(tree)
