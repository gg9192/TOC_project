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
    def toNfa() -> NFA:
        pass

"""This represents zero or more of a given regex"""
class ZeroOrMore:
    def __init__(self, what:TreeElement):
        self.what = what

    def __repr__(self):
        return str(self.what) + "*"
    
    "converts the regex to NFA"
    def toNfa() -> NFA:
        pass

"""This represents one regex followed by another"""
class Follows(TreeElement):
    def __init__(self, first:TreeElement, second:TreeElement):
        self.first = first
        self.second = second

    def __repr__(self):
        return str(self.first) + " " + str(self.second)
    
    "converts the regex to NFA"
    def toNfa() -> NFA:
        pass

"""This represents one regex or another"""
class Or(TreeElement):
    def __init__(self, first:TreeElement, second:TreeElement):
        self.first = first
        self.second = second

    def __repr__(self):
        return str(self.first) + " | " + str(self.second)
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa1 = self.first.toNFA()
        nfa2 = self.second.toNFA()
        nfa2 = nfa1.makeDisjoint(nfa2)
        # add states
        for state in nfa2.states():
            nfa1.setStates(state)

        # add starting states
        for state in nfa2.startStates():
            nfa1.setStartingStates(state)

        # add final states
        for state in nfa2.acceptingStates:
            nfa2.setAcceptingStates(state)
        
        # add edges 
        for startstate in nfa2.edges:
            for letter in nfa2.edges[startstate]:
                for endstate in nfa2.edges[startstate][letter]:
                    nfa1.addEdge(startstate, endstate, letter)
        return NFA1        
        
        
        
    
class Just(TreeElement):
    def __init__(self, what:TreeElement):
        self.what = what
    
    def __repr__(self):
        return str(self.char)
    
    "converts the regex to NFA"
    def toNfa(self) -> NFA:
        nfa = NFA()
        nfa.setStates([1,2])
        nfa.setStartingStates([1])
        nfa.setAcceptingStates([2])
        nfa.addEdge(1,2,self.char)


"""This is the class for an abstract syntax tree for regex"""
class RegexAST():
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root) #recursion
    
    def toNfa(self) -> NFA:
        return self.root.toNFA()

