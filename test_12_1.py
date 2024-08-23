from Runner import *
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Igor")
        for _ in range(10): runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Maksim")
        for _ in range(10): runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner("Viktor")
        runner_2 = Runner("Joshua")
        for _ in range(10): runner.run()
        for _ in range(10): runner_2.walk()
        self.assertNotEqual(runner.distance, runner_2.distance)

if __name__ == "__main__":
    unittest.main()