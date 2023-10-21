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
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.startStates.add(state)
    
    """Adds the given edge"""
    def addEdge(self, sourceState:int, destState:int,  char:str):
        if sourceState in self.edges:
            self.edges[sourceState][char] = destState
        else:
            s = {}
            s[char] = destState
            self.edges[sourceState] = s

    """sets the states"""
    def setStates(self, states:list):
        for state in states:
            self.states.add(state)

    """sets the accepting states"""
    def setAcceptingStates(self,states:list):
        for state in states:
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.acceptingStates.add(state)
        

    """this assumes you have graphviz installed.
       outputs both a png and a gv file
       the id is for a uniqueid
    """
    def convertToImage(self, id:int):
        dot = graphviz.Digraph(name = "nfa", )
        #create a hidden start node, this helps us point to the start state
        dot.node(name ="Start",label="", shape="none")
        # lets first create our states
        for state in self.states:
            #check if its an accepting state
            if state in self.acceptingStates:
                dot.node(name=str(state), label=str(state), shape="circle")
            else:
                dot.node(name=str(state), label=str(state), shape="plaintext")        
        # set the start states
        for state in self.startStates:
            dot.edge("Start", str(state))
        # add the edges
        for state in self.edges:
            for letter in self.edges[state]:
                print(letter)
                print(str(state), self.edges[state][letter])
                dot.edge(str(state), str(self.edges[state][letter]), label=letter)
        
        dot.render("nfa_" + str(id) + ".gv", format = "png")
    

os.chdir("./images")
for file in os.listdir():
    os.remove(file)

nfa = NFA()
nfa.setStates([1,2,3,4,5])
nfa.setStartingStates([1,3])

nfa.addEdge(1,3,"A")
nfa.setAcceptingStates([4,5]);
nfa.convertToImage(1)



        
