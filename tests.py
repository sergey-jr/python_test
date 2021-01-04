import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        statuses = main.main()
        print(statuses)
        self.assertEqual(all([status == "OK" for status in statuses.values()]), True)


if __name__ == '__main__':
    unittest.main()
