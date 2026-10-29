import math, random, pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MAX = 150
ENEMY_START_Y_MIN = 50

ENEMY_SPEED_X = 0.25
ENEMY_SPEED_Y = 5

BULLET_SPEED_Y = 1
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load("bg.jpeg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space invader")
ICON = pygame.image.load("SI logo.png")
pygame.display.set_icon(ICON)
PLAYER_IMG = pygame.image.load("ufo.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (80, 80))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y

playerX_change = 0
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

number_of_enemies = 6
for _i in range(number_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_img[_i] = pygame.transform.scale(enemy_img[_i], (70, 70))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (52, 52))
bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_x_change = 0
bullet_y_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x, text_y = 10, 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x, y):
    screen.blit(PLAYER_IMG, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(BACKGROUND, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = playerX
                    fire_bullet(bullet_x, bullet_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0
                    
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))
    
    for i in range(number_of_enemies):
        if enemyY[i] > 340:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        
        if is_collision(enemyX[i], enemyY[i], bullet_x, bullet_y):
            bullet_y = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
            
        enemy(enemyX[i], enemyY[i], i)
    
    if bullet_y <= 0:
        bullet_y = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        
    player(playerX, playerY)
    show_score(text_x, text_y)
    pygame.display.update()