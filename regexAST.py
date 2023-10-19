class Parens:
    def __init__(self):
        self.what = None

class OneOrMore:
    def __init__(self):
        self.what = None

class ZeroOrMore:
    def __init__(self):
        self.what = None

class follows:
    def __init__(self):
        self.first = None
        self.second = None

class Or:
    def __init__(self):
        self.first = None
        self.second = None

class RegexAST:
    def __init__(self):
        self.root = None