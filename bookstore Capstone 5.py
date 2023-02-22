import sqlite3
db = sqlite3.connect('data/bookstore_db') #creates database in subfolder
cursor = db.cursor() #get cursor object to be able to interact with the database

#Pseudocode outline and minimal code for this task "bookstore"
#SQLite is used to interact with the Python code

#Program capabilities:
#1. Add new books to a database of books
#2. Update books in the database
#3. Delete books from the database
#4. Search the database for a specific book

#Tasks:
#1. Create a database with the structure (id, Title, Author, Qty) using SQL

cursor.execute('''
    CREATE TABLE bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')
db.commit() #required after .execute

#2. Populate database with the given values using SQL

cursor = db.cursor() #create new cursor
id = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                  VALUES (?,?,?,?)''', (id, title1, author1, qty1)
)
print("First book added")
db.commit()

#etc. some logic for the other books

id += 1
title2 = 'Harry Potter and the Philosopher\'s Stone'
author2 = 'J.K Rowling'
qty2 = 40

cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                  VALUES (?,?,?,?)''', (id, title2, author2, qty2)
)
print("Second book added")
db.commit()

id += 1
title3 = 'The Lion, The Witch and Wardrobe'
author3 = 'C.S. Lewis'
qty3 = 25

cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                  VALUES (?,?,?,?)''', (id, title3, author3, qty3)
)
print("Third book added")
db.commit()

id += 1
title4 = 'The Lord of the Rings'
author4 = 'J.R.R. Tolkien'
qty4 = 37

cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                  VALUES (?,?,?,?)''', (id, title4, author4, qty4)
)
print("Fourth book added")
db.commit()

id += 1
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                  VALUES (?,?,?,?)''', (id, title5, author5, qty5)
)
print("Fifth book added")
db.commit()


#3. Create menu with the options in Python
print(''' Menu:

    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit''')

user_choice = input("Select an option from the menu by typing the full command e.g 'Enter book': ")

#For a user to enter a book ask for input
if user_choice == "Enter book":

    title_to_add = str(input("Enter the title"))
    author_to_add = str(input("Enter the author's name"))
    qty_to_add = int(input("How many of this book are there to add?"))
    #get last row ID and add 1 to determine the new ID
    cursor = db.cursor()
    id_last = int(cursor.lastrowid)
    id_to_add = id_last + 1

#Then add that book to the database with that information
    cursor.execute('''INSERT INTO bookstore(id, title, author, qty)
                    VALUES (?,?,?,?)''', (id_to_add, title_to_add, author_to_add, qty_to_add)
    )
    print(f"New book with id {id_to_add} added")
    db.commit()

#For a user to update a book
if user_choice == "Update book":
    id_to_update = int(input("What is the id of the book you wish to update?: "))
    cursor.execute('''SELECT title, author, qty from bookstore WHERE id=? ''', (id_to_update,))
    book = cursor.fetchone()
    print(f'''The current data stored on the book with id {id_to_update} is ''' 
    + book)
    print("Enter the new quantity below. If the value is the same, re-enter it:")
    qty_to_update = input("What is the new quantity?: ")
    cursor.execute('''UPDATE bookstore SET qty = ? WHERE id = ? ''', (qty_to_update, id_to_update))
    print("Book record updated!")
    db.commit()

#For a user to delete a book
if user_choice == "Delete book":
    id_to_delete = int("Enter the id of the book entry to delete: ")
    cursor.execute('''DELETE from bookstore WHERE id =?''', (id_to_delete,))
    print(f"Book with id {id_to_delete} deleted")
    db.commit()
 

#For a user to search books
if user_choice == "Search books":
    book_id = int(input("Enter the id of the book you wish to retrieve: "))
    cursor.execute('''SELECT title, author, qty from bookstore WHERE id=? ''', (book_id,))
    book = cursor.fetchone()
    print(f'''Data retrieved about book with id {book_id}''' 
    + book)
    db.commit()

#Exit program if chosen
elif user_choice == "Exit":
    print("Connection to database closed.")
    db.commit()
    db.close()
    quit()