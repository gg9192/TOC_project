""" The purpose of this file is to contain all the classes required to build an AST for regex
    To get more detail, look at the second method.
"""

"""The purpose of this class is to represent parentheses in regex"""
class Parens:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return "(" + str(self.what) + ")"

"""This represents one or more of a given regex"""
class OneOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "+"

"""This represents zero or more of a given regex"""
class ZeroOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "*"

"""This represents one regex followed by another"""
class Follows:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + " " + str(self.second)

"""This represents one regex or another"""
class Or:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + " | " + str(self.second)

"""This is the class for an abstract syntax tree for regex"""
class RegexAST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root) #recursion
    

