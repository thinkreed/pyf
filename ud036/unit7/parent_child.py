class Parent:
    def __init__(self, last_name, eye_color):
        print('parent init')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('last name is ' + self.last_name)
        print('eye color is ' + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print('child init')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print('last name is ' + self.last_name)
        print('eye color is ' + self.eye_color)
        print('toys ' + str(self.number_of_toys))


reed_thinked = Child('thinkred', 'black', 9)
reed_thinked.show_info()
