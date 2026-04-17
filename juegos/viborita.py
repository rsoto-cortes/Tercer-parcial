import turtle
import time
import random

posponer = 0.1
segmentos = []

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de Snake")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# Funciones de movimiento
def arriba(): cabeza.direction = "up"
def abajo(): cabeza.direction = "down"
def izquierda(): cabeza.direction = "left"
def derecha(): cabeza.direction = "right"

def mover():
    if cabeza.direction == "up": cabeza.sety(cabeza.ycor() + 20)
    if cabeza.direction == "down": cabeza.sety(cabeza.ycor() - 20)
    if cabeza.direction == "left": cabeza.setx(cabeza.xcor() - 20)
    if cabeza.direction == "right": cabeza.setx(cabeza.xcor() + 20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

while True:
    ventana.update()

    # Colisión con la comida
    if cabeza.distance(comida) < 20:
        comida.goto(random.randint(-280, 280), random.randint(-280, 280))
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("lightgreen")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    # Mover el cuerpo
    for i in range(len(segmentos) - 1, 0, -1):
        segmentos[i].goto(segmentos[i-1].xcor(), segmentos[i-1].ycor())
    if len(segmentos) > 0:
        segmentos[0].goto(cabeza.xcor(), cabeza.ycor())

    mover()

    # Colisión con bordes
    if abs(cabeza.xcor()) > 290 or abs(cabeza.ycor()) > 290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        for s in segmentos: s.goto(1000, 1000)
        segmentos.clear()

    time.sleep(posponer)