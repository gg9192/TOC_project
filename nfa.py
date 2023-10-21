"""This class represents"an NFA"""

class NFA():
    def __init__(self):
        self.edges = {}
        self.startnodes = set()
        self.acceptingStates()
        self.states = set()