import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Defensor Eléctrico")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Colores
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Variables
player_pos = [400, 500]
enemy_list = []
score = 0
game_active = False


# ================= FUNCIONES =================

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], 50, 50))


def spawn_enemy():
    x_pos = random.randint(0, WIDTH - 50)
    enemy_list.append([x_pos, 0])


def move_enemies():
    global game_active
    for enemy in enemy_list:
        enemy[1] += 5
        if enemy[1] > HEIGHT:
            game_active = False


def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], 50, 50))


def detect_collision():
    global score
    for enemy in enemy_list:
        if abs(enemy[0] - player_pos[0]) < 50 and abs(enemy[1] - player_pos[1]) < 50:
            enemy_list.remove(enemy)
            score += 1


def draw_score():
    text = font.render(f"Puntos: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def main_menu():
    screen.fill((0, 0, 0))
    title = font.render("DEFENSOR ELÉCTRICO", True, WHITE)
    start = font.render("Presiona ENTER para comenzar", True, WHITE)
    screen.blit(title, (250, 200))
    screen.blit(start, (200, 300))
    pygame.display.update()


# ================= BUCLE PRINCIPAL =================

while True:

    if not game_active:
        main_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_active = True
            enemy_list.clear()
            score = 0
        continue

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Generar enemigos
    if random.randint(1, 30) == 1:
        spawn_enemy()

    move_enemies()
    detect_collision()

    draw_player()
    draw_enemies()
    draw_score()

    pygame.display.update()
    clock.tick(60)
