def break_words(sentence):
    words=sentence.split()
    return words

def sort_words(words):
    return sorted(words)

def sort_sentence(sentence):
    words=sentence.split()
    return sort_words(words)

def print_first_words(words):
    return words.pop(0)

def print_last_words(words):
    return words.pop(-1)

def print_first_and_last(sentence):
    words=break_words(sentence)
    print(print_first_words(words))
    print(print_last_words(words))

def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print(print_first_words(words))
    print(print_last_words(words))
