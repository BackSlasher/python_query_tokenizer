import unittest
from query_tokenizer.string_tokenizer import tokenize, CompoundToken, StringToken


class TestStringTokenizer(unittest.TestCase):
    def _compare(self, inp, expected):
        actual = tokenize(inp)
        self.assertEqual(actual, expected)

    def test_basic(self):
        inp = 'Hello, my name is "jeff the great". Welcome to (my (birthday party))'
        expected = CompoundToken(
            subTokens=(
                StringToken(s="Hello,"),
                StringToken(s="my"),
                StringToken(s="name"),
                StringToken(s="is"),
                StringToken(s='"jeff the great".'),
                StringToken(s="Welcome"),
                StringToken(s="to"),
                CompoundToken(
                    subTokens=(
                        StringToken(s="my"),
                        CompoundToken(
                            subTokens=(
                                StringToken(s="birthday"),
                                StringToken(s="party"),
                            )
                        ),
                    )
                ),
            )
        )
        self._compare(inp, expected)


if __name__ == "__main__":
    unittest.main()
