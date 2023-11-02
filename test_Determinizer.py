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
        nfa.alphabet.add("C")
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

    def buildDfa4(self):
        dfa = NFA()
        for i in range(1,7):
            dfa.setStates([i])
        dfa.setStartingStates([2])
        dfa.setAcceptingStates([3,6])
        dfa.addEdge(1,1,"A")
        dfa.addEdge(1,1,"B")
        dfa.addEdge(1,1,"C")
        dfa.addEdge(1,1,"D")
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,4,"B")
        dfa.addEdge(2,5,"C")
        dfa.addEdge(2,6,"D")
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,1,"B")
        dfa.addEdge(3,1,"C")
        dfa.addEdge(3,1,"D")
        dfa.addEdge(4,1,"A")
        dfa.addEdge(4,4,"B")
        dfa.addEdge(4,5,"C")
        dfa.addEdge(4,6,"D")
        dfa.addEdge(5,1,"A")
        dfa.addEdge(5,4,"B")
        dfa.addEdge(5,5,"C")
        dfa.addEdge(5,6,"D")
        dfa.addEdge(6,1,"A")
        dfa.addEdge(6,4,"B")
        dfa.addEdge(6,1,"A")
        dfa.addEdge(6,5,"C")
        dfa.addEdge(6,6,"D")
        return dfa


    def test_Determinized4(self):
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
        dfa = tree.toNfa().determinize()
        correct = self.buildDfa4()
        self.assertTrue(correct == dfa)
        
import unittest
from nfa import *
from regexAST import *

class TestDeterminize(unittest.TestCase):
    """
    This class tests determinizing NFAs, all test cases computed by hand
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
        nfa.alphabet.add("C")
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

    def buildDfa4(self):
        dfa = NFA()
        for i in range(1,7):
            dfa.setStates([i])
        dfa.setStartingStates([2])
        dfa.setAcceptingStates([3,6])
        dfa.addEdge(1,1,"A")
        dfa.addEdge(1,1,"B")
        dfa.addEdge(1,1,"C")
        dfa.addEdge(1,1,"D")
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,4,"B")
        dfa.addEdge(2,5,"C")
        dfa.addEdge(2,6,"D")
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,3,"A")
        dfa.addEdge(3,1,"B")
        dfa.addEdge(3,1,"C")
        dfa.addEdge(3,1,"D")
        dfa.addEdge(4,1,"A")
        dfa.addEdge(4,4,"B")
        dfa.addEdge(4,5,"C")
        dfa.addEdge(4,6,"D")
        dfa.addEdge(5,1,"A")
        dfa.addEdge(5,4,"B")
        dfa.addEdge(5,5,"C")
        dfa.addEdge(5,6,"D")
        dfa.addEdge(6,1,"A")
        dfa.addEdge(6,4,"B")
        dfa.addEdge(6,1,"A")
        dfa.addEdge(6,5,"C")
        dfa.addEdge(6,6,"D")
        return dfa


    def test_Determinized4(self):
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
        dfa = tree.toNfa().determinize()
        correct = self.buildDfa4()
        self.assertTrue(correct == dfa)
        
    def buildDfa5(self):
        dfa = NFA()
        for i in range(1,6):
            dfa.setStates([i])
        dfa.setStartingStates([2])
        dfa.setAcceptingStates([5])
        dfa.addEdge(1,1,"A")
        dfa.addEdge(1,1,"B")
        dfa.addEdge(1,1,"C")
        dfa.addEdge(2,3,"A")
        dfa.addEdge(2,1,"B")
        dfa.addEdge(2,1,"C")
        dfa.addEdge(3,4,"B")
        dfa.addEdge(3,1,"A")
        dfa.addEdge(3,1,"C")
        dfa.addEdge(4,1,"A")
        dfa.addEdge(4,1,"B")
        dfa.addEdge(4,5,"C")
        dfa.addEdge(5,1,"A")
        dfa.addEdge(5,1,"B")
        dfa.addEdge(5,1,"C")
        return dfa


        
        return dfa

    def test_Determinized5(self):
        """A B C"""
        a = Just("A")
        b = Just("B")
        c = Just("C")
        fol1 = Follows(a,b)
        fol2 = Follows(fol1, c)
        tree = RegexAST(fol2)
        dfa = tree.toNfa().determinize()
        correct = self.buildDfa5()
        assert correct == dfa
        # self.assertTrue(correct == dfa)