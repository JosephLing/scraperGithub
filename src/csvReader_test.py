import unittest
from unittest import mock
import csvReader


class CheckName(unittest.TestCase):

    def does_not_exist(self):
        csvReader.exists = mock.Mock()
        csvReader.exists.return_value = False
        self.assertEqual("cat", csvReader.check_name("cat"))

    def does_exist_above_count(self):
        csvReader.exists = mock.Mock()
        csvReader.exists.return_value = True
        self.assertEqual("", csvReader.check_name("cat"))

    def does_exist_within_count(self):
        def side_effect(name):
            return "9" not in name

        csvReader.exists = mock.Mock()
        csvReader.exists.side_effect = side_effect
        self.assertEqual("cat9", csvReader.check_name("cat"))


if __name__ == '__main__':
    unittest.main()
