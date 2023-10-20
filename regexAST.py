class Parens:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return "(" + str(self.what) + ")"

class OneOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "+"

class ZeroOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "*"

class follows:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + str(self.second)

class Or:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + " + " + str(self.second)

class RegexAST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)
    
tree = RegexAST()
tree.root = ZeroOrMore()
what = Parens()
orr = Or()
what.what = orr
tree.root.what = what
orr.first = "A"
orr.second = "B"
print(tree)
