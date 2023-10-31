import unittest
from nfa import *
from regexAST import *

class TestDeterminize(unittest.TestCase):
    """
    This class tests determinizing NFAs
    """

    def test_determinze1(self):
        #(A | B)*
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        nfa = ast.toNfa()
        # nfa.alphabet.add("C")
        dfa = nfa.determinize()
        dfa.convertToImage(30)