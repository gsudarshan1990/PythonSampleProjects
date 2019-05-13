"""
Write a Python function to check whether a string is pangram or not.
For example : "The quick brown fox jumps over the lazy dog"
"""

def check_panagram(string1):
   list_words=string1.split()
   list_character=[]
   final_list=[]
   for word in list_words:
       for character in word:
           list_character.append(character.lower())
   print(list_character)
   set_character=set(list_character)
   list_unique_character=list(set_character)
   print(list_unique_character)
   print(len(list_unique_character))
   for letter in list_unique_character:
       if ord('a')<=ord(letter)<=ord('z'):
            index=ord(letter)-ord('a')
            print(index)
            final_list.insert(index,letter)
   print(final_list)
string1="The quick brown fox jumps over the lazy dog"
check_panagram(string1)
