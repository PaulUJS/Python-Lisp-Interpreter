class Expression:
    def __init__(self, op, expr, num, index):
        self.op = op
        self.expr = expr
        self.num = num
        self.index = index

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def listify(self, tokens):
        count = 0
        ops = ['Plus', 'Minus', 'Star', 'Slash']
        if len(self.expr) == 0:
            self.expr.append([])
        for i in tokens:
            count += 1
            if i in ops:
                self.expr[self.index].append(i)
            elif lispy.num_match(i):
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
                if lispy.num_match(i):
                    self.num.append(int(i))
            res.append(ops[self.op](self.num[0], self.num[1]))
            self.num.clear()
            index -= 1
        for v in self.expr[index]:
            if ops.get(v):
                self.op = v
        print(res)
        print(ops[self.op](res[0], res[1]))

class interpreter:
    tokens = []
    def read_contents(self) -> str:
        prog_file = open("test.txt", "r")
        res = prog_file.readlines()
        listToStr = ' '.join([str(elem) for elem in res])
        self.tokenize(listToStr)

    def num_match(self, num: str) -> bool:
        nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if nums.get(num):
            return True
        return False

    def op_match(self, op: str) -> str:
        ops = {'+': 'Plus', '-': 'Minus', '*': 'Star', '/': 'Slash'}
        if ops.get(op):
            #add_token(ops.get(op))
            return ops.get(op)

    def tokenize(self, chars: str) -> list:
        print(chars)
        left = 0
        right = 0
        for c in chars:
            if left != right or left == 0 :
                if c == '(':
                    left += 1
                    self.add_token('LeftParen')
                elif c ==')':
                    right += 1
                    self.add_token('RighParen')
                elif self.num_match(c):
                    self.add_token(c)
                elif self.op_match(c): 
                    self.add_token(self.op_match(c))
            elif left == right and left > 0:
                left = 0; right = 0;
                object = Expression('', [], [], 0)
                object.listify(self.tokens)
                self.tokens = []

    def add_token(self, token: str) -> list:
        self.tokens.append(token)
        return self.tokens

lispy = interpreter()
lispy.read_contents()
