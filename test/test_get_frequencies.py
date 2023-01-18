from src.get_frequencies.get_frequencies import get_frequencies


def test_get_frequencies_returns_dict():
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert isinstance(result, dict)


def test_get_frequencies_returns_char_and_freq():
    expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert result == expected
