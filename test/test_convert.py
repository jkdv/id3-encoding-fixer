import unittest

import chardet

import convert


class ConvertCase(unittest.TestCase):
    def test_fix_save(self):
        convert.fix_save_batch('melon')
        # self.fail()

    def test_encode(self):
        raw = 'Á¤ÀºÁöÁ¤ÀºÁöÁ¤ÀºÁöÁ¤ÀºÁöÁ¤ÀºÁöÁ¤ÀºÁö'.encode(encoding='cp1252')
        encoding = chardet.detect(raw)

        text = raw.decode(encoding='EUC-KR')
        self.assertIsNotNone(text)


if __name__ == '__main__':
    unittest.main()
