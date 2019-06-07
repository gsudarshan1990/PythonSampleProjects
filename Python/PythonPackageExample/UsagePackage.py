import SentenceModification

sentence='All goods come to those who wait'

words=SentenceModification.break_words(sentence)
print(words)

print(SentenceModification.sort_sentence(sentence))

SentenceModification.print_first_and_last(sentence)
SentenceModification.print_first_and_last_sorted(sentence)
