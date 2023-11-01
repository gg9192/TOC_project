import unittest
from nfa import *
import os

class DrawGraphs (unittest.TestCase):
    
    def buildGraph1(self):
        """
        Builds the following NFA:
        Q = {1,2,3,4}
        Alphabet = {a,b,c}
        R(a) = {(1,3),(2,4),(4,1),(2,3)}
        R(b) = {(2,3),(4,2),(1,4)}
        R(c) = {(2,4),(1,2),(3,4)}
        s = {1,3}
        f = {2,4}
        correct
        """
        nfa = NFA()
        nfa.setStates([1,2,3,4])
        nfa.setStartingStates([1,3])
        nfa.setAcceptingStates([4,2])
        for start, dest in {(1,3),(2,4),(4,1),(2,3)}:
            nfa.addEdge(start,dest,"a")
        for start, dest in {(2,3),(4,2),(1,4)}:
            nfa.addEdge(start,dest,"b")
        for start, dest in {(2,4),(1,2),(3,4)}:
            nfa.addEdge(start,dest,"c")
        return nfa

    def test_graph1(self):
        nfa = self.buildGraph1()
        nfa.convertToImage(1)
        self.assertTrue(True)  
    
    
    def buildGraph2(self):
        """
        Builds the following NFA:
        Q = {1,2,3}
        Alphabet = {a,b,c}
        R(a) = {(1,1),(1,2),(1,3)}
        R(b) = {(2,1),(2,2),(2,3)}
        R(c) = {(3,1),(3,2),(3,3)}
        s = {1,3}
        f = {2}
        correct
        """
        nfa = NFA()
        nfa.setStates([1,2,3])
        nfa.setStartingStates([1,3])
        nfa.setAcceptingStates([2])
        for start, dest in {(1,1),(1,2),(1,3)}:
            nfa.addEdge(start,dest,"a")
        for start, dest in {(2,1),(2,2),(2,3)}:
            nfa.addEdge(start,dest,"b")
        for start, dest in {(3,1),(3,2),(3,3)}:
            nfa.addEdge(start,dest,"c")
        return nfa    
    
    def test_graph2(self):
        nfa = self.buildGraph2()
        nfa.convertToImage(2)
        self.assertTrue(True) 

    
    def buildGraph3(self):
        """
        Builds the following NFA:
        Q = {1,2,3}
        Alphabet = {a,b}
        R(a) = {(1,2),(3,4)}
        R(b) = {(4,1),(2,2)}
        R(c) = {(3,2),(3,3)}
        s = {1,2}
        f = {3}
        correct
        """
        nfa = NFA()
        nfa.setStates([1,2,3])
        nfa.setStartingStates([1,2])
        nfa.setAcceptingStates([3])
        for start, dest in {(1,2),(3,1)}:
            nfa.addEdge(start,dest,"a")
        for start, dest in {(2,1),(2,2)}:
            nfa.addEdge(start,dest,"b")
        for start, dest in {(3,2),(3,3)}:
            nfa.addEdge(start,dest,"c")
        return nfa    
    
    def test_graph3(self):
        nfa = self.buildGraph3()
        nfa.convertToImage(3)
        self.assertTrue(True) 



    
    def buildGraph4(self):
        """
        Tests Epsilon transitions can be rendered correctly
        Builds the following NFA:
        Q = {1,2,3}
        Alphabet = {}
        R(ϵ) = {(1,2),(2,3),(3,4)}
        s = {1,2}
        f = {3}
        """
        nfa = NFA()
        nfa.setStates([1,2,3])
        nfa.setStartingStates([1,2])
        nfa.setAcceptingStates([3])
        for start, dest in {(1,2),(2,3),(3,1)}:
            nfa.addEdge(start,dest,"ϵ")
        return nfa    
    
    def test_graph4(self):
        nfa = self.buildGraph4()
        nfa.convertToImage(4)
        self.assertTrue(True) 

    
    def buildGraph5(self):
        """
        Tests Epsilon transitions in graph
        Builds the following NFA:
        Q = {1,2,3}
        Alphabet = {a,b}
        R(a) = {(1,2),(3,1)}
        R(b) = {(3,1),(1,2)}:
        R(ϵ) = {(3,2),(1,3)}
        s = {1,2}
        f = {3}
        correct
        """
        nfa = NFA()
        nfa.setStates([1,2,3])
        nfa.setStartingStates([1,2])
        nfa.setAcceptingStates([3])
        for start, dest in {(3,2),(1,3)}:
            nfa.addEdge(start,dest,"ϵ")
        for start, dest in {(3,1),(1,2)}:
            nfa.addEdge(start,dest,"b")
        for start, dest in {(1,2),(3,1)}:
            nfa.addEdge(start,dest,"a")
        return nfa

    def test_graph5(self):
        nfa = self.buildGraph5()
        nfa.convertToImage(5)
        self.assertTrue(True) 