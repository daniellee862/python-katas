from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case, camel_to_english_regex, camel_to_english_isupper)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_two_words_in_upper_if_true():
    expected = 'This Sentence'
    result = sentence_to_camel_case('this sentence', True)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_two_words_in_lower_if_false():
    expected = 'this Sentence'
    result = sentence_to_camel_case('this sentence', False)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_all_words_from_mixed_sentence_in_upper_if_true():
    expected = 'This Sentence Is Now In Upper Camel Case'
    result = sentence_to_camel_case(
        'this sentence Is Now in upper Camel case', True)
    print(f'Result is: {result}')
    assert result == expected


def test_returns_english_from_camel_case_using_regex():
    expected = 'This bigger strange sentence.'
    result = camel_to_english_regex(
        "thisBiggerStrangeSentence")
    print(f'Result is: {result}')
    assert result == expected


def test_returns_english_from_camel_case_using_isupper():
    expected = 'This bigger strange sentence.'
    result = camel_to_english_isupper(
        "thisBiggerStrangeSentence")
    print(f'Result is: {result}')
    assert result == expected
