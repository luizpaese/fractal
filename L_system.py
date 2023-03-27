import turtle

#config screen
WIDTH, HEIGHT = 1280, 720
screen = turtle.Screen()
# screen.setup(WIDTH, HEIGHT)
screen.screensize(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.delay(0)

#config turtle
triangle = turtle.Turtle()
triangle.pensize(2)
triangle.speed(0)
triangle.setpos(-WIDTH//3, -HEIGHT//2)
triangle.color("green")


#l-system
generation = 9
axiom = 'F'
char_1, rule_1 = 'F', 'F-G+F+G-F'
char_2, rule_2 = 'G', 'GG'
# char_1, rule_1 = 'F', 'F-F+F' #Triangulos que não se sobressaem
# char_2, rule_2 = 'G', 'G-F'
# char_1, rule_1 = 'F', 'F-F+F+G'
# char_2, rule_2 = 'G', 'G-F'
step = 5
angle = 120

def apply_rules(axiom):
    return ''.join([rule_1 if char == char_1 else
                    rule_2 if char == char_2 else char for char in axiom])

def get_result(generation, axiom):
    for gen in range(generation):
        axiom = apply_rules(axiom)

    return axiom

axiom = get_result(generation, axiom)

for chr in axiom:
    if chr == char_1 or chr == char_2:
        triangle.forward(step)
    elif chr == '+':
        triangle.right(angle)
    elif chr == '-':
        triangle.left(angle)

turtle.Screen().exitonclick()