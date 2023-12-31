import unittest
from regexAST import *
from nfa import *


class RegexToNFA(unittest.TestCase):
    """All tests for regex to NFA, all testcases handbuilt/tested for correcness"""
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
        return nfa

    
    
    def test_regextoNFA1(self):
        """(A | B)*"""
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
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
            return nfa

    
    def test_regextoNFA2(self):
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
        nfa = tree.toNfa()
        nfa = tree.toNfa()
        
        correct = self.buildNFA2()
        self.assertTrue(correct == nfa)

    def buildNFA3(self):
        nfa = NFA()
        nfa.setStates([1,2,3,4,5,6,7,8])
        nfa.startStates.add(7)
        nfa.acceptingStates.add(8)
        nfa.addEdge(7,3,None)
        nfa.addEdge(7,5,None)
        nfa.addEdge(3,1,None)
        nfa.addEdge(1,2,"A")
        nfa.addEdge(2,4,None)
        nfa.addEdge(4,8,None)
        nfa.addEdge(4,3,None)
        nfa.addEdge(5,6,"B")
        nfa.addEdge(6,8,None)
        nfa.addEdge(8,7,None)
        nfa.addEdge(7,8,None)
        return nfa
        

    
    def test_regextoNFA3(self):
        """# (A+| B)*"""
        a = Just("A")
        b = Just("B")
        oom = OneOrMore(a)
        orr = Or(oom, b)
        paren = Parens(orr)
        zmm2 = ZeroOrMore(paren)
        tree = RegexAST(zmm2)
        nfa = tree.toNfa()
        correct = self.buildNFA3()
        self.assertTrue(correct == nfa)
        
    def buildNFA4(self):
        nfa = NFA()
        
        # set the states
        for i in range(1,15):
            nfa.setStates([i])

        # set the starting state
        nfa.setStartingStates([3,13])
        nfa.setAcceptingStates([4,14])
        nfa.addEdge(3,1,None)
        nfa.addEdge(1,2,"A")
        nfa.addEdge(2,4,None)
        nfa.addEdge(4,3,None)
        nfa.addEdge(13,9,None)
        nfa.addEdge(9,5,None)
        nfa.addEdge(9,7,None)
        nfa.addEdge(5,6,"B")
        nfa.addEdge(7,8,"C")
        nfa.addEdge(6,10,None)
        nfa.addEdge(8,10,None)
        nfa.addEdge(9,10,None)
        nfa.addEdge(10,9,None)
        nfa.addEdge(10,11,None)
        nfa.addEdge(11,12,"D")
        nfa.addEdge(12,14,None)
        nfa.addEdge(14,13,None)
        return nfa

    def test_regextoNFA4(self):
        """A+ | ((B | C)* D)+"""
        a = Just("A")
        b = Just("B")
        c = Just("C")
        d = Just("D")
        aplus = OneOrMore(a)
        borc = Or(b,c)
        innerparen = Parens(borc)
        zom = ZeroOrMore(innerparen)
        follows = Follows(zom,d)
        outerparen = Parens(follows)
        oor = OneOrMore(outerparen) 
        bigOr = Or(aplus, oor)
        tree = RegexAST(bigOr)
        nfa = tree.toNfa()
        correct = self.buildNFA4()
        self.assertTrue(correct == nfa)

    def buildNFA5(self):
        nfa = NFA()
        for i in range(1,7):
            nfa.setStates([i])
        nfa.setStartingStates([1])
        nfa.setAcceptingStates([6])
        nfa.addEdge(1,2,"A")
        nfa.addEdge(2,3,None)
        nfa.addEdge(3,4,"B")
        nfa.addEdge(4,5,None)
        nfa.addEdge(5,6,"C")     
        return nfa

    
    def test_regextoNFA5(self):
        """A B C"""
        a = Just("A")
        b = Just("B")
        c = Just("C")
        fol1 = Follows(a,b)
        fol2 = Follows(fol1, c)
        tree = RegexAST(fol2)
        nfa = tree.toNfa()
        correct = self.buildNFA5()
        self.assertTrue(nfa == correct)