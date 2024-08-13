# Import pandas
import pandas as pd

# Create a sample dataframe and csv file for the library management system
# NOTE: After exiting the system, please comment the code below (line 11 - 19) to ensure any changes made to the
#       existing dataframe is stored permanently into the csv file;

library = {
    "Book_ID": ["B059", "B057"],
    "Book_Title": ["Psychology", "Life"],
    "Author": ["George F.", "William T."],
    "Borrower_Name": ["Ryan", "Alex"],
    "Book_Return_Date": ["14/10/2023", "26/10/2023"]
}
lib_book_df = pd.DataFrame(library)
lib_book_df.to_csv('Library_BookList.csv', index=False)

# Define functions
def addBook():
    global lib_book_df
    lib_book_df = pd.read_csv("Library_BookList.csv")
    print(lib_book_df)
    print()

    print("BOOK 1")
    print()
    Book_ID = str(input("Please insert the book ID in the B___ format (e.g., B123): "))
    Book_Title = input("Please insert the book title: ")
    Author = input("Please insert the author's name: ")
    Borrower_Name = input("Please insert the borrower's name: ")
    Book_Return_Date = input("Please insert the date when the book should be returned by the borrower (dd/mm/yyyy): ")
    print()

    new_record = {"Book_ID": Book_ID, "Book_Title": Book_Title, "Author": Author, "Borrower_Name": Borrower_Name,
                  "Book_Return_Date": Book_Return_Date}

    if Book_ID[0] == "B" and Book_ID not in lib_book_df["Book_ID"].values:
        lib_book_df = lib_book_df._append(new_record, ignore_index=True)
        lib_book_df.to_csv("Library_BookList.csv", index=False)
        print(lib_book_df)
        print()
        print("You've successfully added a new book record to the existing library!")
    else:
        print('The entered Book ID has already existed in the system or its format is wrong, please try again :)\n')
        addBook()

    print()

def deleteBook():
    global lib_book_df
    lib_book_df = pd.read_csv("Library_BookList.csv")
    Book_ID = input("Please enter the book ID of the book that you'd like to delete: ")
    print()

    if Book_ID[0] == "B" and Book_ID in lib_book_df["Book_ID"].values:
        x = lib_book_df.eq(str(Book_ID)).any(axis = 1)
        lib_book_df = lib_book_df.drop(lib_book_df[x].index)
        lib_book_df.to_csv("Library_BookList.csv", index=False)
        print("Book_ID removed")
        print()
        print(lib_book_df)
        print()
    else:
        print("Book_ID not found, please try again")
        print()
        deleteBook()

def searchBook():
    global lib_book_df
    lib_book_df = pd.read_csv("Library_BookList.csv")
    Book_ID = input("Please enter the book ID of the book that you'd like to search: ")
    print()

    if Book_ID[0] == "B" and Book_ID in lib_book_df["Book_ID"].values:
        y = lib_book_df["Book_ID"] == Book_ID
        print(lib_book_df[y])
        print()
        print('The book is found successfully!')
    else:
        print("Book doesn't exist, please try again")
        print()
        searchBook()

def updateBook():
    global lib_book_df
    lib_book_df = pd.read_csv("Library_BookList.csv")
    Book_ID = input("Please enter the book ID of the book that you'd like to update: ")
    print()

    if Book_ID[0] == "B" and Book_ID in lib_book_df["Book_ID"].values:
        y = lib_book_df["Book_ID"] == Book_ID
        print(lib_book_df[y])
        print()
        value_before = str(input("Please input the value that you'd like to change based on the filtered book list above: "))
        value_after = str(input("Please input the new value: "))
        print()
        lib_book_df[lib_book_df == str(value_before)] = str(value_after)
        print(lib_book_df)
        lib_book_df.to_csv("Library_BookList.csv", index=False)
        print()
        print("You have successfully updated the book record!")
    else:
        print("Book doesn't exist, please try again")
        print()
        updateBook()

def viewAllBook():
    lib_book_df = pd.read_csv("Library_BookList.csv")
    print(lib_book_df)

def main_menu():
    print("*****************")
    print("Main Menu")
    menu = ["1. Add Book", "2. Update Book", "3. List All Book", "4. Search Book", "5. Remove Book", "6. Exit"]
    for options in menu:
        print(options)
    print("*****************")
    global choice
    choice = int(input("Enter your choice: "))
    print()

# Apply all functions into this library management system
main_menu()

while True:
    if choice == 1:
        print("YOU ARE NOW IN THE ADD BOOK SECTION")
        print()
        addBook()
        back_to_menu = input("Back to main menu - Yes OR No? ")
        if back_to_menu == "Yes":
            print()
            main_menu()
            print()
        else:
            print()
            print("Thank you for your hard work, and have a great day ahead!")
            break
    elif choice == 2:
        print("YOU ARE NOW IN THE UPDATE BOOK SECTION")
        print()
        updateBook()
        print()
        back_to_menu = input("Back to main menu - Yes OR No? ")
        if back_to_menu == "Yes":
            print()
            main_menu()
            print()
        else:
            print()
            print("Thank you for your hard work, and have a great day ahead!")
            break
    elif choice == 3:
        print("YOU ARE NOW IN THE LIST ALL BOOK SECTION")
        print()
        viewAllBook()
        print()
        back_to_menu = input("Back to main menu - Yes OR No? ")
        if back_to_menu == "Yes":
            print()
            main_menu()
            print()
        else:
            print()
            print("Thank you for your hard work, and have a great day ahead!")
            break
    elif choice == 4:
        print("YOU ARE NOW IN THE SEARCH BOOK SECTION")
        print()
        searchBook()
        print()
        back_to_menu = input("Back to main menu - Yes OR No? ")
        if back_to_menu == "Yes":
            print()
            main_menu()
            print()
        else:
            print()
            print("Thank you for your hard work, and have a great day ahead!")
            break
    elif choice == 5:
        print("YOU ARE NOW IN THE REMOVE BOOK SECTION")
        print()
        viewAllBook()
        print()
        deleteBook()
        back_to_menu = input("Back to main menu - Yes OR No? ")
        if back_to_menu == "Yes":
            print()
            main_menu()
            print()
        else:
            print()
            print("Thank you for your hard work, and have a great day ahead!")
            break
    elif choice == 6:
        print("Thank you for using our system, GOOD BYE :)")
        break
    else:
        print("Sorry, invalid input, please try again")
        print()
        main_menu()
