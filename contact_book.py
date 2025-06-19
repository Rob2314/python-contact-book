import json

def load_contacts_from_file(): 
    try: 
        with open('contacts.json', 'r') as file: 
            contacts = json.load(file) 
    except (FileNotFoundError, json.JSONDecodeError): 
        contacts = []
    return contacts 

def save_contacts_to_file(contacts):
    with open('contacts.json', 'w') as file: 
        json.dump(contacts, file, indent=4) 

def view_all_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1): #
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contacts(contacts, search_name): #search function for use in other functions.
    found_contacts = []

    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            found_contacts.append(contact)

    return found_contacts


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact) 
    save_contacts_to_file(contacts) 
    print(f"Contact {name} added successfully.")

def show_searched_contacts(contacts): #search function shown to user.
    search_name = input("Enter name you wish to search: ")
    found_contacts = search_contacts(contacts,search_name)
    if found_contacts:
        view_all_contacts(found_contacts)
    else:
        print("No contacts found.")

    
def delete_contact(contacts):
    search_name = input('Enter name you wish to delete: ')
    found_contacts = search_contacts(contacts, search_name)

    if found_contacts:
        view_all_contacts(found_contacts)
    else:
        print("Not found.")
        return

    try:
        num = int(input("Which contact do you wish to delete? Enter number."))
        if num > len(found_contacts) or num < 1:
            print("Error. Please choose one of the numbers assigned to a contact.")
        else:
            deleted_contact = found_contacts[num-1]
            contacts.remove(deleted_contact)
            save_contacts_to_file(contacts)
            print("Deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def return_to_menu():
    input('\n Press Enter to return to menu.')
    

# show menu
def menu(): 
    print("\nContact Book Menu:")
    print("1. View All Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = load_contacts_from_file()
  
    while True:
        menu()
        menu_choice = input("Enter a number (1-5): ")
        if menu_choice == "1":
            view_all_contacts(contacts)
            return_to_menu()
        
        elif menu_choice == "2":
            add_contact(contacts)
            return_to_menu()

        elif menu_choice == "3":
            show_searched_contacts(contacts)
            return_to_menu()

        elif menu_choice == "4":
            delete_contact(contacts)
            return_to_menu()

        elif menu_choice == "5":
            print("Exiting the program")
            break
        else:
            print("Invalid. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
