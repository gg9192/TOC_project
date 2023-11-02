# TOC_project
Authors: Alex Guo

Tooling: Python
    - pip install pytest
    - pip install graphvis

Sources: 
nfa.py contains a class definition for an NFA
regexAST contains classes for a regex ast
test_*.py contains unit tests

Required functions: list and briefly describe the functions you wrote to satisfy the various
parts of the project (as listed above, in their respective sections)

1. Define a datatype (in whatever language you are using) for representing regular expressions.
[10 points]
See regexAST and object object methods

2. Define a datatype for representing nondeterministic finite automata with epsilon-transitions
(as this format is used for the first step of translating regular expressions). [15 points]
See NFA.py and associated object methods

3. Write a printing function that can generate a GraphViz file for the transition diagram of an
automaton as implemented in the previous step. I am providing a sample GraphViz file for
an automaton, for inspiration. You can render such files using online tools like
This is dfa1.gv (rendered in dfa1.pdf). [15 points]
See nfa.convertToImage()

4. Write a function to translate regular expressions into finite automata. [60 points]
See TreeElement.toNfa() in regexAST

5. Now write a function that can determinize a finite automaton. You can just take in an
automaton of the type you defined, and generate a new one of those automata, where the
transition relation is nondeterministic: no epsilon-transitions, and exactly one outgoing edge
with each character of the input alphabet, for each state. The advantage of this approach is
that you do not need to define a new datatype for DFAs. Just use the original datatype for
NFAs, but use the subset construction to eliminate all nondeterminism. [50 points]
See NFA.determinize() and associated helper methods

Status: Are all your functions working correctly, or are some incomplete or have bugs that
you know of? Please give us your assessment, to help us as we review your code (so we don’t
waste time trying to puzzle out how something is working if it is incomplete or buggy).

No errors that I am aware 