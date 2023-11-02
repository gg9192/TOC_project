import unittest
from regexAST import *

class TestRegex1(unittest.TestCase):
    """(A | B)*"""
    def getAST1(self):
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        p = Parens(orr)
        zom = ZeroOrMore(p) 
        ast = RegexAST(zom)
        return ast
    
    def test_Accepting1(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        b = dfa.runString("")
        self.assertTrue(b)

    def test_Accepting2(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        b = dfa.runString("ABABBABABABABABBB")
        self.assertTrue(b)
    
    def test_Accepting3(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        b = dfa.runString("BABABAABAABBABAABBABAB")
        self.assertTrue(b)

    def testRejecting1(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        b = dfa.runString("BABABAABCAABBABAABBABAB")
        self.assertTrue(b == False)

    def testRejecting2(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        dfa.convertToImage(134)
        b = dfa.runString("BABABAABAABCBABAACCBBABAB")
        self.assertTrue(b == False)
        
    def testRejecting3(self):
        ast = self.getAST1()
        nfa = ast.toNfa()
        nfa.alphabet.add("C")
        dfa = nfa.determinize()
        b = dfa.runString("BABABAABAABBABACABBABAB")
        self.assertTrue(b == False)

class testRegex2(unittest.TestCase):
    """((A | B)+ D| C)+"""
    def getAST2(self):
        a = Just("A")
        b = Just("B")
        orr = Or(a,b)
        innerParen = Parens(orr)
        oom = OneOrMore(innerParen)
        c = Just("C")
        d = Just("D")
        follows = Follows(oom,d)
        orr2 = Or(follows, c)
        outerparens = Parens(orr2)
        oom2 = OneOrMore(outerparens)
        tree = RegexAST(oom2)
        return tree
    
    def test_Accepting1(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABABDBDC")
        self.assertTrue(b)

    def test_Accepting2(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABABDCBD")
        self.assertTrue(b)

    def test_Accepting3(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABDCCCCABAD")
        self.assertTrue(b)

    def test_Rejecting1(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("")
        self.assertTrue(b == False)

    def test_Rejecting2(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABABABDABABC")
        self.assertTrue(b == False)

    def test_Rejecting3(self):
        ast = self.getAST2()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABDCCCABABDABABCCD")
        self.assertTrue(b == False)

class testRegex3(unittest.TestCase):
    """# (A+ D | B)*"""
    def getAST3(self):
        a = Just("A")
        b = Just("B")
        oom = OneOrMore(a)
        d = Just("D")
        fol = Follows(oom,d)
        orr = Or(fol, b)
        paren = Parens(orr)
        zmm2 = ZeroOrMore(paren)
        tree = RegexAST(zmm2)
        return tree

    def test_Accepting1(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("")
        self.assertTrue(b)

    def test_Accepting2(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAADADADB")
        self.assertTrue(b)

    def test_Accepting3(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAAD")
        self.assertTrue(b)

    def test_Rejecting1(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAA")
        self.assertTrue(b == False)

    def test_Rejecting2(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAABBBD")
        self.assertTrue(b == False)

    def test_Rejecting3(self):
        ast = self.getAST3()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("DAD")
        self.assertTrue(b == False)

class testRegex4(unittest.TestCase):

    def getAST4(self):
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
        return tree
    
    def test_Accepting1(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("D")
        self.assertTrue(b)

    def test_Accepting2(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("BCBCCCCCBCD")
        self.assertTrue(b)

    def test_Accepting3(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAAAA")
        self.assertTrue(b)

    def test_Rejecting1(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("AAAAAB")
        self.assertTrue(b == False)

    def test_Rejecting2(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("DB")
        self.assertTrue(b == False)

    def test_Rejecting3(self):
        ast = self.getAST4()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("")
        self.assertTrue(b == False)
    
class testRegex5(unittest.TestCase):
    """A B C"""
    def getAST5(self):
        """A B C"""
        a = Just("A")
        b = Just("B")
        c = Just("C")
        fol1 = Follows(a,b)
        fol2 = Follows(fol1, c)
        tree = RegexAST(fol2)
        return tree
    
    def test_Accept1(self):
        ast = self.getAST5()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABC")
        self.assertTrue(b)

    def test_reject1(self):
        ast = self.getAST5()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ABCAA")
        self.assertTrue(b == False)

    def test_reject2(self):
        ast = self.getAST5()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("CCABC")
        self.assertTrue(b == False)

    def test_reject3(self):
        ast = self.getAST5()
        nfa = ast.toNfa()
        dfa = nfa.determinize()
        b = dfa.runString("ACBC")
        self.assertTrue(b == False)
