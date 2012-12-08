'''
Created on 20-Nov-2012

@author: koolkid
'''

from Source.com.miller.core.AnalogySolver import Solver

numberOfProblems = 12
visualAnswers = Solver.visualAnswers(numberOfProblems)
propositionalAnswers = Solver.propositionalAnswers(numberOfProblems)

print "------------Summary for the Visual Method--------------------"
for i in range(0, numberOfProblems):
    print "Solution for Problem(",str(i+1),") is ", visualAnswers[i]
print "----------------------------------------"

print "------------Summary for the Propositional Method--------------------"
for i in range(0, numberOfProblems):
    print "Solution for Problem(",str(i+1),") is ", propositionalAnswers[i]
print "----------------------------------------"
