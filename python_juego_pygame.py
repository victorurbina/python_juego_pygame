import pygame
from pygame.locals import *

#inicializo pygame
pygame.init()

#titulo de la ventana, creditos
pygame.display.set_caption("Juego Pygame by Ing. Victor E. Urbina")

#creacion de variables globales
global ventana

#creacion modular de metodos

#dibujar la superficie=ventana
def dibujar_superficie(size_x,size_y):
    superficie=pygame.display.set_mode((size_x,size_y))
    return superficie

#inicializo la ventana
ventana=dibujar_superficie(400,300)

#defino el color con que voy a pintar
def colorear(rojo,verde,azul):
    color=pygame.Color(rojo,verde,azul)
    return color

#dibujar una linea en la ventana
def dibujar_linea(superficie,color,p1_x,p1_y,p2_x,p2_y,grueso):
    pygame.draw.line(superficie,color,(p1_x,p1_y),(p2_x,p2_y),grueso)

#realizo la linea
color_linea=colorear(255,0,0)
dibujar_linea(ventana,color_linea,20,130,100,170,8)

#dibujar un circulo en la ventana
def dibujar_circulo(superficie,color,p1_x,p1_y,radio):
    pygame.draw.circle(superficie,color,(p1_x,p1_y),radio)

#realizo el circulo
color_circulo=colorear(0,150,255)
dibujar_circulo(ventana,color_circulo,70,110,5)

#dibujar un rectangulo en la ventana
def dibujar_rectangulo(superficie,color,p1_x,p1_y,ancho,largo):
    pygame.draw.rect(superficie,color,(p1_x,p1_y,ancho,largo))

#realizo el circulo
color_rectangulo=colorear(0,255,155)
dibujar_rectangulo(ventana,color_rectangulo,60,120,25,70)

#dibujar un poligono en la ventana
def dibujar_poligono(superficie,color,p1_x,p1_y,p2_x,p2_y,p3_x,p3_y,p4_x,p4_y,p5_x,p5_y):
    pygame.draw.polygon(superficie,color,((p1_x,p1_y),(p2_x,p2_y),(p3_x,p3_y),(p4_x,p4_y),(p5_x,p5_y)))

#realizo el circulo
color_poligono=colorear(155,0,155)
dibujar_poligono(ventana,color_poligono,70,10,140,50,110,100,30,100,0,50)

#inicializo el color de fondo de la ventana
color_ventana=colorear(150,100,50)

while True:
    
    #ventana.fill(color_ventana)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



