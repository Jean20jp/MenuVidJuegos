

import pygame

pygame.font.init()

ALTURA = 600
ANCHO = 1000
PANTALLA_ALTURA = 800
PANTALLA_ANCHO = 1200
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
GRIS = (128, 128, 128)
AZUL = (0, 0, 255)

win = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTURA))
win.fill(GRIS)
pygame.display.set_caption("Pong")

class Bloque():
    def __init__(self, x, y, ancho, altura, color):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.color = color
        self.rect = (x, y, ancho, altura)
        self.mov = 8
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
    
    def mover(self, bloque, superior, inferior):

        teclas = pygame.key.get_pressed()# 0 - 1
        # [a=0, b=1, c, ...]
        if bloque == 2:
            if teclas[pygame.K_UP]:
                self.y -= self.mov# self.y = self.y - self.mov
                if self.y <= superior:
                    self.y += self.mov
            
            if teclas[pygame.K_DOWN]:
                self.y += self.mov# self.y = self.y +self.mov
                if self.y + self.altura >= inferior:
                    self.y -= self.mov
                
        if bloque == 1:
            if teclas[pygame.K_w]:
                self.y -= self.mov# self.y = self.y - self.mov
                if self.y <= superior:
                    self.y += self.mov
            
            if teclas[pygame.K_s]:
                self.y += self.mov# self.y = self.y +self.mov
                if self.y + self.altura >= inferior:
                    self.y -= self.mov
            
        
        self.actualizar()
        
    def actualizar(self):
        self.rect = (self.x, self.y, self.ancho, self.altura)

class Bola():
    def __init__(self, x, y, radio, color):
        self.x = x
        self.initx = x
        self.y = y
        self.inity = y
        self.radio = radio
        self.color = color
        self.centro = (x, y)
        self.movx = 8
        self.movy = 8
        self.golpear1 = False
        self.golpear2 = False
        
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, self.centro, self.radio)
        # Enteros(Integer) - 0, 15, -22
        # Flotantes(Float) - 15.2, 3.7, 1.0
    
    def mover(self, superior, inferior, izq, der, bloque_1, bloque_2):
        self.x += self.movx # self.x = self.x + self.movx
        self.y += self.movy
        
        if self.y - self.radio <= superior:
            self.movy *= -1
        
        if self.y + self.radio >= inferior:
            self.movy *= -1
        
        if self.x - self.radio <= izq:
            self.x = self.initx
            self.y = self.inity
            self.reset()
            self.movx *= -1
            return 2
            
        if self.x + self.radio >= der:
            self.x = self.initx
            self.y = self.inity
            self.reset()
            self.movx *= -1
            return 1
        
        if bloque_2.x + bloque_2.ancho >= self.x + self.radio >= bloque_2.x:
            if bloque_2.y + bloque_2.altura >= self.y + self.radio >= bloque_2.y:
                if not self.golpear2:
                    self.movx *= -1
                    self.golpear2 = True
                    self.golpear1 = False
                
        if bloque_1.x <= self.x - self.radio <= bloque_1.x + bloque_1.ancho:
            if bloque_1.y + bloque_1.altura >= self.y + self.radio >= bloque_1.y:
                if not self.golpear1:
                    self.movx *= -1
                    self.golpear1 = True
                    self.golpear2 = False
            
                
        self.actualizar()
    
    def actualizar(self):
        self.centro = (self.x, self.y)
    
    def reset(self):
        self.golpear2 = False
        self.golpear1 = False

#Funciones

def ganador(ventana, Jugador):
    fuente = pygame.font.SysFont("Arial", 100, True)
    texto = "Gano el jugador " + str(Jugador) + "!"
    escribir = fuente.render(texto, 1, ROJO)
    ventana.blit(escribir, (PANTALLA_ANCHO/2-escribir.get_width()/2, PANTALLA_ALTURA/2- escribir.get_height()/2))
    pygame.display.update()
    

def dibujarpuntaje(ventana, puntaje_1, puntaje_2):
    fuente = pygame.font.SysFont("Arial", 50, True)
    texto = "Jugador 1: " + str(puntaje_1) + "      Jugador 2: " + str(puntaje_2)
    escribir = fuente.render(texto, 1, AZUL)
    ventana.blit(escribir, (PANTALLA_ANCHO/2-escribir.get_width()/2, 20))

def redibujarventana(ventana, bloque_1, bloque_2, bola, puntaje_1, puntaje_2):
    ventana.fill(GRIS)
    pygame.draw.rect(ventana, NEGRO, ((PANTALLA_ANCHO-ANCHO)/2, (PANTALLA_ALTURA-ALTURA)/2, ANCHO, ALTURA))
    bloque_1.dibujar(ventana)
    bloque_2.dibujar(ventana)
    bola.dibujar(ventana)
    dibujarpuntaje(ventana, puntaje_1, puntaje_2)
    pygame.display.update()

def principal():
    puntaje_1 = 0
    puntaje_2 = 0
    bandera = True
    reloj = pygame.time.Clock()
    
    #Objetos
    bloque_1 = Bloque(ANCHO/10+(PANTALLA_ANCHO-ANCHO)/2, PANTALLA_ALTURA/2-75, ANCHO/40, 150, BLANCO)
    bloque_2 = Bloque(PANTALLA_ANCHO-(PANTALLA_ANCHO-ANCHO)/2-(ANCHO/10+ANCHO/40), PANTALLA_ALTURA/2-75, ANCHO/40, 150, BLANCO)
    bola = Bola(int(round(PANTALLA_ANCHO/2)), int(round(PANTALLA_ALTURA/2)), int(round(ANCHO/50)), BLANCO)
    
    redibujarventana(win, bloque_1, bloque_2, bola, puntaje_1, puntaje_2)
    
    pygame.time.delay(500)
    
    while bandera:
        pygame.time.delay(50)# 1s - 1000ms
        reloj.tick(60)#FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera = False
                pygame.quit()
                
        bloque_1.mover(1, (PANTALLA_ALTURA-ALTURA)/2, PANTALLA_ALTURA-(PANTALLA_ALTURA-ALTURA)/2)
        bloque_2.mover(2, (PANTALLA_ALTURA-ALTURA)/2, PANTALLA_ALTURA-(PANTALLA_ALTURA-ALTURA)/2)
        punto = bola.mover((PANTALLA_ALTURA-ALTURA)/2, PANTALLA_ALTURA-(PANTALLA_ALTURA-ALTURA)/2, (PANTALLA_ANCHO-ANCHO)/2, PANTALLA_ANCHO-(PANTALLA_ANCHO-ANCHO)/2, bloque_1, bloque_2)
        
        if punto == 1:
            puntaje_1 += 1
        elif punto == 2:
            puntaje_2 += 1
                
        redibujarventana(win, bloque_1, bloque_2, bola, puntaje_1, puntaje_2)
        
        if puntaje_1 == 5:
            ganador(win, 1)
            pygame.time.delay(2000)
            bandera = False
        elif puntaje_2 == 5:
            ganador(win, 2)
            pygame.time.delay(2000)
            bandera = False

def menu():
    win.fill(NEGRO)
    fuente = pygame.font.SysFont("Arial", 100, True)
    texto = "PRESIONE PARA JUGAR"
    escribir = fuente.render(texto, 1, BLANCO)
    win.blit(escribir, (PANTALLA_ANCHO/2-escribir.get_width()/2, PANTALLA_ALTURA/2- escribir.get_height()/2))
    pygame.display.update()
    
    bandera = True
    
    while bandera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                principal()
    
    
    
menu()