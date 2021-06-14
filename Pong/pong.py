import turtle
import threading
import time
from playsound import playsound


class PingPong:
    def __init__(self,ventana) :
        self.windows = ventana.Screen()
        self.score_a = 0
        self.score_b = 0
        self.paddle_a = ventana.Turtle()
        self.paddle_b = ventana.Turtle()
        self.line = ventana.Turtle()
        self.ball = ventana.Turtle()
        self.static = True
        self.pen = ventana.Turtle()
        self.pen2 = ventana.Turtle()
        #-------------

    def areaJuego(self):
        wn = turtle.Screen()
        self.windows.title("Pong")
        self.windows.bgcolor("#A9A9A9")
        self.windows.setup(width=800, height=600)
        self.windows.tracer(0)
    
    def palaA(self):


        
        #PALA A
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-350, 0)

    def palaB(self):
        #PALA B
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(350, 0)

    def lineaMedio(self):
        #LINEA DIVISORIA
        self.line.speed(0)
        self.line.shape("square")
        self.line.color("gray")
        self.line.shapesize(stretch_wid=30, stretch_len=0.07)
        self.line.penup()
        self.line.goto(0, 0)  

    def pelota(self):
        #PELOTA
        
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.9
        self.ball.dy = 0.9
        self.static = True      

    def marcadorInicial(self):
        #MARCADOR INICIAL
        
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-2.5, 220)
        self.pen.write("0       0",align="center", font=("Fixedsys", 60, "bold"))

    def marcadorEnter(self):
        #MENSAJE "ENTER".
        
        self.pen2.speed(0)
        self.pen2.color("black")
        self.pen2.penup()
        self.pen2.hideturtle()
        self.pen2.goto(0, 120)
        self.pen2.write("Presione la Tecla Enter",align="center", font=("Fixedsys", 24, "bold"))
    
    def update_score(self):
        #ACTUALIZA MARCADOR.
        self.pen.clear()
        self.pen.write("{}       {}".format(self.score_a,self.score_b),
        align="center", font=("Fixedsys", 60, "bold"))  

    def paddle_a_up(self):
        #MOVER PALA "A" HACIA ARRIBA
        y = self.paddle_a.ycor()
        if y <= 240:
            y += 20
            self.paddle_a.sety(y)

    
    def paddle_a_down(self):
        #MOVER PALA "A" HACIA ABAJO
        y = self.paddle_a.ycor()
        if y >= -220:
            y -= 20
            self.paddle_a.sety(y)

    
    def paddle_b_up(self):
        #MOVER PARA "B" HACIA ARRIBA
        y = self.paddle_b.ycor()
        if y <= 240:
            y += 20
            self.paddle_b.sety(y)

    
    def paddle_b_down(self):
        #MOVER PALA "B" HACIA ABAJO
        y = self.paddle_b.ycor()
        if y >= -220:
            y -= 20
            self.paddle_b.sety(y)

    
    def play_sound(self):
        #REPRODUCCIÓN DE SONIDO
        playsound("pong.mp3")

    
    def init_playsoun(self):
        #INICAR TAREA EN SEGUNDO PLANO
        t = threading.Thread(target=self.play_sound)
        t.start()

       
    def init_game(self):
        #INICIAR JUEGO 
        global static
        self.static = False
        self.pen2.clear()

    
    def reset_screen(self):
        #RESTAURAR PANTALLA DE INICIO
        self.ball.goto(0, 0)
        self.ball.dx *= -1    
        self.pen2.write("PRESIONE LA TECLA ENTER PARA EMPEZAR",
        align="center", font=("Fixedsys", 24, "bold"))
        self.paddle_a.goto(-350, 0)
        self.paddle_b.goto(350, 0)

    def registroEventos(self):

        #REGISTRAR EVENTOS DE TECLADO.    
        self.windows.listen()
        self.windows.onkeypress(self.paddle_a_up(), "w")
        self.windows.onkeypress(self.paddle_a_down(), "s")
        self.windows.onkeypress(self.paddle_b_up(), "Up")
        self.windows.onkeypress(self.paddle_b_down(), "Down")
        self.windows.onkeypress(self.init_game(), "Return")

    def desarrolloJuego(self):
        #DESARROLLO DEL JUEGO.
        while True:
            try:
                self.windows.update()
                #MOVER PELOTA
                if self.static == False:
                    self.ball.setx(self.ball.xcor() + self.ball.dx)
                    self.ball.sety(self.ball.ycor() + self.ball.dy)

                #REBOTE EN EL MARGEN SUPERIOR.
                if self.ball.ycor() > 290:
                    self.ball.sety(290)
                    self.ball.dy *= -1
                    self.init_playsoun()

                #REBOTE EN EL MARGEN INFERIOR.
                if self.ball.ycor() < -290:
                    self.ball.sety(-290)
                    self.ball.dy *= -1
                    self.init_playsoun()

                #PELOTA SOBREPASA LA PALA B
                if self.ball.xcor() > 390:
                    self.score_a += 1
                    self.update_score()
                    self.static = True
                    time.sleep(1)
                    self.reset_screen()

                #PELOTA SOBREPASA LA PALA A
                if self.ball.xcor() < -390:
                    self.score_b += 1
                    self.update_score()
                    self.static = True
                    time.sleep(1)
                    self.reset_screen()

                #REBOTE EN LA PALA B.
                if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < self.paddle_b.ycor() + 50 and self.ball.ycor() > self.paddle_b.ycor() - 50):
                    self.ball.setx(340)
                    self.ball.dx *= -1
                    self.init_playsoun()

                #REBOTE EN LA PALA A
                if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < self.paddle_a.ycor() + 50 and self.ball.ycor() > self.paddle_a.ycor() - 50):
                    self.ball.setx(-340)
                    self.ball.dx *= -1        
                    self.init_playsoun()
            except:
                break
    
    def correr(self):
        self.areaJuego()
        self.palaA()
        self.palaB()
        self.lineaMedio()
        self.pelota()
        self.marcadorInicial()
        self.marcadorEnter()
        self.update_score()
        self.paddle_a_up()
        self.paddle_a_down()
        self.paddle_b_up()
        self.paddle_b_down()
        #self.play_sound()
        #self.init_playsoun()
        self.init_game()
        self.reset_screen()
        self.registroEventos()
        self.desarrolloJuego()
        
#---------------------
windows = turtle
juego = PingPong(windows)
juego.correr()