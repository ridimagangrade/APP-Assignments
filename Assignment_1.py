class functions():
    def __init__(self):
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def borrowbook(self, title):
        if title in self.books:
            self.books.remove(title)
            print("Book borrowed successfully!")
        else:
            print("Book not found!")

    def returnbook(self, book):
        self.books.append(book)
        print("Book returned successfully!")

    def display(self):
        print("Available books:", self.books)


class users():
    def __init__(self):
        self.users = []

    def adduser(self, user):
        self.users.append(user)
        print("User added successfully!")

    def removeuser(self, user):
        if user in self.users:
            self.users.remove(user)
            print("User removed successfully!")
        else:
            print("User not found!")

    def display(self):
        print("Available users:", self.users)


library = functions()
member = users()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Add User")
    print("6. Remove User")
    print("7. Display Users")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.addbook(book)

    elif choice == 2:
        book = input("Enter book name to borrow: ")
        library.borrowbook(book)

    elif choice == 3:
        book = input("Enter book name to return: ")
        library.returnbook(book)

    elif choice == 4:
        library.display()

    elif choice == 5:
        user = input("Enter user name: ")
        member.adduser(user)

    elif choice == 6:
        user = input("Enter user name to remove: ")
        member.removeuser(user)

    elif choice == 7:
        member.display()

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")