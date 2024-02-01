class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'Phone': phone, 'Email': email}
        print(f"Contact '{name}' added successfully.")

    def edit_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['Phone'] = phone
            if email:
                self.contacts[name]['Email'] = email
            print(f"Contact '{name}' edited successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        print("Contacts:")
        for name, details in self.contacts.items():
            print(f"{name}: Phone - {details['Phone']}, Email - {details['Email']}")

def main():
    contact_list = ContactList()

    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_list.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter contact name to edit: ")
            phone = input("Enter new phone number (press Enter to keep the same): ")
            email = input("Enter new email address (press Enter to keep the same): ")
            contact_list.edit_contact(name, phone, email)

        elif choice == '3':
            name = input("Enter contact name to delete: ")
            contact_list.delete_contact(name)

        elif choice == '4':
            contact_list.display_contacts()

        elif choice == '5':
            print("Exiting Contact List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
