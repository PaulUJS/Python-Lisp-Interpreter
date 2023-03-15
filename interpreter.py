# Type definitions for the interpreter
Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict

tokens = []

class Expression:
    op = ''
    index = 0
    expr = []
    num = []
    result = None

    def listify(self):
        count = 0
        ops = ['Plus', 'Minus', 'Star', 'Slash']
        if len(self.expr) == 0:
            self.expr.append([])
        for i in tokens:
            count += 1
            if i in ops:
                self.expr[self.index].append(i)
            elif num_match(i):
                self.expr[self.index].append(i)
            elif i == 'LeftParen' and count > 1:
                self.expr.append([])
                self.index += 1
        print(self.expr)
        self.evaluate()

    def evaluate(self):
        index = len(self.expr) - 1
        ops = {
            'Plus': lambda x, y: x + y,
            'Minus': lambda x, y: x - y,
            'Star': lambda x, y: x * y,
            'Slash': lambda x, y: x // y,
          }
        res = []
        while index >= 1:
            for i in self.expr[index]:
                if ops.get(i):
                    self.op = i
                if num_match(i):
                    self.num.append(int(i))
            res.append(ops[self.op](self.num[0], self.num[1]))
            self.num.clear()
            index -= 1
        for v in self.expr[index]:
            if ops.get(v):
                self.op = v
        print(res)
        print(ops[self.op](res[0], res[1]))
        


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

read_contents()
exp = Expression()
exp.listify()
