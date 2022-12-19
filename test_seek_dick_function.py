import unittest
from seekDick import seek_dick

class TestSeekDick(unittest.TestCase):
    """此类用来测试 seekDick 模块。
    """

    def test_seek_dick_yyf_man(self):
        result = seek_dick("嘤嘤饭", "男性")
        self.assertEqual(result, False)

    def test_seek_dick_yyf_woman(self):
        result = seek_dick("嘤嘤饭", "女性")
        self.assertEqual(result, False)

    def test_seek_dick_yyf_other_sex(self):
        result = seek_dick("嘤嘤饭", "其他性别")
        self.assertEqual(result, False)

    def test_seek_dick_other_man(self):
        result = seek_dick("被测试者", "男性")
        self.assertEqual(result, True)

    def test_seek_dick_other_woman(self):
        result = seek_dick("被测试者", "女性")
        self.assertEqual(result, False)

    def test_seek_dick_other_sex(self):
        result = seek_dick("被测试者", "其他性别")
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
