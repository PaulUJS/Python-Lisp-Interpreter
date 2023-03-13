# Type definitions for the interpreter
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict

tokens = []

def read_contents() -> str:
    prog_file = open("test.txt", "r")
    res = prog_file.readlines()
    listToStr = ' '.join([str(elem) for elem in res])
    tokenize(listToStr)

def num_match(num: str) -> bool:
    nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if nums.get(num):
        return True
    return False

def op_match(op: str) -> str:
    ops = {'+': 'Plus', '-': 'Minus', '*': 'Star', '/': 'Slash'}
    if ops.get(op):
        #add_token(ops.get(op))
        return ops.get(op)

def tokenize(chars: str) -> list:
    #chars.replace('(', ' ( ').replace(')', ' ) ').split()
    print(chars)
    for c in chars:
        if c == '(':
            add_token('LeftParen')
        elif c ==')':
            add_token('RighParen')
        elif num_match(c):
            add_token(c)
        elif op_match(c): 
            add_token(op_match(c))
    print(tokens)

def add_token(token: str) -> list:
    tokens.append(token)
    return tokens

def evaluate():
    ops = {
            'Plus': lambda x, y: print(x + y),
            'Minus': lambda x, y: print(x - y),
            'Star': lambda x, y: print(x * y),
            'Slash': lambda x, y: print(x / y)
          }
    op = ''
    num = []
    for i in tokens:
        if len(num) != 2:
            if ops.get(i):
                op = i
            if num_match(i):
                num.append(int(i))
        else:  
            ops[op](num[0], num[1])
            num.clear()
            op = ''


read_contents()
evaluate()
