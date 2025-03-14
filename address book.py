address__book = {}
def add__contact(name,phone,email):
   address__book[name]= {"phone": phone, "Email": email}
   print(f"contact {name} added.")
def view__contact():
      if not address__book:
         print("Address book is empty.")
      else:
        for name, details in address__book.items():
         print(f"{name}: {details}") 
def search__contact(name):
      if name in address__book:
            print(f"{name}:{address__book[name]}")
      else:
            print("contact not found.") 
while True:  
      print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
      choice = input("Enter choice: ")
      if choice == "1":   
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter the choice:") 
            add__contact(name,phone,email) 
      elif choice == "2":
           view__contact()
      elif choice == "3":
           name=("Enter name to search:")
           search__contact  (name)
      elif choice == "4":
           print("Exiting address book.")
           break
      else:
           print("Invalid choice,try again.")
           

      
      





