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
    
    #((a | b)+ | C)+
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

    # (A+ | B)*
    def test_regextostring3(self):
        tree = RegexAST()
        tree.root = ZeroOrMore()
        root = tree.root
        root.what = Parens()
        p = root.what
        p.what = Or()
        p.what.first = OneOrMore()
        p.what.first.what = "A"
        p.what.second = "B"
        s = str(tree)
        print(s)
        self.assertTrue(s == "(A+ | B)*")
        
    # A+ | ((B | C)* D)
    def test_regextostring4(self):
        tree = RegexAST()
        o = Or()
        tree.root = o
        r = tree.root
        r.first = OneOrMore()
        r.first.what = "A"
        sec = Parens()
        r.second = sec
        sec.what = Follows()
        f = sec.what
        f.first = ZeroOrMore()
        f.first.what = Parens()
        f.first.what.what = Or()
        o = f.first.what.what
        o.first = "B"
        o.second = "C"
        f.second = "D"
        s = str(tree)
        print(s)
        self.assertTrue(s == "A+ | ((B | C)* D)")
