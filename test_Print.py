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

    def buildGraph1(self):
        nfa = NFA()
        nfa.setStates([1,2,3,4])
        nfa.setStartingStates([1,3])
        nfa.setAcceptingStates([4,2])
        return nfa

        


    def test_graph1(self):
        nfa = self.buildGraph1()
        nfa.convertToImage(1)
        self.assertTrue(True)        
