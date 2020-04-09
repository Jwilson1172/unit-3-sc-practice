import unittest
from package.blank_class import Person


class ScraperMethodTests(unittest.TestCase):
    person = Person('joe', 25, 'm', 125000.00)

    def test_age_to_incomeR(self):
        self.assertGreater(self.person.age_to_incomeR(), 90)

    def test_split_name(self):
        with self.assertRaises(ValueError):
            self.person.split_name()


if __name__ == '__main__':
    unittest.main()
