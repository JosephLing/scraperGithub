import unittest
from .data_parser import isCommentInString


class IsCommentInStringTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(isCommentInString("#hello"), "#hello")

    def test_end_of_string(self):
        self.assertEqual(isCommentInString("asdfasdfasdf#hello"), "#hello")

    def test_quotes(self):
        self.assertEqual(isCommentInString("'a'#hello"), "#hello")

    def test_single_quotes(self):
        self.assertEqual(isCommentInString('"asdf"#hello'), "#hello")

    def test_mixed_quotes(self):
        self.assertEqual(isCommentInString("'asdf#assd'#cat"), "#cat")

    def test_mixed_quotes2(self):
        self.assertEqual(isCommentInString('"asa#cats"asdfdfsdf#dog'), "#dog")


    def test_empty(self):
        self.assertEqual(isCommentInString(''), "")

    def test_newline(self):
        self.assertEqual(isCommentInString('\n'), "")

    def test_no_comment(self):
        self.assertEqual(isCommentInString('hello world'), "")


if __name__ == '__main__':
    unittest.main()
