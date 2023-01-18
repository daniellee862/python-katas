def get_frequencies(string):
    # I want to try do this in a nested list compresion where I return a count for char in string, but first; brute force
    char_freq = {}
    for char in string:
        if char != " ":
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    return char_freq

# get_frequencies('hello world')

# {
#   h: 1,
#   e: 1,
#   l: 3,
#   o: 2,
#   w: 1,
#   r: 1,
#   d: 1
# }


# new_dictionary = { key:value | for (key,value) in iterable | if condition }

# words = ['this','poker','quest']

# dict = { word:len(word) for word in words }

# {'this': 4, 'poker': 5, 'quest': 5}
