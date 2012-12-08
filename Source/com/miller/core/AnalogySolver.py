'''
Created on 19-Nov-2012

@author: koolkid
'''
from Source.com.miller.utils.AnalogySolverHelper import PropositionalSolver
from Source.com.miller.utils.AnalogySolverHelper import VisualSolver

class Solver:

    @staticmethod
    def propositionalAnswers(num):
        answers = []
        numberOfProblems = num
        for i in range(1,(numberOfProblems+1)):
            answer = PropositionalSolver(i).solveProblem()
            print "Answer to the problem ", i," is ", str(answer)
            answers.append(answer)
        return answers
    
    @staticmethod
    def visualAnswers(num):
        answers = []
        numberOfProblems = num
        for i in range(1,(numberOfProblems+1)):
            answer = VisualSolver(i).solveProblem()
            print "Answer to the problem ", i," is ", str(answer)
            answers.append(answer)
        return answers
