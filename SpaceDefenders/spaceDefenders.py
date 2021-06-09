import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Space Defense")
window.bgcolor("black")
window.bgpic("background.gif")
#Detener actualizaciones de pantalla
window.tracer(0)

#Definir formas
playerVertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
window.register_shape("player", playerVertices)


asteroidVertices = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10),
                        (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("asteroid", asteroidVertices)

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #velocidad de animación
        self.speed(0)
        self.penup()
        
def getHeadingTo(player, asteroid):
    x1 = player.xcor()
    y1 = player.ycor()
    x2 = asteroid.xcor()
    y2 = asteroid.ycor()
    heading = math.atan2(y1 - y2, x1 - x2)
    heading = heading * 180.0 / 3.14159
    return heading

#Definir jugador   
player = Sprite()
player.color("#102C54")
player.shape("player")
player.score = 0

#Creacion de missiles
missiles = []
for _ in range(3):
    missile = Sprite()
    missile.color("red")
    missile.shape("arrow")
    missile.speed = 1
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)

#Creacion de asteroides
asteroids = []
for i in range(5):   
    asteroid = Sprite()
    asteroid.color("#9B9B9B")
    asteroid.shape("asteroid")
    asteroid.speed = random.randint(2, 3)/50
    asteroid.goto(0, 0)
    heading = random.randint(0, 260)
    distance = random.randint(300, 400)
    asteroid.setheading(heading)
    asteroid.fd(distance)
    asteroid.setheading(getHeadingTo(player, asteroid))
    asteroids.append(asteroid)

#Rotar jugador a la derecha e izquierda 
def rotate_left():
    player.lt(20)
def rotate_right():
    player.rt(20)

#Disparar missiles    
def fireMissile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break

#Enlazar con teclado
window.listen()
window.onkey(rotate_left, "Left")
window.onkey(rotate_right, "Right")
window.onkey(fireMissile, "space")

#Loop of game
gameOver = False
while True:
    window.update()
    player.goto(0, 0)
    
    #Mover missil
    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        #Comprobar borde
        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "ready"

    #Iterar array de asteroides
    for asteroid in asteroids:    
        #Mover asteroides
        asteroid.fd(asteroid.speed)
        
        #Comprobar colision entre asteroide y missil
        for missile in missiles:
            if asteroid.distance(missile) < 20:
                #Restablecer asteroide
                heading = random.randint(0, 260)
                distance = random.randint(600, 800)
                asteroid.setheading(heading)
                asteroid.fd(distance)
                asteroid.setheading(getHeadingTo(player, asteroid))
                asteroid.speed += 0.01
                #Restablecer Missile
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"

        #Colision asteroide y jugador
        if asteroid.distance(player) < 20:
            #Restablecer asteroide
            heading = random.randint(0, 260)
            distance = random.randint(600, 800)
            asteroid.setheading(heading)
            asteroid.fd(distance)
            asteroid.setheading(getHeadingTo(player, asteroid))
            asteroid.speed += 0.005
            gameOver = True
         
    if gameOver == True:
        player.hideturtle()
        missile.hideturtle()
        for i in asteroids:
            i.hideturtle()
        break

window.mainloop()