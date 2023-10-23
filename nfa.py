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
        self.alphabet = set()
        self.alphabet.add(None)
    
    """sets the starting states"""
    def setStartingStates(self, states:list):
        for state in states:
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.startStates.add(state)
    
    """Adds the given edge"""
    def addEdge(self, sourceState:int, destState:int,  char:str):
        if char not in self.alphabet:
            self.alphabet.add(char)
        if sourceState in self.edges:
            if char in self.edges[sourceState]:
                self.edges[sourceState][char].add(destState)
            else:
                s = set()
                s.add(destState)
                self.edges[sourceState][char] = s
        else:
            mapp = {}
            s = set()
            s.add(destState)
            mapp[char] = s
            self.edges[sourceState] = mapp

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
        graphviz.charset = 'utf-8'
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
                for endstate in self.edges[state][letter]:
                    if letter == None:
                        dot.edge(str(state), str(endstate), label="ϵ")
                    else:
                        dot.edge(str(state), str(endstate), label=letter)
        
        dot.render("./images/nfa_" + str(id) + ".gv", format = "png")
    



        
