import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-man")

# Cores
black = (0, 0, 0) # set a   
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Configurações do Pac-man
pacman_size = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Configurações do fantasma
ghost_size = 20
ghost_x = random.randint(0, screen_width - ghost_size)
ghost_y = random.randint(0, screen_height - ghost_size)
ghost_speed = 3

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do Pac-man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Movimentação do fantasma
    if ghost_x < pacman_x:
        ghost_x += ghost_speed
    if ghost_x > pacman_x:
        ghost_x -= ghost_speed
    if ghost_y < pacman_y:
        ghost_y += ghost_speed
    if ghost_y > pacman_y:
        ghost_y -= ghost_speed

    # Verifica colisão
    if abs(pacman_x - ghost_x) < pacman_size and abs(pacman_y - ghost_y) < pacman_size:
        running = False

    # Desenha tudo na tela
    screen.fill(black)
    pygame.draw.rect(screen, yellow, (pacman_x, pacman_y, pacman_size, pacman_size))
    pygame.draw.rect(screen, red, (ghost_x, ghost_y, ghost_size, ghost_size))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
# Função para desenhar o labirinto
def draw_maze():
    maze = [
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.####.##.########.##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.##### ## #####.######",
        "######.##### ## #####.######",
        "######.##          ##.######",
        "######.## ###--### ##.######",
        "######.## #      # ##.######",
        "######.## #      # ##.######",
        "######.## ######## ##.######",
        "######.##          ##.######",
        "######.## ######## ##.######",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.##..........##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.#####.##.#####.######",
        "######.#####.##.#####.######",
        "#............##............#",
        "############################"
    ]
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "#":
                pygame.draw.rect(screen, white, (x * pacman_size, y * pacman_size, pacman_size, pacman_size))

# Função para verificar colisão com o labirinto
def check_collision(x, y):
    maze = [
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.####.##.########.##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.##### ## #####.######",
        "######.##### ## #####.######",
        "######.##          ##.######",
        "######.## ###--### ##.######",
        "######.## #      # ##.######",
        "######.## #      # ##.######",
        "######.## ######## ##.######",
        "######.##          ##.######",
        "######.## ######## ##.######",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.##..........##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.#####.##.#####.######",
        "######.#####.##.#####.######",
        "#............##............#",
        "############################"
    ]
    x_index = x // pacman_size
    y_index = y // pacman_size
    if maze[y_index][x_index] == "#":
        return True
    return False

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do Pac-man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not check_collision(pacman_x - pacman_speed, pacman_y):
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT] and not check_collision(pacman_x + pacman_speed, pacman_y):
        pacman_x += pacman_speed
    if keys[pygame.K_UP] and not check_collision(pacman_x, pacman_y - pacman_speed):
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN] and not check_collision(pacman_x, pacman_y + pacman_speed):
        pacman_y += pacman_speed

    # Movimentação do fantasma
    if ghost_x < pacman_x and not check_collision(ghost_x + ghost_speed, ghost_y):
        ghost_x += ghost_speed
    if ghost_x > pacman_x and not check_collision(ghost_x - ghost_speed, ghost_y):
        ghost_x -= ghost_speed
    if ghost_y < pacman_y and not check_collision(ghost_x, ghost_y + ghost_speed):
        ghost_y += ghost_speed
    if ghost_y > pacman_y and not check_collision(ghost_x, ghost_y - ghost_speed):
        ghost_y -= ghost_speed

    # Verifica colisão
    if abs(pacman_x - ghost_x) < pacman_size and abs(pacman_y - ghost_y) < pacman_size:
        running = False

    # Desenha tudo na tela
    screen.fill(black)
    draw_maze()
    pygame.draw.rect(screen, yellow, (pacman_x, pacman_y, pacman_size, pacman_size))
    pygame.draw.rect(screen, red, (ghost_x, ghost_y, ghost_size, ghost_size))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
