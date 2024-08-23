from Runner_2 import *
from test_12_1 import RunnerTest
from test_12_2 import TournamentTest
import unittest

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

testtest = unittest.TextTestRunner(verbosity=2)
testtest.run(runnerST)