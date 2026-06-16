class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

obj = Child()

obj.show_grandparent()
obj.show_parent()
obj.show_child()

'''Grandparent → Base class
Parent inherits from Grandparent
Child inherits from Parent'''