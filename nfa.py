import graphviz 
from typing import Optional

class NFA():
    """This class represents an NFA"""
    def __init__(self):
        # Nested hashmap, first we give the startstate, then we give the letter. We get the destsate
        self.edges = {}
        self.startStates = set()
        self.acceptingStates = set()
        self.states = set()
        self.alphabet = set()
        self.alphabet.add(None)
        self.determinized = False
    
    def __eq__(self, nfa) -> bool:
        print(self.acceptingStates,nfa.acceptingStates)
        acceptingStates = self.acceptingStates == nfa.acceptingStates
        startStates = self.startStates == nfa.startStates
        states = self.states == nfa.states
        alphabet = self.alphabet == nfa.alphabet
        edges = self.edges == nfa.edges
        if self.edges != nfa.edges:
            for start in nfa.edges:
                for char in nfa.edges[start]:
                    for end in nfa.edges[start][char]:
                        if end not in self.edges[start][char]:
                            raise Exception(start, char, end)
        return acceptingStates and startStates and states and alphabet and edges

    def setStartingStates(self, states:list):
        """sets the starting states"""
        for state in states:
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.startStates.add(state)
    
    
    def addEdgeToNew(sourceState:int, destState:int,  char:str, newEdges:dict, newAlphabet: set):
        """Adds the given edge to the dictionary, and update the new alphabet set"""

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

    
    
    def addEdge(self, sourceState:int, destState:int,  char:str):
        """Adds the given edge to the NFA"""
        if sourceState not in self.states or destState not in self.states:
            raise Exception("Source or dest not in edges, can't add edge")
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

    
    def makeDisjoint(self, nfa):
        """
        we can not have duplicate state names when we determinize some regexes, this function solves this problem
        the way that I generate these NFAs guarentee that states have names 1 to n where n is the number of states
        """
        newstateid = len(self.states) + 1
        # maps the old state number to the new state number
        stateMap = {}

        # set iteration is random, if we want to test this, we need to ensure that the new state names
        # are assigned to the same states every time 
        states = list(nfa.states)
        states.sort()
        for state in states:
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


    
    def setStates(self, states:list):
        """sets the states of the NFA"""
        for state in states:
            self.states.add(state)
    
    def setAcceptingStates(self,states:list):
        """sets the accepting states"""
        for state in states:
            if state not in self.states:
                raise Exception("Starting states must be a subset of states, perhaps you didn't set your states first")
            self.acceptingStates.add(state)

    def convertToImage(self, id:int):
        """this assumes you have graphviz installed.
        outputs both a png and a gv file
        the id is for a uniqueid
        """
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
                    if startstate not in self.states or endstate not in self.states:
                        raise Exception("Start or end state does not exist, can not draw!")
                    # epsilon
                    if letter == None:
                        dot.edge(str(startstate), str(endstate), label="ϵ")
                    else:
                        dot.edge(str(startstate), str(endstate), label=letter)
        
        dot.render("./images/nfa_" + str(id) + ".gv", format = "png")
    
    def gri(self,state:int, char:str)-> set:
            """gets the relational image for 1 character and number"""
            if char in self.edges[state]:
                return self.edges[state][char]
            else:
                return set()
    
    def getRelationalImage(self, state:set, char:str) -> Optional[set]:
        """gets the relational image for 1 character and set of states"""
        s = set()
        for i in state:
            temp = self.gri(i,char)
            s = temp.union(s)
        return s if len(s) != 0 else None
        

    def determinize(self):
        # this is the best I can do for private methods, none of the sub-methods can be accessed outside of the method
        """determinizes the NFA"""
        
        def stateToID(state:set) -> int:
            """
            converts a given state to the int id associated with the state
            returns a negative number if no state was found
            """
            i = 0
            for statee in states:
                if statee == state:
                    return i + 1
                else:
                    i += 1

            raise Exception("State not found: " + str(state) + " " + str(states))

        def closureHelper(state:int, active:set):
            """DFS recursive solution with caching"""
            active.add(state)
            returnset = set()
            returnset.add(state)
            
            if None in self.edges[state]:
                for endstate in self.edges[state][None]:
                    # prevent infinate recursion
                    if endstate not in active:
                        tempset = closureHelper(endstate,active)
                        returnset = returnset.union(tempset)
                    else:
                        # note that we can reach the state in the returnset for a correct cache
                        returnset.add(endstate)
            return returnset
            

        def gec(state:int) -> set:
            """getEpsilonClosure but for 1 state"""
            active = set()
            return closureHelper(state, active)
        
        def getEpsilonClosure(state: Optional[set]) -> Optional[set]:
            """
            Gets the epsilon closure of a given set of states
            """
            if state == None:
                return None
            s = set()
            for i in state:
                if i in epsiloncache:
                    print("CACHE HIT")
                    temp = epsiloncache[i]
                    s = s.union(temp)
                else:
                    temp = gec(i)
                    epsiloncache[i] = temp
                    s = s.union(temp)
            return s

        def addState(state:set, dfa) -> int:
            """Given the state as a set, add the state to the dfa and states array, returns the int id of the set"""
            states.append(state)
            i = stateToID(state)
            dfa.setStates([i])
            return i
        
        def printStateMap():
            """prints the current maping of state id to set"""
            for i in range(0, len(states)):
                print(i + 1, states[i])
        
        def buildDFAHelper(startState:set, dfa, alphabet:list):
            """dfa helper """

            # set iteration is random, if we want to test this, we need to ensure that the new state names
            
            for char in alphabet:
                if char == None:
                    # skip epsilon
                    continue
                state = getEpsilonClosure(self.getRelationalImage(startState,char))
                if state in states:
                    # we already have explored this state, don't recurse
                    source = stateToID(startState)
                    dest = stateToID(state)
                    dfa.addEdge(source, dest, char)
                else:
                    dest = addState(state, dfa)
                    source = stateToID(startState)
                    dfa.addEdge(source, dest, char)
                    buildDFAHelper(state,dfa, alphabet)
                

        def buildDFA(startState:set):
            # are assigned to the same states every time 
            alphabet = list(self.alphabet)
            alphabet.remove(None)
            alphabet.sort()
            alphabet = [None] + alphabet
            """this function builds the DFA, given the start state"""
            dfa = NFA()
            dfa.setStates([1])
            start = getEpsilonClosure(self.startStates)
            startID = addState(start, dfa)
            dfa.setStartingStates([startID])
            for char in self.alphabet:
                if char == None:
                    continue
                dfa.addEdge(stateToID(None), stateToID(None), char)
            buildDFAHelper(start, dfa, alphabet)
            return dfa

        def isAcceptingState(state:set) -> bool:
            """given a state as a set of states, 
            determine if its a accepting state"""
            for i in state:
                if i in self.acceptingStates:
                    return True
            return False
        
        def removeNullIfNeeded(dfa) -> None:
            """given a dfa"""
            for startstate in dfa.edges:
                for char in dfa.edges[startstate]:
                    for endstate in dfa.edges[startstate][char]:
                        if endstate == 1 and startstate != 1:
                            return
            dfa.states.remove(1)
            del dfa.edges[1]

            

        # unfortunatly, we can't hash a set, represent sets of states as list of sets
        # in the edges hashmap, the index of the state is the id - 1, see state to ID
        states = [None]
        # maps state:int to cached set of epsilon closure
        epsiloncache = {}
        
        dfa = buildDFA(self.startStates)
        i = 0
        for state in states:
            if state == None:
                i += 1
                continue
            if isAcceptingState(state):
                dfa.setAcceptingStates([i + 1])
            i += 1
        printStateMap()
        removeNullIfNeeded(dfa)
        print(epsiloncache)
        return dfa
        
        