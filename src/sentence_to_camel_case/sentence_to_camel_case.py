import re


def sentence_to_camel_case(arg1, arg2):
    # The . split() method returns a new list of substrings, and the original string is not modified in any way.
    sentence_list = arg1.split()
    if arg2:
        to_upper = [word.capitalize() for word in sentence_list]
        print(" ".join(to_upper))
        return " ".join(to_upper)
    else:
        # enumerate func takes iterable object and returns enumerate obj; each iter yields a tuple of the form (count, value), this can be used for iteration, count starts at 0 as default. LOVE THIS!
        # can this be donw with a lambda?
        to_lower = [word if index < 1 else word.capitalize()
                    for index, word in enumerate(sentence_list)]
        return " ".join(to_lower)


def camel_to_english_isupper(camel_string):
    sentence = ""
    for i in range(len(camel_string)):
        # If current char is uppercase, add space
        if camel_string[i].isupper():
            sentence += " "
        # Add char
        sentence += camel_string[i]
    # Make first letter uppercase
    sentence = sentence.capitalize()
    # Add full stop
    sentence += "."
    return sentence


def camel_to_english_regex(camel_string):
    # Use regex to split camel at every uppercase letter
    split_string = re.findall(r'[a-zA-Z][a-z]*', camel_string)
    print(split_string)
    # Join plit string with spaces and make first letter uppercase
    sentence = ' '.join(split_string).capitalize()
    # Add full stop
    sentence += '.'
    print(sentence)
    return sentence
