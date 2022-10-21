author_book = {'Louise Jensen' : ['All for you'], 'Karen M. McManus' : ['The Cousins', 'One of us is lying', 
'One of us is next'], 'Wulf Dorn' : ['Los Herederos'], 'Neil White' : ['The Death Collector']}

#in order to use the sorted() function for alphabetical order you need to make every single value a list

key = author_book.keys()
value = sorted(author_book.values())

for key in author_book:
    author_name = input('Please enter an author name: ')
    if author_name == key:
        print('Book title: ',sorted(author_book[key]))
    
print(type(author_book['Karen M. McManus']))

