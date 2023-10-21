import graphviz 
import os
"""This class represents"an NFA"""
class NFA():
    def __init__(self):
        # Nested hashmap, first 
        self.edges = {}
        self.startStates = set()
        self.acceptingStates = set()
        self.states = set()
    
    """sets the starting states"""
    def setStartingStates(self, states:list):
        for state in states:
            self.startStates.add(state)
    
    """Adds the given edge"""
    def addEdge(self, state:int, char:str):
        if state in self.edges:
            self.edges[state].add(char)
        else:
            s = set()
            s.add(char)
            self.edges[state] = s

    """sets the states"""
    def setStates(self, states:list):
        for state in states:
            self.states.add(state)

    def convertToDot():
        pass
    
    



        
