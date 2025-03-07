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





         
      

