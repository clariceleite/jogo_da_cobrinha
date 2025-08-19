import turtle
import time
import random

delay = 0.1

pontuacao = 0
maior_pontuacao = 0

# Configuração da tela
saida = turtle.Screen()
saida.title("Jogo da Cobra")
saida.bgcolor("yellow")
saida.setup(width=600, height=600)
saida.tracer(0)  # Desativa a animação automática

#cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("black")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

#comida da cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

#corpo da cobra
corpo = []

# Pontuação
pontuacao_display = turtle.Turtle()
pontuacao_display.speed(0)
pontuacao_display.shape("square")
pontuacao_display.color("black")
pontuacao_display.penup()
pontuacao_display.hideturtle()
pontuacao_display.goto(0, 260)
pontuacao_display.write("Pontuação: 0  Maior Pontuação: 0", align="center", font=("Courier", 24, "normal")) 

#Funções
def mover():
    if cabeca.direction == "cima":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "baixo":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "esquerda":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direction == "direita":
        x = cabeca.xcor()
        cabeca.setx(x + 20)
def cima():
    if cabeca.direction != "baixo":
        cabeca.direction = "cima"
def baixo():
    if cabeca.direction != "cima":
        cabeca.direction = "baixo"
def esquerda():
    if cabeca.direction != "direita":
        cabeca.direction = "esquerda"
def direita():
    if cabeca.direction != "esquerda":
        cabeca.direction = "direita"

# Teclado
saida.listen()
saida.onkeypress(cima, "w")
saida.onkeypress(baixo, "s")
saida.onkeypress(esquerda, "a")
saida.onkeypress(direita, "d")

# Loop principal do jogo
while True:
    saida.update()  # Atualiza a tela
    # Verifica colisão com as bordas da tela
    if (cabeca.xcor() > 290 or cabeca.xcor() < -290 or 
            cabeca.ycor() > 290 or cabeca.ycor() < -290):
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"
        # Esvaziar o corpo da cobra
        for segmento in corpo:
            segmento.goto(1000, 1000)  # Move os segmentos para fora da tela
        corpo.clear()
        # Resetar a pontuação
        pontuacao = 0
        # Resetar Delay
        delay = 0.1
        pontuacao_display.clear()
        pontuacao_display.write(f"Pontuação: {pontuacao}  Maior Pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))  

    # Verifica colisão com a comida
    if cabeca.distance(comida) < 20:
        # Mover a comida para uma nova posição aleatória
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        # Adicionar um segmento ao corpo da cobra
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("black")
        novo_segmento.penup()
        corpo.append(novo_segmento)

        # Diminuir o delay
        delay -= 0.001
        # Aumentar a pontuação
        pontuacao += 10

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
        pontuacao_display.clear()
        pontuacao_display.write(f"Pontuação: {pontuacao}  Maior Pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))

    # Mover o corpo da cobra
    for index in range(len(corpo) - 1, 0, -1):
        x = corpo[index - 1].xcor()
        y = corpo[index - 1].ycor()
        corpo[index].goto(x, y)
    # Mover o primeiro segmento do corpo para a posição da cabeça
    if len(corpo) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        corpo[0].goto(x, y)
    mover()
    # Verifica colisão com o corpo da cobra
    for segmento in corpo:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direction = "stop"

            # Esvaziar o corpo da cobra
            for segmento in corpo:
                segmento.goto(1000, 1000)  # Move os segmentos para fora da tela
            corpo.clear()
            # Resetar a pontuação
            pontuacao = 0
            # Resetar Delay
            delay = 0.1      

            # Atualizar a pontuação na tela
            pontuacao_display.clear()
            pontuacao_display.write(f"Pontuação: {pontuacao}  Maior Pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)  # Controla a velocidade do jogo
saida.mainloop()  # Mantém a janela aberta
# Finaliza o jogo
