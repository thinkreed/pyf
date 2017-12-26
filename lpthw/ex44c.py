class Parent(object):

    def altered(self):
        print("parent altered")


class Child(Parent):

    def altered(self):
        print("before")
        super(Child, self).altered()
        print("after")


dad = Parent()
son = Child()

dad.altered()
son.altered()