class fruit:
    print("My favourite fruits are mango ,Ice apple,Bananna,Watermelon")
a=fruit()
# Write a program to create a class Parrot and perform the following tasks - 
# Create a class variable species, Create a constructor 
# that has instance variables - name and age, Create instances of class Parrot,
# passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.
class parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)       
oge=parrot("Mikku",10)
oge.display()
