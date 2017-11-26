import turtle


def create_window():
    window = turtle.Screen()
    window.bgcolor('red')
    return window


def draw_circle(window):
    angie = turtle.Turtle()
    angie.color('yellow')
    angie.shape('arrow')
    angie.speed(2)
    angie.circle(100)


def draw_triangle(window):
    baby = turtle.Turtle()
    baby.color('blue')
    baby.shape('turtle')
    baby.speed(2)
    for i in range(0, 3):
        baby.forward(100)
        baby.right(120)


def draw_rectangle_circle(window):

    john = turtle.Turtle()
    john.shape('turtle')
    john.color('green')
    john.speed(2)

    for i in range(0, 36):
        draw_square(john)
        john.right(10)


def draw_square(turtle):
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)


def test():
    window = create_window()
    draw_rectangle_circle(window)
    window.exitonclick()


test()