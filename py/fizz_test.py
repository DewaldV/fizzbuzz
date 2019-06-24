def fizzbuzz(i):
    if i == 3:
        return 'fizz'
    if i == 5:
        return 'buzz'
    return str(i)

import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("fizzbuzz(1)", '1'),
    ("fizzbuzz(2)", '2'),
    ("fizzbuzz(3)", 'fizz'),
    ("fizzbuzz(5)", 'buzz')
])
def test_should_return_number(test_input, expected):
    assert eval(test_input) == expected

