import unittest
from nfa import *
import os
"""This class draws NFAs to test, responsibility is on the user
   To verify correctness
"""
class DrawGraphs (unittest.TestCase):
   
    """Removes all files from output dir"""
    @classmethod
    def setup_class():
        os.chdir("./images")
        ls = os.listdir()
        for file in ls:
            os.remove(file)
        os.chdir("..")

    """
    Builds the following NFA:
    Q = {1,2,3,4}
    Alphabet = {a,b,c}
    R(a) = {(1,3),(2,4),(4,1),(2,3)}
    R(b) = {(2,3),(4,2),(1,4)}
    R(c) = {(2,4),(1,2),(3,4)}
    s = {1,3}
    f = {2,4}
    """
    def buildGraph1(self):
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
        print(nfa.edges)
        self.assertTrue(True)        
