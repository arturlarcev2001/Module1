from Runner_2 import *
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.run1 = Runner("Усэйн", 10)
        self.run2 = Runner("Андрей", 9)
        self.run3 = Runner("Ник", 3)

    def test_tournament_1(self):
        tour = Tournament(90, self.run1, self.run3)
        self.all_results[1] = tour.start()
        self.assertTrue(self.all_results[1][2], "Ник")
    def test_tournament_2(self):
        tour = Tournament(90, self.run2, self.run3)
        self.all_results[2] = tour.start()
        self.assertTrue(self.all_results[2][2], "Ник")
    def test_tournament_3(self):
        tour = Tournament(90, self.run1, self.run2, self.run3)
        self.all_results[3] = tour.start()
        self.assertTrue(self.all_results[3][3], "Ник")

    @classmethod
    def tearDownClass(self):
        for a in self.all_results.keys():
            print(self.all_results[a])

if __name__ == "__main__":
    unittest.main()