from random import shuffle

# function which takes a word as an argument and returns a shuffled version
def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

# function used to grab all the words and convert to json
def get_objects(words):
    new_list = []
    for i in words:
        empty_set = {}
        empty_set['text'] = i[0]
        empty_set['hint'] = i[1]
        empty_set['mix'] = jumble(i[0])
        new_list.append(empty_set)
    return new_list