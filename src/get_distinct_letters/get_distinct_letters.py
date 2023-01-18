def get_distinct_letters(param1, param2):
    # after googling for a refactor came across the ^ operator:
    all_distinct_letters = "".join(
        sorted(set(param1.lower()) ^ set(param2.lower())))
    return all_distinct_letters

    # can even use it in a list comprehension:
    # all_distinct_letters = "".join(sorted(c for c in param1+param2 if (c in param1) ^ (c in param2)))
    distinct_letters_1 = [char for char in param1 if char not in param2]
    distinct_letters_2 = [char for char in param2 if char not in param1]
    all_distinct_letters = distinct_letters_1 + distinct_letters_2
    distinct_letter_string = "".join(sorted(all_distinct_letters))
