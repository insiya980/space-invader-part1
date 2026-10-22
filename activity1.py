import math, random, pygame

SCREEN_HEIGHT=500
SCREEN_WIDTH=800

PLAYER_START_X=370
PLAYER_START_Y=380

ENEMY_START_Y_MAX=150
ENEMY_START_Y_MIN=50

ENEMY_SPEED_X=0.25
ENEMY_SPEED_Y=5

BULLET_SPEED_Y=1
COLLISION_DISTANCE=27

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BACKGROUND=pygame.image.load("bg.jpeg")
BACKGROUND=pygame.transformation.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space invader ")
ICON=pygame.display.image.load("SI logo.png ")
pygame.display.set_icon(ICON)
PLAYER_IMG=pygame.image.load("ufo.png ")
PLAYER_IMG=pygame.transform.scale(PLAYER_IMG,(80,80))
playerX=PLAYER_START_X
playerY=PLAYER_START_Y

playerX_change=0
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]

number_of_enemies=6
for _i in range(number_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_img[_i]=pygame.transform.scale(enemy_img[_i],(70,70))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_img=pygame.image.load("bullet.png")
bullet_img=pygame.transform.scale(bullet_img,(52,52))
bullet_x=0
bullet_y=PLAYER_START_Y
bullet_x_change=0
bullet_y_change=BULLET_SPEED_Y
bullet_state="ready"