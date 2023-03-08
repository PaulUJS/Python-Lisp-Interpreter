# Type definitions for the interpreter
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict

arr = []

def read_contents():
    prog_file = open("test.txt", "r")
    res = prog_file.readlines()
    listToStr = ' '.join([str(elem) for elem in res])
    tokenize(listToStr)

def tokenize(chars: str) -> list:
    #chars.replace('(', ' ( ').replace(')', ' ) ').split()
    print(chars)
    for c in chars:
        if c == '(':
            add_token('LeftParen')
        elif c ==')':
            add_token('RighParen')
        elif c == '+':
            add_token('Plus')
        elif c == '-':
            add_token('Minus')
        elif c == '*':
            add_token('Star')
        elif c == '/':
            add_token('Slash')
        elif c == 'define':
            add_token('Define')

def add_token(token: str) -> list:
    arr.append(token)
    print(arr)
    return arr


read_contents()