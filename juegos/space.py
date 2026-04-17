
import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Duelo Espacial: Pro")

# Colores y Fuente
NEGRO, BLANCO, VERDE, ROJO, AMARILLO = (0,0,0), (255,255,255), (0,255,0), (255,0,0), (255,255,0)
fuente = pygame.font.SysFont("monospace", 35)
reloj = pygame.time.Clock()

# Jugador
jugador = pygame.Rect(ANCHO//2, ALTO-60, 50, 40)
balas_jugador = []
puntos = 0

# Enemigo
enemigo = pygame.Rect(random.randint(0, ANCHO-50), 50, 50, 50)
vel_enemigo = 4
balas_enemigo = []
ULTIMO_DISPARO = pygame.time.get_ticks()

def mostrar_texto(texto, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x, y))

# Bucle Principal
jugando = True
while jugando:
    ventana.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Disparo del jugador
                balas_jugador.append(pygame.Rect(jugador.centerx - 2, jugador.top, 5, 15))

    # Movimiento Jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0: jugador.x -= 7
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO: jugador.x += 7

    # IA del Enemigo (Movimiento y Disparo)
    enemigo.x += vel_enemigo
    if enemigo.right >= ANCHO or enemigo.left <= 0:
        vel_enemigo *= -1 # Rebota en las paredes
    
    # Disparo automático del enemigo cada 1.2 segundos
    tiempo_ahora = pygame.time.get_ticks()
    if tiempo_ahora - ULTIMO_DISPARO > 1200:
        balas_enemigo.append(pygame.Rect(enemigo.centerx - 2, enemigo.bottom, 5, 15))
        ULTIMO_DISPARO = tiempo_ahora

    # Lógica de Balas Jugador (Suben)
    for b in balas_jugador[:]:
        b.y -= 10
        if b.colliderect(enemigo):
            puntos += 10
            balas_jugador.remove(b)
            enemigo.x = random.randint(0, ANCHO-50) # El enemigo reaparece
        elif b.bottom < 0: balas_jugador.remove(b)

    # Lógica de Balas Enemigo (Bajan)
    for be in balas_enemigo[:]:
        be.y += 6
        if be.colliderect(jugador):
            print(f"GAME OVER! Puntos finales: {puntos}")
            jugando = False # Fin del juego si te dan
        elif be.top > ALTO: balas_enemigo.remove(be)

    # Dibujar todo
    pygame.draw.rect(ventana, VERDE, jugador)
    pygame.draw.rect(ventana, ROJO, enemigo)
    for b in balas_jugador: pygame.draw.rect(ventana, BLANCO, b)
    for be in balas_enemigo: pygame.draw.rect(ventana, AMARILLO, be)
    
    mostrar_texto(f"PUNTOS: {puntos}", BLANCO, 10, 10)
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()