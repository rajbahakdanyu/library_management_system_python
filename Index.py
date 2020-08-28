import Return
import Borrow

# Reading from booklist.txt and displaying booklist
def read_booklist():
    with open("booklist.txt","r") as reading:
        file_content = reading.readlines()
        for each_list in file_content:
            book_list.append(each_list.replace("\n",",").split(","))
        print("Book id\t\tBook name\t\tAuthor\t\t\tQuantity\tPrice($)")
        for each_list in book_list:
            print(f"{each_list[0]}\t\t{each_list[1]}\t\t{each_list[2]}\t\t{each_list[3]}\t\t{each_list[4]}")
    print()

# Main loop for user input
user = "a"
while user != "e":
    book_list = []
    read_booklist()
    user = input("Press r to return book, b to borrow book or e to exit program: ").lower()
    if user == "r":
        Return.return_book(book_list)
    elif user == "b":
        Borrow.borrow_book(book_list)
    elif user == "e":
        break
    else:
        print("Please enter a valid keyword")
    print()
