from rt_with_exceptions import *
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Jack', -5)
            for _ in range(10): runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" успешно выполнен')
        except:
            logging.warning(f"Неверная скорость для Runner", exc_info=2)

    def test_run(self):
        try:
            runner = Runner(123)
            for _ in range(10): runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=2)
            

    def test_challenge(self):
        runner = Runner("Viktor")
        runner_2 = Runner("Joshua")
        for _ in range(10): runner.run()
        for _ in range(10): runner_2.walk()
        self.assertNotEqual(runner.distance, runner_2.distance)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", 
    filename="runner.test.log", encoding="UTF-8", format="%(asctime)s | %(levelname)s | %(message)s")

    unittest.main(verbosity=2)

