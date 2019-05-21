"""
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""


def calculate_grate(score):
    if not (0.0<=score<=1.0):
        return 'Bad Score'
    elif score>=0.9:
        return 'A'
    elif score>=0.8:
        return 'B'
    elif score>=0.7:
        return 'C'
    elif score>=0.6:
        return 'D'
    elif score<0.6:
        return 'F'

score=input('Enter the score')
try:
    float_score=float(score)
    print(calculate_grate(float_score))
except:
    print('Bad Score')


