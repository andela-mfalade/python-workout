import turtle

screen = turtle.Screen()
screen.bgcolor('#e74c3c')


class CustomizedTurtle(turtle.Turtle):
    def __init__(self):
        super(CustomizedTurtle, self).__init__()
        self.shape('turtle')
        self.color('#2ecc71')
        self.speed(5)


def draw_hat():
    march = CustomizedTurtle()
    march.speed(9)
    march.fill(flag=True)
    for i in range(180):
        march.forward(100)
        march.right(30)
        march.forward(20)
        march.left(60)
        march.forward(50)
        march.right(30)
        march.penup()
        march.setposition(0, 0)
        march.pendown()
        march.right(2)
    screen.exitonclick()
    turtle.done()


def draw_flower():
    rose = CustomizedTurtle()
    for i in range(6):
        color = '#2ecc71' if i % 2 == 0 else '#9b59b6'
        rose.color(color)
        rose.forward(100)
        rose.left(90)
        rose.circle(120, 180)


def draw_circle_with_squares():
    brad = CustomizedTurtle()
    for i in range(36):
        brad.forward(100)
        brad.left(90)
        brad.forward(100)
        brad.left(90)
        brad.forward(100)
        brad.left(90)
        brad.forward(100)
        brad.left(90)
        brad.right(10)
    screen.exitonclick()


def draw_complex_triangle():
    meow = CustomizedTurtle()

    def draw_triangle(the_turtle, length, ori, recursion):
        recursion = recursion + 1
        meow = the_turtle

        for i in range(0, 3):
            if(recursion < 4):
                meow.forward(length / 2)
                meow.left(120)
                draw_triangle(meow, length / 2, 0, recursion)
                meow.right(120)
                meow.forward(length / 2)
            else:
                meow.forward(length)
            if (ori == 1):
                meow.left(120)
            else:
                meow.right(120)
    screen.exitonclick()
    draw_triangle(meow, 200, 1, 0)


def main():
    # draw_circle_with_squares()
    draw_complex_triangle()


if __name__ == '__main__':
    main()
