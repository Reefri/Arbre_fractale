import turtle as t

def feuille():
    t.circle(2)

def arbre(distance,angle,branches,n):

    if n==0:
        feuille()
        return
    
    t.right(angle)
    t.forward(distance)

    for i in range(len(branches)):
        arbre(distance*branches[i][0],branches[i][1],branches,n-1)

    t.forward(-distance)
    t.left(angle)


def main(branches):
    t.setheading(90)
    t.hideturtle()
    t.speed(0)
    t.tracer(0)

    arbre(100,0,branches,7)

    t.update()
    t.exitonclick()


if __name__ == '__main__':

    branches = [
        (0.6,45),
        (0.6,-40),
        (0.7,-10)
    ]

    main(branches)