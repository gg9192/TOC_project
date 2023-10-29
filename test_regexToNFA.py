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

    
    #(A | B)*
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
        self.assertTrue(correct == nfa)
    
    def buildNFA2(self):
            nfa = NFA()
            nfa.setStates([1,2,3,4,5,6,7,8,9,10])
            nfa.addEdge(1,2,"A")
            nfa.addEdge(3,4,"B")
            nfa.addEdge(5,1,None)
            nfa.addEdge(5,3,None)
            nfa.addEdge(2,6,None)
            nfa.addEdge(4,6,None)
            nfa.addEdge(6,5,None)
            nfa.addEdge(7,8,"C")
            nfa.addEdge(9,5,None)
            nfa.addEdge(9,7,None)
            nfa.addEdge(6,10,None)
            nfa.addEdge(8,10,None)
            nfa.addEdge(10,9,None)
            nfa.setStartingStates([9])
            nfa.setAcceptingStates([10])
            nfa.alphabet.add("A")
            nfa.alphabet.add("B")
            nfa.alphabet.add("C")
            return nfa

    #((A | B)+ | C)+
    def test_regextoNFA2(self):
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        innerParen = Parens(orr)
        oom = OneOrMore(innerParen)
        c = Just("C")
        orr2 = Or(oom, c)
        outerparens = Parens(orr2)
        oom2 = OneOrMore(outerparens)
        tree = RegexAST(oom2)
        nfa = tree.toNfa()
        correct = self.buildNFA2()
        self.assertTrue(correct == nfa)

    # (A+ | B)*
    def test_regextoNFA3(self):
        a = Just("A")
        b = Just("B")
        oom = OneOrMore(a)
        orr = Or(oom, b)
        paren = Parens(orr)
        zmm2 = ZeroOrMore(paren)
        tree = RegexAST(zmm2)
        s = str(tree)
        self.assertTrue(s == "(A+ | B)*")
        
    # A+ | ((B | C)* D)*
    def test_regextoNFA4(self):
        a = Just("A")
        oom = OneOrMore(a)
        b = Just(b)
        tree = RegexAST()
        s = str(tree)
        self.assertTrue(s == "A+ | ((B | C)* D)*")

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