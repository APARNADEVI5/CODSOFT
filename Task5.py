contacts = {} 
def addc():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!\n")

def viewc():
    if not contacts:
        print("No contacts found!\n")
        return
    print(" Contact List:")
    for name, phone in contacts.items():
        print(f" {name}: {phone}")
    print()

def seac():
    name = input(" Enter Name to Search: ")
    if name in contacts:
        print(f" {name}: {contacts[name]}\n")
    else:
        print(" Contact not found!\n")
def delc():
    name = input("🗑️ Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(" Contact not found!\n")
while True:
    print(" Simple Contact Book")
    print("1️ Add Contact")
    print("2️ View Contacts")
    print("3️ Search Contact")
    print("4️ Delete Contact")
    print("5️ Exit")
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        addc()
    elif choice == "2":
        viewc()
    elif choice == "3":
        seac()
    elif choice == "4":
        delc()
    elif choice == "5":
        print("close")
        break
    else:
        print("Invalid choice")
