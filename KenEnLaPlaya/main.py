import pygame
import os
import random

pygame.init()

# CONSTANTES
ALTURA = 600
ANCHO = 1100
SCREEN = pygame.display.set_mode((ANCHO, ALTURA))

# Musica
pygame.mixer_music.load('musica.ogg')

# Fondo del juego
BG = pygame.image.load(os.path.join("Assets/Fondo", "fondo_2.jpg"))

KEN_CORRE = [pygame.image.load(os.path.join("Assets/Ken", "ken1.png")),
             pygame.image.load(os.path.join("Assets/Ken", "ken2.png"))]
KEN_SALTA = pygame.image.load(os.path.join("Assets/Ken", "ken0.png"))
OBSTACULO_PLAYA = [pygame.image.load(os.path.join("Assets/Obstaculos_Playa", "racket.png")),
                   pygame.image.load(os.path.join("Assets/Obstaculos_Playa", "beach-ball.png")),
                   pygame.image.load(os.path.join("Assets/Obstaculos_Playa", "surfing-board.png"))]

OBSTACULO_PLAYA_2 = [pygame.image.load(os.path.join("Assets/Obstaculos_Castillo", "sand-castle.png")),
                     pygame.image.load(os.path.join("Assets/Obstaculos_Castillo", "sand-castle_2.png")),
                     pygame.image.load(os.path.join("Assets/Obstaculos_Castillo", "sand-castle_3.png"))]

# Musica
pygame.mixer_music.load('musica.ogg')


# Creación del personaje
class Ken:
    X_POS = 80
    Y_POS = 380
    VELOCIDAD_SALTO = 8.5

    def __init__(self):
        self.correr_img = KEN_CORRE
        self.salta_img = KEN_SALTA

        self.KEN_CORRE = True
        self.ken_salta = False

        self.numero_pasos = 0
        self.velocidad_salto = self.VELOCIDAD_SALTO
        self.imagen = self.correr_img[0]
        self.ken_rect = self.imagen.get_rect()
        self.ken_rect.x = self.X_POS
        self.ken_rect.y = self.Y_POS

    def update(self, entradaUsuario):
        if self.KEN_CORRE:
            self.correr()
        if self.ken_salta:
            self.salta()

        if self.numero_pasos >= 10:
            self.numero_pasos = 0

        if entradaUsuario[pygame.K_UP] and not self.ken_salta:
            self.KEN_CORRE = False
            self.ken_salta = True
        elif not (self.ken_salta or entradaUsuario[pygame.K_DOWN]):
            self.KEN_CORRE = True
            self.ken_salta = False

    def correr(self):
        self.imagen = self.correr_img[self.numero_pasos // 5]
        self.ken_rect = self.imagen.get_rect()
        self.ken_rect.x = self.X_POS
        self.ken_rect.y = self.Y_POS
        self.numero_pasos += 1

    def salta(self):
        self.imagen = self.salta_img
        if self.ken_salta:
            self.ken_rect.y -= self.velocidad_salto * 4
            self.velocidad_salto -= 0.8
        if self.velocidad_salto < - self.VELOCIDAD_SALTO:
            self.ken_salta = False
            self.velocidad_salto = self.VELOCIDAD_SALTO

    def draw(self, SCREEN):
        SCREEN.blit(self.imagen, (self.ken_rect.x, self.ken_rect.y))


#### Obstáculo ####
class Obstaculo:
    def __init__(self, imagen, type):
        self.imagen = imagen
        self.type = type
        self.rect = self.imagen[self.type].get_rect()
        self.rect.x = ANCHO

    def update(self):
        self.rect.x -= velocidad_juego
        if self.rect.x < -self.rect.width:
            obstaculos.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.imagen[self.type], self.rect)


#### Obstáculo playa
class ObstaculosPlaya(Obstaculo):
    def __init__(self, imagen):
        self.type = random.randint(0, 2)
        super().__init__(imagen, self.type)
        self.rect.y = 450


class ObstaculosCastillo(Obstaculo):
    def __init__(self, imagen):
        self.type = random.randint(0, 2)
        super().__init__(imagen, self.type)
        self.rect.y = 450


def main():
    global velocidad_juego, x_pos_bg, y_pos_bg, puntos, obstaculos
    correr = True
    reloj = pygame.time.Clock()
    jugador = Ken()
    velocidad_juego = 20
    x_pos_bg = 0
    y_pos_bg = 0
    puntos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstaculos = []
    vidas_perdidas = 0

    def puntaje():
        global puntos, velocidad_juego
        puntos += 1
        if puntos % 100 == 0:
            velocidad_juego += 1

        text = font.render("puntos: " + str(puntos), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def fondo():
        global x_pos_bg, y_pos_bg
        ancho_imagen = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (ancho_imagen + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -ancho_imagen:
            SCREEN.blit(BG, (ancho_imagen + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= velocidad_juego

    while correr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False

        SCREEN.fill((255, 255, 255))
        entradaUsuario = pygame.key.get_pressed()
        fondo()
        jugador.draw(SCREEN)
        jugador.update(entradaUsuario)

        if len(obstaculos) == 0:
            if random.randint(0, 1) == 0:
                obstaculos.append(ObstaculosPlaya(OBSTACULO_PLAYA))
            elif random.randint(0, 1) == 1:
                obstaculos.append(ObstaculosCastillo(OBSTACULO_PLAYA_2))

        for obstacle in obstaculos:
            obstacle.draw(SCREEN)
            obstacle.update()
            if jugador.ken_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                vidas_perdidas += 1
                pygame.mixer_music.stop()
                menu(vidas_perdidas)

        puntaje()

        reloj.tick(30)
        pygame.display.update()


def menu(vidas_perdidas):
    global puntos
    correr = True
    while correr:
        SCREEN.fill((255, 203, 219))
        font = pygame.font.Font('barbie.ttf', 30)
        pygame.mixer_music.play(-1)

        if vidas_perdidas == 0:
            text = font.render("Presiona cualquier tecla para iniciar", True, (0, 0, 0))

        elif vidas_perdidas > 0:
            text = font.render("Presiona cualquier tecla para jugar de nuevo", True, (0, 0, 0))
            score = font.render("Tu puntaje es: " + str(puntos), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (ANCHO // 2, ALTURA // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (ANCHO // 2, ALTURA // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(KEN_CORRE[0], (ANCHO // 2 - 20, ALTURA // 2 - 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.KEYDOWN:
                main()


menu(0)