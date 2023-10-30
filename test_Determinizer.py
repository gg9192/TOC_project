import unittest
from nfa import *
from regexAST import *
import os

class TestDeterminize(unittest.TestCase):
    """This class tests determinizing NFAs
    """
    def test_determinze1(self):
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        nfa = ast.toNfa()
        nfa.determinize()