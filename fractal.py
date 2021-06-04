import turtle

STEP = 10
ANGLE = 120
from1 = 'A'
to1 = 'A-B+A+B-A'
from2 = 'B'
to2 = 'BB'
FIRST_RULE = 'A-B-B'


def init_turtle(speed=0, width=1900, height=900):
    turtle.speed(speed)
    t = turtle.Turtle()

    screen = turtle.Screen()
    screen.setup(width, height)
    screen.delay(0)
    return t


def change(data):
    changed = ''
    for el in data:
        if el == from1:
            changed += to1
        elif el == from2:
            changed += to2
        else:
            changed += el
    return changed


def create_commands(n, rule):
    res = []
    temp_rule = rule
    for gen in range(n):
        temp_rule = change(temp_rule)
        res.append(temp_rule)
    return res


def execute_commands(commands, MyTurtle, step, angle):
    for command in commands:
        for symb in command:
            if symb == 'A' or symb == 'B':
                MyTurtle.forward(step)
            elif symb == '-':
                MyTurtle.left(angle)
            else:
                MyTurtle.right(angle)


def draw_fractal(n=6):
    MyTurtle = init_turtle()
    res = create_commands(n, FIRST_RULE)
    execute_commands(res, MyTurtle, STEP, ANGLE)
    turtle.done()


def main():
    n = int(input("Degree: "))
    draw_fractal(n)


if __name__ == "__main__":
    main()

