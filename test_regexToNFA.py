import unittest
from regexAST import *

"""All tests for regex to NFA"""
class testToString(unittest.TestCase):

    def buildNFA1(self):
        nfa = NFA()
        nfa.setStates([1,2,3,4,5,6])
        nfa.addEdge(1,2,"A")
        nfa.addEdge(3,4,"B")
        nfa.addEdge(5,1,None)
        nfa.addEdge(5,3,None)
        nfa.addEdge(2,6,None)
        nfa.addEdge(4,6,None)
        nfa.addEdge(5,6,None)
        nfa.addEdge(6,5,None)
        nfa.setStartingStates([5])
        nfa.setAcceptingStates([6])
        nfa.alphabet.add("A")
        nfa.alphabet.add("B")
        return nfa

    
    #(A + B)*
    def test_regextoNFA1(self):
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        s = str(ast)
        nfa = ast.toNfa()
        correct = self.buildNFA1()
        print("correct: " + str(correct.edges))
        print("nfa: " + str(nfa.edges))
        self.assertTrue(correct == nfa)
    
    #((a | b)+ | C)+
    def test_regextoNFA2(self):
        tree = RegexAST()
        o = Or()
        o.first = Just()
        o.first.char = "A"
        o.second = Just()
        o.second.char = "B"
        p = Parens()
        p.what = o
        one = OneOrMore()
        one.what = p
        o = Or()
        o.first = one
        o.second = Just()
        o.second.char = "C"
        p = Parens()
        p.what = o
        o = OneOrMore()
        o.what = p
        tree.root = o
        s = str(tree)
        print(s)
        self.assertTrue(s == "((A | B)+ | C)+")

    # (A+ | B)*
    def test_regextoNFA3(self):
        tree = RegexAST()
        tree.root = ZeroOrMore()
        root = tree.root
        root.what = Parens()
        p = root.what
        p.what = Or()
        p.what.first = OneOrMore()
        p.what.first.what = Just()
        p.what.first.what.char = "A"
        p.what.second = Just()
        p.what.second.char = "B"
        s = str(tree)
        print(s)
        self.assertTrue(s == "(A+ | B)*")
        
    # A+ | ((B | C)* D)
    def test_regextoNFA4(self):
        tree = RegexAST()
        o = Or()
        tree.root = o
        r = tree.root
        r.first = OneOrMore()
        r.first.what = Just()
        r.first.what.char = "A"
        sec = Parens()
        r.second = sec
        sec.what = Follows()
        f = sec.what
        f.first = ZeroOrMore()
        f.first.what = Parens()
        f.first.what.what = Or()
        o = f.first.what.what
        o.first = Just()
        o.first.char = "B"
        o.second = Just()
        o.second.char = "C"
        f.second = Just()
        f.second.char = "D"
        s = str(tree)
        self.assertTrue(s == "A+ | ((B | C)* D)")

    # A B C
    def test_regextoNFA5(self):
        tree = RegexAST()
        tree.root = Follows()
        tree.root.first = Just()
        tree.root.first.char = "A"
        f = Follows()
        tree.root.second = f
        f.first = Just()
        f.first.char = "B"
        f.second = Just()
        f.second.char = "C"
        s = str(tree)
        self.assertTrue(s == "A B C")