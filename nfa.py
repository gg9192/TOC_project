import graphviz 
import os
"""This class represents"an NFA"""
class NFA():
    def __init__(self):
        # Nested hashmap, first we give the startstate, then we give the letter. We get the destsate
        self.edges = {}
        self.startStates = set()
        self.acceptingStates = set()
        self.states = set()
        self.alphabet = set()
        self.alphabet.add(None)
        self.determinized = False
    
    

    """sets the starting states"""
    def setStartingStates(self, states:list):
        for state in states:
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.startStates.add(state)
    
    """Adds the given edge to the dictionary, and update the new alphabet set"""
    def addEdgeToNew(sourceState:int, destState:int,  char:str, newEdges:dict, newAlphabet: set):
        if char not in newAlphabet:
            # add the character to the alphabet
            newAlphabet.add(char)
        if sourceState in newEdges:
            # if we have the sourcestate in the edges
            if char in newEdges[sourceState]:
                # if we have outgoing edges with the same character from the sourcs state
                newEdges[sourceState][char].add(destState)
            else:
                s = set()
                s.add(destState)
                newEdges[sourceState][char] = s
        else:
            # if dont have the sourcestate in the edges
            mapp = {}
            s = set()
            s.add(destState)
            mapp[char] = s
            newEdges[sourceState] = mapp

    
    """Adds the given edge to the NFA"""
    def addEdge(self, sourceState:int, destState:int,  char:str):
        if char not in self.alphabet:
            # add the character to the alphabet
            self.alphabet.add(char)
        if sourceState in self.edges:
            # if we have the sourcestate in the edges
            if char in self.edges[sourceState]:
                # if we have outgoing edges with the same character from the sourcs state
                self.edges[sourceState][char].add(destState)
            else:
                s = set()
                s.add(destState)
                self.edges[sourceState][char] = s
        else:
            # if dont have the sourcestate in the edges
            mapp = {}
            s = set()
            s.add(destState)
            mapp[char] = s
            self.edges[sourceState] = mapp

    """
    we can not have duplicate state names when we determinize some regexes, this function solves this problem
    the way that I generate these NFAs guarentee that states have names 1 to n where n is the number of states
    """
    def makeDisjoint(self, nfa):
        newstateid = len(self.states) + 1
        # maps the old state number to the new state number
        stateMap = {}
        for state in nfa.states:
            stateMap[state] = newstateid
            newstateid += 1
        
        # deal with the start states
        newstart = set()
        for state in nfa.startStates:
            newstart.add(stateMap[state])
        nfa.startStates = newstart
        # deal with accepting states
        newaccept = set()
        for state in nfa.acceptingStates:
            newaccept.add(stateMap[state])
        nfa.acceptingStates = newaccept
        print(str(nfa.edges) + "asdfsegfzsef")
        newAlphabet = set()
        newEdges = {}
        # deal with the edges
        for startstate in nfa.edges:
            for letter in nfa.edges[startstate]:
                for endstate in nfa.edges[startstate][letter]:
                    NFA.addEdgeToNew(stateMap[startstate], stateMap[endstate], letter, newEdges, newAlphabet)
                    
        nfa.alphabet = newAlphabet
        nfa.edges = newEdges
        

        # deal with states
        newStates = set()
        for state in nfa.states:
            newStates.add(stateMap[state])
        nfa.states = newStates
        return nfa


    """sets the states of the NFA"""
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
        for startstate in self.edges:
            for letter in self.edges[startstate]:
                for endstate in self.edges[startstate][letter]:
                    # check error states
                    if letter not in self.alphabet:
                        raise Exception("The letter is not in the alphabet, can not draw!")
                    if state not in self.states or endstate not in self.states:
                        raise Exception("Start or end state does not exist, can not draw!")
                    # epsilon
                    if letter == None:
                        dot.edge(str(startstate), str(endstate), label="ϵ")
                    else:
                        dot.edge(str(startstate), str(endstate), label=letter)
        
        dot.render("./images/nfa_" + str(id) + ".gv", format = "png")
    


