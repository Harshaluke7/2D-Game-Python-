import pygame
import random
pygame.init()

SIZE = WIDTH , HEIGHT = 1200 , 700
SCREEN = pygame.display.set_mode(SIZE)
# RGB COLORS
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255
X_COLOR = 125, 200, 100

bulletSound = pygame.mixer.Sound("Assets/sounds/airplane-fly-by-01a.wav")
enemySound = pygame.mixer.Sound("Assets/sounds/airplane-fly-by-02.wav")

#homeScreen
def homeScreen():
    font1 = pygame.font.Font("Assets/sketch-gothic-school/Sketch Gothic School.ttf",100)
    text = font1.render("SPACE SHOOTER",True,RED)

    font2 = pygame.font.SysFont(None,60)
    text2 = font2.render("Press Space to Start",True,BLUE)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 main()
         SCREEN.blit(text,(200, 200))
         SCREEN.blit(text2, (390, 350))
         pygame.display.flip()

def gameOver():
    font = pygame.font.SysFont(None, 150)
    text = font.render(f"GAME_OVER", True, RED)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            SCREEN.blit(text, (200, 200))
            pygame.display.flip()


def youwin():
    font = pygame.font.SysFont(None, 150)
    text = font.render(f"YOU WIN", True, WHITE)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            SCREEN.blit(text, (200, 200))
            pygame.display.flip()

def playerHealth(count):
    font = pygame.font.SysFont(None, 60)
    text = font.render(f"Health : {count}", True, RED)
    SCREEN.blit(text, (50,500))


def main():
    move_x =0

    ship = pygame.image.load("Assets/images/images.png")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH // 2 - ship_w // 2
    ship_y = (HEIGHT - ship_h)

    enemyShip = pygame.image.load("Assets/images/enemyship.png")
    eship_w = enemyShip.get_width()
    eship_h = enemyShip.get_height()

    enemyList = []
    nrow = 2
    ncols = WIDTH // eship_w

    for i in range (nrow):
        for j in range (ncols):
            enemyX = eship_w * j
            enemyY = eship_h * i
            enemyRect = pygame.Rect(enemyX, enemyY, eship_w, eship_h)
            enemyList.append(enemyRect)

    #BulletCode
    bullet_w = 8
    bullet_h = 15
    bullet_y = ship_y
    moveBullet = 0

    # enemy bullets
    random_enemy = random.choice(enemyList)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_x = random_enemy.x + eship_w//2
    enemy_bullet_y = random_enemy.bottom - 10

    playerHealthCount = 100
    while True:
        bullet_x = ship_x + ship_w // 2
        evenList = pygame.event.get()
        for event in evenList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 0.8
                elif event.key == pygame.K_LEFT:
                    move_x = -0.8
                elif event.key == pygame.K_SPACE:
                    moveBullet = -5
                    bulletSound.play()
            else:
                move_x =0

        SCREEN.fill(WHITE)
        bullet_rect = pygame.draw.rect(SCREEN, GREEN, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += moveBullet
        SCREEN.blit(ship, (ship_x, ship_y))
        ship_x += move_x

        # player ship
        ship_rect = pygame.Rect(ship_x, ship_y, ship_w, ship_h)
        enemyBullet = pygame.draw.rect(SCREEN, GREEN, [enemy_bullet_x, enemy_bullet_y, enemy_bullet_w,enemy_bullet_h])
        enemy_bullet_y += 4

        for i in range (len(enemyList)):
            # enemyShip - image
            SCREEN.blit(enemyShip , (enemyList[i].x, enemyList[i].y))

        for i in range(len(enemyList)):
            if bullet_rect.colliderect(enemyList[i]):
                bullet_y = ship_y
                moveBullet = 0
                del enemyList[i]
                break

        if bullet_y < 0:
            bullet_y = ship_y
            moveBullet = 0

        if enemy_bullet_y > HEIGHT:
            random_enemy = random.choice(enemyList)
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemy_bullet_y = random_enemy.bottom - 10
            enemySound.play()


        if enemyBullet.colliderect(ship_rect):
            playerHealthCount -= 1
            enemy_bullet_y = HEIGHT+10


        if playerHealthCount == 0:
            gameOver()

        if len(enemyList) == 0:
            SCREEN.fill(BLACK)
            youwin()


        playerHealth(playerHealthCount)
        pygame.display.flip()

homeScreen()