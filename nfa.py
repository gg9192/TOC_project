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

    """removes the given edge from the current NFA"""
    def removeEdge(self, startState:int, endState:int, char:str):
        # validate that the edge exists
        if startState in self.edges:
            if char in self.edges[startState]:
                if endState in self.edges[startState][char]:
                    #the edge exists
                    if len(self.edges[startState]) == 1:
                        # theres only 1 character in transitions from the start state
                        if len(self.edges[startState][char]) == 1:
                            # there is only one transition for this character
                            # ie, this is the only edge for the startstate
                            del self.edges[startState]
                        else:
                            # there are multiple transitions for this character
                            self.edges[startState][char].remove(endState)
                    else:
                        # there are multiple transitions from the start state
                        if len(self.edges[startState][char]) == 1:
                            # there is only one transition for this character
                            del self.edges[startState][char]
                        else:
                            # there are multiple transitions for this character
                            self.edges[startState][char].remove(endState)


                    return
        raise Exception("edge does not exist")

    """
    we can not have duplicate state names when we determinize some regexes, this function solves this problem
    the way that I generate these NFAs guarentee that states have names 1 to n where n is the number of states
    """
    def makeDisjoint(self, nfa):
        newstateid = len(self.states) + 1
        # maps the old state number to the new state number
        stateMap = {}
        for state in self.states:
            stateMap[state] = newstateid
            newstateid += 1
        
        # deal with the start states
        newstart = set()
        for state in self.startStates:
            newstart.add(stateMap[state])
        self.startStates = newstart
        
        # deal with accepting states
        newaccept = set()
        for state in self.acceptingStates:
            newaccept.add(stateMap[state])
        
        # deal witrh the edges
        for startstate in self.edges:
            for letter in self.edges[state]:
                for endstate in self.edges[state][letter]:
                    self.addEdge(stateMap[startstate], stateMap[endstate], letter)
                    self.removeEdge(startstate, endstate, letter)

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
    


