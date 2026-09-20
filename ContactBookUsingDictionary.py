contacts = {}


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print("Contact added.")


def search_contact():
    name = input("Enter Name: ")
    if name in contacts:
        print("Name:", name)
        print("Mobile No:", contacts[name])
    else:
        print("Contact is not present! Add contact first.")


def update_contact():
    name = input("Enter Name: ")
    if name in contacts:
        contacts[name] = input("Enter New Phone Number: ")
        print("Contact updated.")
    else:
        print("Contact is not present!")


def delete_contact():
    name = input("Enter Name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact is not present!")


while True:
    print("====== MENU ======")
    print("1. ADD CONTACT")
    print("2. SEARCH CONTACT")
    print("3. UPDATE CONTACT")
    print("4. DELETE CONTACT")
    print("5. EXIT")
    choice = input("Enter your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
                  
    

    