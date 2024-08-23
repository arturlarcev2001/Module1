from Runner_2 import *
from RunnerTest import RunnerTest
from TournamentTest import TournamentTest
import unittest

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

testtest = unittest.TextTestRunner(verbosity=2)
testtest.run(runnerST)