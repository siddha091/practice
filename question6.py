'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words

'''


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]



words = ['sid', 'i am here', 'test']
print map_to_lengths_for(words)
print map_to_lengths_map(words)
print map_to_lengths_lists(words)