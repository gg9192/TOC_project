""" The purpose of this file is to contain all the classes required to build an AST for regex
    To get more detail, look at the second method.
"""
from nfa import *

"""The purpose of this class is to represent parentheses in regex"""
class Parens:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return "(" + str(self.what) + ")"
    
    "converts the regex to NFA" 
    def toNFA(self):
        return self.what.toNfa()

"""This represents one or more of a given regex"""
class OneOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "+"
    
    "converts the regex to NFA"
    def toNFA():
        pass

"""This represents zero or more of a given regex"""
class ZeroOrMore:
    def __init__(self):
        self.what = None

    def __repr__(self):
        return str(self.what) + "*"
    
    "converts the regex to NFA"
    def toNFA():
        pass

"""This represents one regex followed by another"""
class Follows:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + " " + str(self.second)
    
    "converts the regex to NFA"
    def toNFA():
        pass

"""This represents one regex or another"""
class Or:
    def __init__(self):
        self.first = None
        self.second = None

    def __repr__(self):
        return str(self.first) + " | " + str(self.second)
    
    "converts the regex to NFA"
    def toNFA(self):
        nfa1 = self.first.toNFA()
        nfa2 = self.second.toNFA()
        
    
class Just:
    def __init__(self):
        self.char = None
    
    def __repr__(self):
        return str(self.char)
    
    "converts the regex to NFA"
    def toNfa(self):
        nfa = NFA()
        nfa.setStates([1,2])
        nfa.setStartingStates([1])
        nfa.setAcceptingStates([2])
        nfa.addEdge(1,2,self.char)


"""This is the class for an abstract syntax tree for regex"""
class RegexAST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root) #recursion
    
    def toNFA(self):
        return self.root.toNFA()

