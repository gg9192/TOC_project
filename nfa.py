"""This class represents"an NFA"""

class NFA():
    def __init__(self):
        self.edges = {}
        self.startStates = set()
        self.acceptingStates = set()
        self.states = set()
    
    "sets the starting states"
    def setStartingStates(self, states:list):
        for state in states:
            self.startStates.add(state)
    
    def addEdge(self, state:int, char):
        pass

print(type('c'))
