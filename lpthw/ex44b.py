class Parent(object):

    def override(self):
        print("parent override")


class Child(Parent):

    def override(self):
        print("child override")


dad = Parent()
son = Child()

dad.override()
son.override()