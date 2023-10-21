import unittest
from regexAST import *

class testToString(unittest.TestCase):
    
    #(A + B)*
    def test_regextostring1(self):
        tree = RegexAST()
        tree.root = ZeroOrMore()
        what = Parens()
        orr = Or()
        what.what = orr
        tree.root.what = what
        orr.first = "A"
        orr.second = "B"
        s = str(tree)
        self.assertTrue(s == "(A | B)*")
    
    #((a | b)+ | c)+
    def test_regextostring2(self):
        tree = RegexAST()
        o = Or()
        o.first = "A"
        o.second = "B"
        p = Parens()
        p.what = o
        one = OneOrMore()
        one.what = p
        o = Or()
        o.first = one
        o.second = "C"
        p = Parens()
        p.what = o
        o = OneOrMore()
        o.what = p
        tree.root = o
        s = str(tree)
        print(s)
        self.assertTrue(s == "((A | B)+ | C)+")