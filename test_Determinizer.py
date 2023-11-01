import unittest
from nfa import *
from regexAST import *

class TestDeterminize(unittest.TestCase):
    """
    This class tests determinizing NFAs
    """
    def buildDfa1(self):
        dfa = NFA()
        for i in range(1,5):
            dfa.setStates([i])
        dfa.setAcceptingStates([2,3,4])
        dfa.setStartingStates([2])
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,4 ,"B")
        dfa.addEdge(2,1 ,"C")
        dfa.addEdge(4,4,"B")
        dfa.addEdge(4,3,"A")
        dfa.addEdge(4,1,"C")
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,4,"B")
        dfa.addEdge(3,1,"C")
        dfa.addEdge(1,1,"A")
        dfa.addEdge(1,1,"B")
        dfa.addEdge(1,1,"C")
        return dfa
        
    
    def test_determinze1(self):
        #(A | B)*
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        nfa = ast.toNfa()
        print(nfa.alphabet)
        nfa.alphabet.add("C")
        print(nfa.alphabet)
        dfa = nfa.determinize()
        
        correct = self.buildDfa1()
        self.assertTrue(dfa == correct)

    def buildDfa2(self):
        dfa = NFA()
        for i in range(2,6):
            dfa.setStates([i])
        dfa.setAcceptingStates([3,4,5])
        dfa.setStartingStates([2])
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,4,"B")
        dfa.addEdge(2,5,"C")        
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,4,"B")
        dfa.addEdge(3,5,"C")
        dfa.addEdge(4,3,"A")
        dfa.addEdge(4,4,"B")
        dfa.addEdge(4,5,"C")
        dfa.addEdge(5,3,"A")
        dfa.addEdge(5,4,"B")
        dfa.addEdge(5,5,"C")
        return dfa

    def test_determinze2(self):
        """((A | B)+ | C)+"""
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
        dfa = tree.toNfa().determinize()
        correct = self.buildDfa2()
        self.assertTrue(correct == dfa)
        
    def buildDfa3(self):
        dfa = NFA()
        dfa.setStates([2,3,4])
        dfa.setAcceptingStates([2,3,4])
        dfa.setStartingStates([2])
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,4,"B")       
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,4,"B")
        dfa.addEdge(4,3,"A")
        dfa.addEdge(4,4,"B")
        return dfa

    def test_Determinized3(self):
        """# (A+ | B)*"""
        a = Just("A")
        b = Just("B")
        oom = OneOrMore(a)
        orr = Or(oom, b)
        paren = Parens(orr)
        zmm2 = ZeroOrMore(paren)
        tree = RegexAST(zmm2)
        nfa = tree.toNfa().determinize()
        correct = self.buildDfa3()
        self.assertTrue(nfa == correct)