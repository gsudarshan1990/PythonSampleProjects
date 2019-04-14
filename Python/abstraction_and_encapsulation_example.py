class Library:
    def __init__(self, list_of_books):
        self.availablebooks=list_of_books

    def dispaly_books(self):
        for book in self.availablebooks:
            print(book)

    def lend_books(self, requestedBook):
        if requestedBook in self.availablebooks:
            self.availablebooks.remove(requestedBook)
            print('Your book has been dispatched')
        else:
            print('Sorry, your book is not available')

    def return_books(self,returnedBook):
        self.availablebooks.append(returnedBook)
        print('Your book has been added')

class Customer:
    def getBook(self):
        print('Enter the name of the book that you want to borrow')
        requestBook=input()
        return requestBook

    def returnBook(self):
        print('Enter the book that you want to return')
        returnBook=input()
        return returnBook

library=Library(['Think and Grow Rich', 'For One More Day', 'Positive Thinking'])
customer=Customer()
while True:
    print('Enter 1 for display the books')
    print('Enter 2 for borrow the book')
    print('Enter 3 for return book')
    print('Enter 4 to quit')
    user_choice=int(input())

    if user_choice == 1:
        library.dispaly_books()
    elif user_choice ==2:
        requestedBook=customer.getBook()
        library.lend_books(requestedBook)
    elif user_choice == 3:
        returnBook=customer.returnBook()
        library.return_books(returnBook)
    elif user_choice == 4:
        quit()
