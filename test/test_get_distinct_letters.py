from src.get_distinct_letters.get_distinct_letters import get_distinct_letters


def test_get_distinct_letters_returns_string():
    result = get_distinct_letters('hello', 'world')  # => 'dehrw'
    print(f'Result is: {result}')
    assert isinstance(result, str)


def test_returns_distinct_letters():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    print(f'Result is: {result}')
    assert result == expected


def test_returns_distinct_letters_when_passed_cap():
    expected = 'dehrw'
    result = get_distinct_letters('heLLo', 'WorRRRrld')
    print(f'Result is: {result}')
    assert result == expected
