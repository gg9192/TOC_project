""" The purpose of this file is to contain all the classes required to build an AST for regex
    To get more detail, look at the second method.
"""
from nfa import *
# abstract class
from abc import *

class TreeElement(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def toNfa(self) -> NFA:
        pass

"""The purpose of this class is to represent parentheses in regex"""
class Parens(TreeElement):
    def __init__(self, what:TreeElement):
        self.what = what

    def __repr__(self):
        return "(" + str(self.what) + ")"
    
    "converts the regex to NFA" 
    def toNfa(self) -> NFA:
        return self.what.toNfa()

"""This represents one or more of a given regex"""
class OneOrMore(TreeElement):
    def __init__(self, what:TreeElement):
        self.what = what

    def __repr__(self):
        return str(self.what) + "+"
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa = self.what.toNfa()

        # don't connect all start states to end states (1)
        # connect all endstate to startstates (or more)
        for startstate in nfa.startStates:
            for acceptstate in nfa.acceptingStates:
                nfa.addEdge(acceptstate, startstate, None)
        
        return nfa

"""This represents zero or more of a given regex"""
class ZeroOrMore:
    def __init__(self, what:TreeElement):
        self.what = what

    def __repr__(self):
        return str(self.what) + "*"
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa = self.what.toNfa()
        newStart = len(nfa.states) + 1
        newAccept = len(nfa.states) + 2
        nfa.setStates([newStart,newAccept])

        # connect start to newStart
        for startstate in nfa.startStates:
            nfa.addEdge(newStart, startstate, None)
        
        # connect acceptings to new accepting
        for accept in nfa.acceptingStates:
            nfa.addEdge(accept, newAccept, None)

        sstart = set()
        sstart.add(newStart)
        nfa.startStates = sstart

        aacept = set()
        aacept.add(newAccept)
        nfa.acceptingStates = aacept


        
        # connect all start states to end states (0)
        for startstate in nfa.startStates:
            for acceptstate in nfa.acceptingStates:
                nfa.addEdge(startstate, acceptstate, None)

        # connect all endstate to startstates (or more)
        for startstate in nfa.startStates:
            for acceptstate in nfa.acceptingStates:
                nfa.addEdge(acceptstate, startstate, None)

        return nfa

"""This represents one regex followed by another"""
class Follows(TreeElement):
    def __init__(self, first:TreeElement, second:TreeElement):
        self.first = first
        self.second = second

    def __repr__(self):
        return str(self.first) + " " + str(self.second)
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa1 = self.first.toNfa()
        nfa2 = self.second.toNfa()
        nfa2 = nfa1.makeDisjoint(nfa2)

        # add states
        for state in nfa2.states():
            nfa1.setStates(state)

        # deal with the edges
        for startstate in nfa2.edges:
            for letter in nfa2.edges[startstate]:
                for endstate in nfa2.edges[startstate][letter]:
                    nfa1.addEdge(startstate, endstate, letter)
        
        # connect the 2
        for accepting in nfa1.acceptingStates:
            for starting in nfa2.startStates:
                nfa1.addEdge(accepting, starting, None)

        # set new accepting states
        newAccepting = set()
        for accepting in nfa2.acceptingStates:
            newAccepting.add(accepting)
        nfa1.acceptingStates = newAccepting

        return nfa1





"""This represents one regex or another"""
class Or(TreeElement):
    def __init__(self, first:TreeElement, second:TreeElement):
        self.first = first
        self.second = second

    def __repr__(self):
        return str(self.first) + " | " + str(self.second)
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa1 = self.first.toNfa()
        nfa2 = self.second.toNfa()
        print(nfa2.edges)
        nfa1.makeDisjoint(nfa2)
        # now nfa1 is disjoint
        # add states
        for state in nfa2.states:
            nfa1.setStates([state])
        # add starting states
        for state in nfa2.startStates:
            nfa1.setStartingStates([state])

        # add final states
        for state in nfa2.acceptingStates:
            nfa1.setAcceptingStates([state])
        
        
        # add edges 
        for startstate in nfa2.edges:
            print("fghx")
            for letter in nfa2.edges[startstate]:
                print("serd;lohk")
                for endstate in nfa2.edges[startstate][letter]:
                    print(letter)
                    nfa1.addEdge(startstate, endstate, letter)
        return nfa1
        
        
        
    
class Just(TreeElement):
    def __init__(self, what:str):
        self.what = what
    
    def __repr__(self):
        return str(self.what)
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa = NFA()
        nfa.setStates([1,2])
        nfa.setStartingStates([1])
        nfa.setAcceptingStates([2])
        nfa.addEdge(1,2,self.what)
        return nfa


"""This is the class for an abstract syntax tree for regex"""
class RegexAST():
    def __init__(self, root:TreeElement):
        self.root = root

    def __repr__(self):
        return str(self.root) #recursion
    
    def toNfa(self) -> NFA:
        return self.root.toNfa()

