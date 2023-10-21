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

    """this assumes you have graphviz installed.
       outputs both a png and a gv file
       the id is for a uniqueid
    """
    def convertToImage(self, id:int):
        dot = graphviz.Digraph(name = "nfa", )
        #create a hidden start node, this helps us point to the start state
        dot.node(name ="Start",label="", shape="none")
        # lets first deal with the start states
        for state in self.startStates:
            dot.node(str(state))
        dot.render("nfa_" + str(id) + ".gv", format = "png")
    

os.chdir("./images")
for file in os.listdir():
    os.remove(file)

nfa = NFA()
nfa.setStates([1,2,3,4,5])
nfa.setStartingStates([1,3])
nfa.convertToImage(1)



        
