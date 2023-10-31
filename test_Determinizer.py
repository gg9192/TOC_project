import unittest
from nfa import *
from regexAST import *

class TestDeterminize(unittest.TestCase):
    """This class tests determinizing NFAs
    """
    @pytest.fixture(scope="session")
    def my_fixture():
        print('INITIALIZATION')
        yield 2
        print('TEAR DOWN')

    def test_determinze1(self):
        #(A | B)*
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        nfa = ast.toNfa()
        
        nfa.determinize()