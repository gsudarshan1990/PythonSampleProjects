"""

Below, we have provided a nested list called big_list. Use nested iteration to create a dictionary, word_counts, that contains all the words in big_list as keys, and the number of times they occur as values.

big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

"""


big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]
word_counts=dict()

for element_in_outer_list in big_list:
    if type(element_in_outer_list) is list:
        for element_in_inner_list in element_in_outer_list:
            if type(element_in_inner_list) is list:
                for element_in_second_inner_list in element_in_inner_list:
                    word_counts[element_in_second_inner_list]=word_counts.get(element_in_second_inner_list,0)+1

print(word_counts)
