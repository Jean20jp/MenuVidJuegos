import turtle
import time
import random

head = turtle.Turtle()
text = turtle.Turtle()
food = turtle.Turtle()
segment = []
posponer = 0.1

class Ventana:
    def __init__(self, windown):
        self.windown = turtle.Screen()
        self.windown.title("Juego de Snake")
        self.windown.bgpic("borde.gif")
        self.windown.setup(width=600, height=600)
        self.windown.tracer(0)
        self.windown.listen()
        self.windown.onkeypress(self.up, "Up")
        self.windown.onkeypress(self.down, "Down")
        self.windown.onkeypress(self.left, "Left")
        self.windown.onkeypress(self.right, "Right")
        self.cabeza()
        self.comida()
        self.textos()
        self.controlSnake()


    def cabeza(self):
        head.speed(0)
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "Stop"
    
    def comida(self):
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0, 100)

    def textos(self):
        text.speed(0)
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0, 260)
        text.write("Score: 0       High Score: 0",
        align="center", font = ("Courier", 18, "normal"))

    def up(self):
        head.direction = "up"

    def down(self):
        head.direction = "down"

    def left(self):
        head.direction = "left"

    def right(self):
        head.direction = "right"

    def moveSnake(self):
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    
    def controlSnake(self):
        score = 0
        highScore = 0
        windown = turtle.Screen()
        while True:
            windown.update()

            #Colisiones bordes 
            if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                #Esconder segmentos
                for seg in segment:
                    seg.goto(1000, 1000)
                #Limpiar lista de segmentos
                segment.clear()
            
                #Resetear marcador
                score = 0
                text.clear()
                text.write("Score: {}       High Score: {}".format(score, highScore),
                align="center", font = ("Courier", 18, "normal"))

            #Colision con la comida
            if head.distance(food) < 20:
                #Mover la comida a posicion random
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                food.goto(x, y)

                newSegment = turtle.Turtle()
                newSegment.speed(0)
                newSegment.shape("square")
                newSegment.color("grey")
                newSegment.penup() 
                segment.append(newSegment)

                #Aumentar marcador
                score += 10
                if score > highScore:
                    highScore = score

                text.clear()
                text.write("Score: {}       High Score: {}".format(score, highScore),
                align="center", font = ("Courier", 18, "normal"))
    
            #Mover cuerpo de la serpiente
            totalSeg = len(segment)
            for index in range(totalSeg - 1, 0, -1):
                x = segment[index - 1].xcor()
                y = segment[index - 1].ycor()
                segment[index].goto(x, y)
            if totalSeg > 0:
                x = head.xcor()
                y = head.ycor()
                segment[0].goto(x, y)

            ventana = Ventana
            ventana.moveSnake(self)

            #Colisiones con el cuerpo
            for seg in segment:
                if seg.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    #Esconder segmentos
                    for seg in segment:
                        seg.goto(1000, 1000)
                    segment.clear()

                    #Resetear marcador
                    score = 0
                    text.clear()
                    text.write("Score: {}       High Score: {}".format(score, highScore),
                    align="center", font = ("Courier", 18, "normal"))
            
            time.sleep(posponer)   

def run():
    if __name__ == "__main__":
        window = turtle
        Ventana(window)
        window.mainloop()

run()