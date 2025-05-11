import turtle as t
import numpy as np


def feuille():
    t.right(90)
    t.circle(2)
    t.left(90)


def colorPicker(iteration):
    color1 = tuple(int(start_color1[i] + (start_color2[i] - start_color1[i]) * np.random.choice(distribution) ) for i in range(3))
    color2 = tuple(int(end_color1[i] + (end_color2[i] - end_color1[i]) * np.random.choice(distribution) ) for i in range(3))
    color  = tuple(int(color1[i] + (color2[i] - color1[i]) * (maxIteration-iteration)/maxIteration) for i in range(3))

    return tuple(int(color[i] + ((0,0,0)[i] - color[i]) * (nbArbre-numeroArbre-1)/(2*nbArbre)) for i in range(3))


def arbre(distance,angle,iteration):

    if iteration==0:
        feuille()
        return
    
    t.pensize(iteration*0.75)
    t.pencolor(colorPicker(iteration))
    
    t.right(angle)
    t.forward(distance)

    for i in range(len(branches)):
        if np.random.choice(distribution)<branches[i][2] :

            arbre(distance*branches[i][0],branches[i][1] +np.random.normal(0, dispertionBranche) ,iteration-1) 


    t.penup()
    t.forward(-distance)
    t.pendown()
    t.left(angle)


def generate_spaced_points(nombrePoints=10, min_distance=80, bounds=((-200,200), (0,-200)), max_attempts=1000):

    points = []
    for _ in range(nombrePoints):
        attempts = 0
        while attempts < max_attempts:
            x = np.random.uniform(bounds[0][0], bounds[0][1])
            y = np.random.uniform(bounds[1][0], bounds[1][1])
            if all(np.sqrt((x-p[0])**2 + (y-p[1])**2) > min_distance for p in points):
                points.append([x, y])
                break
            attempts += 1
    return np.array(points)


def main():
    t.colormode(255)

    #t.Turtle._screen.bgcolor((127,127,127))

    t.hideturtle()
    t.speed(0)
    t.delay(0)
    t.tracer(0)

    global numeroArbre

    for numeroArbre in range(nbArbre):

        t.penup()
        t.goto(coordonnees[numeroArbre])
        t.pendown()

        t.setheading(90 + np.random.normal(0, dispertionArbre))

        arbre(taille,0,maxIteration)

        t.update()
        print("arbre n°" + str(numeroArbre+1) + " sur " + str(nbArbre) + " terminé !")
    print("programme terminé !")
    t.exitonclick()


if __name__ == '__main__':

    nbArbre = 1

    coordonnees = sorted(generate_spaced_points(nbArbre), key=lambda point: point[1], reverse=True)

    maxIteration=8
    taille = 100

    branches = [
        (0.6,45,0.9),
        (0.6,-40,0.8),
        (0.7,-10,0.9),
        (0.7,20,0.5),
        (0.2,60,0.2),
        (0.2,-50,0.1)
    ]

    distribution = np.arange(0, 1, 0.01)

    dispertionBranche = 2
    dispertionArbre = 5

    start_color1 = (139, 69, 30)  # Marron
    start_color2 = (122, 107, 66) # Marron

    end_color1 = (124, 252, 34)    # Vert
    end_color2 = (88, 183, 86)     # Vert

    main()