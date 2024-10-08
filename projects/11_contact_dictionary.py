title = "Contact Book Menu"
# Initialize an empty contact book
contact_book = {}

def add_contact(name, phone):
    #Add a new contact to the contact book.
    contact_book[name] = {
        'phone': phone
    } #adds a new contact
    print(f"Your contact {name} is added.")

def view_contacts():
    #Displays all contacts in the contact book.
    if not contact_book:
        print("Contact book is empty.")
        return
    for name, info in contact_book.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def delete_contact(name):
    #Deletes a contact by name.
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

