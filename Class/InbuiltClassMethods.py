#Print and Length does not work as expected

class Sample():
    pass

sample=Sample()
#print(sample)
#len(sample)



class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return "Book name is {} and author is {}".format(self.title,self.author)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


book=Book('Python','charles',200)
print(book)
print(len(book))
del book

