import unittest

import convert


class ConvertCase(unittest.TestCase):
    def test_fix_save(self):
        'XIA (준수)'.encode(encoding='cp1252')
        self.fail()


if __name__ == '__main__':
    unittest.main()
