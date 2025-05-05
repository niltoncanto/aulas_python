import turtle

# Classe para a Bola
class Bola:
    def __init__(self):
        self.bola = turtle.Turtle()
        self.bola.speed(1)  # Define a velocidade da animação
        self.bola.shape("circle")
        self.bola.color("white")
        self.bola.penup()
        self.bola.goto(0, 0)
        self.bola.dx = 1  # Define a direção no eixo x
        self.bola.dy = -1  # Define a direção no eixo y

    def mover(self):
        x = self.bola.xcor()
        y = self.bola.ycor()
        self.bola.setx(x + self.bola.dx)
        self.bola.sety(y + self.bola.dy)

# Classe para a Raquete
class Raquete:
    def __init__(self, x, y):
        self.raquete = turtle.Turtle()
        self.raquete.speed(0)
        self.raquete.shape("square")
        self.raquete.color("white")
        self.raquete.shapesize(stretch_wid=6, stretch_len=1)
        self.raquete.penup()
        self.raquete.goto(x, y)

    def subir(self):
        y = self.raquete.ycor()
        if y < 250:
            y += 20
            self.raquete.sety(y)

    def descer(self):
        y = self.raquete.ycor()
        if y > -240:
            y -= 20
            self.raquete.sety(y)

# Configuração da tela
tela = turtle.Screen()
tela.title("Pong")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Criação das raquetes e bola
raquete_esquerda = Raquete(-350, 0)
raquete_direita = Raquete(350, 0)
bola = Bola()

# Controles
tela.listen()
tela.onkeypress(raquete_esquerda.subir, "w")
tela.onkeypress(raquete_esquerda.descer, "s")
tela.onkeypress(raquete_direita.subir, "Up")
tela.onkeypress(raquete_direita.descer, "Down")

# Loop principal do jogo
while True:
    tela.update()
    bola.mover()

    # Colisão com as bordas superior e inferior
    if bola.bola.ycor() > 290 or bola.bola.ycor() < -290:
        bola.bola.dy *= -1

    # Colisão com as raquetes
    if (bola.bola.dx > 0) and (350 > bola.bola.xcor() > 340) and (raquete_direita.raquete.ycor() + 50 > bola.bola.ycor() > raquete_direita.raquete.ycor() - 50):
        bola.bola.dx *= -1

    if (bola.bola.dx < 0) and (-350 < bola.bola.xcor() < -340) and (raquete_esquerda.raquete.ycor() + 50 > bola.bola.ycor() > raquete_esquerda.raquete.ycor() - 50):
        bola.bola.dx *= -1

    # Bola sai da tela
    if bola.bola.xcor() > 390 or bola.bola.xcor() < -390:
        bola.bola.goto(0, 0)
        bola.bola.dx *= -1
