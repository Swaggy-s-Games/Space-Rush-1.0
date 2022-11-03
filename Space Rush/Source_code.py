from cmath import rect
from pygame import mixer
import pygame
import random
import time

# intialize the pygame
pygame.init()

# intialize the mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# title and stuff
pygame.display.set_caption('Space Rush by @itsswaggy')
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

# create window
screen = pygame.display.set_mode((800, 600))

# start time
time.sleep(3)

# load the sounds
laser_fx = pygame.mixer.Sound("lazer.wav")
laser_fx.set_volume(0.55)

ex = pygame.mixer.Sound("explosion.wav")
ex.set_volume(0.60)

# background music
bgmusic = pygame.mixer.Sound("bgmusic.wav")
bgmusic.play(-1)
bgmusic.set_volume(0.75)

# score and stuff
score = -1
font = pygame.font.Font('Bubblegum.ttf', 32)

def show_score():
    score_value = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_value, (345, 20))

# baground
bg = pygame.image.load('bg.png')

# spaceship
playerImg = pygame.image.load('Spaceship.png')
hitbox = playerImg.get_rect()
vel = 2
hitbox.y = 268

# small asteroid
asteroid_smallImg = pygame.image.load('asteroid.png')
hitbox_ = asteroid_smallImg.get_rect()
vel_ = 1

# aliens
alienImg = pygame.image.load('Invader.png')
hitbox___ = alienImg.get_rect()
vel___ = 1
hitbox___.x = 530

alien_Img = pygame.image.load('Invader.png')
alien_hitbox = alien_Img.get_rect()
speed___ = 2
alien_hitbox.x = 630

# big asteroid
big_asteroidImg = pygame.image.load('Big_asteroid.png')
hitbox__ = big_asteroidImg.get_rect()
vel__ = 0.5
hitbox__.y = -150

# bullets
bulletImg = pygame.image.load('bullet.png')
bullet_hitbox = bulletImg.get_rect()
speed_ = 2.1
bullet_hitbox.x = -50
bullet_hitbox.y = 0

bullet_Img = pygame.image.load('bullet.png')
bullet__hitbox = bullet_Img.get_rect()
speed__ = 2.1
bullet__hitbox.x = -50
bullet__hitbox.y = 0

player_bullet = pygame.image.load('laser.png')
pbullet_hitbox = player_bullet.get_rect()
pbullet_speed = 2.5
pbullet_hitbox.x = 2000

# point
pointImg = pygame.image.load('asteroid.png')
point = pointImg.get_rect()
point_speed = 4
point.y

# gameloop
running = True
while running:

    # RGB
    screen.fill((149, 27, 218))
    # bagground
    screen.blit(bg, (0,0))

    # define quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard input
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_RIGHT]:
        hitbox.x += vel
    if userInput[pygame.K_LEFT]:
        hitbox.x -= vel
    if userInput[pygame.K_UP]:
        hitbox.y -= vel
    if userInput[pygame.K_DOWN]:
        hitbox.y += vel
    if userInput[pygame.K_d]:
        hitbox.x += vel
    if userInput[pygame.K_a]:
        hitbox.x -= vel
    if userInput[pygame.K_w]:
        hitbox.y -= vel
    if userInput[pygame.K_s]:
        hitbox.y += vel
    if userInput[pygame.K_SPACE] and pbullet_hitbox.x == 2000:
        pbullet_hitbox.x = hitbox.x
        pbullet_hitbox.y = hitbox.y
        laser_fx.play()

    # movement
    if hitbox_.x >= 0:
        hitbox_.x -= vel_
    
    if hitbox__.x >= 0:
        hitbox__.x -= vel__

    if score == 10:
        hitbox__.y = 112

    if hitbox___.y <= 600:
        hitbox___.y += vel___

    if alien_hitbox.y <= 600:
        alien_hitbox.y += vel___

    if score > 9:
        vel = 2

    if bullet_hitbox.x > -70:
        bullet_hitbox.x -= speed_

    if bullet__hitbox.x > -70:
        bullet__hitbox.x -= speed__
    
    if pbullet_hitbox.x < 2000:
        pbullet_hitbox.x += pbullet_speed

    # point clock
    if point.x > 0:
        point.x -= point_speed
    
    if point.x <= 5:
        point.x = 736
        score += 1

    # player bounderies
    if hitbox.y <= 0:
        hitbox.y = 0
    elif hitbox.y >= 536:
        hitbox.y = 536
        
    if hitbox.x <= 0:
        hitbox.x = 0
    elif hitbox.x >= 736:
        hitbox.x = 736

    # if the asteroid hits the left side, tp back
    if hitbox_.x <= 1:
        hitbox_.x = 736
        hitbox_.y = random.randint(1,536)
        vel_ += 0.03
    
    if score > 9 and hitbox__.x <= 0:
        hitbox__.x = 672
        hitbox__.y = random.randint(1,472)
        vel__ += 0.09
    
    if bullet_hitbox.x < 0 and score > 20 and hitbox___.y == 268:
        bullet_hitbox.y = 268
        bullet_hitbox.x = 530
        laser_fx.play()
    
    if bullet_hitbox.x < 0 and score > 20 and hitbox___.y == 532:
        bullet_hitbox.y = 532
        bullet_hitbox.x = 530
        laser_fx.play()
    
    if bullet_hitbox.x < 0 and score > 20 and hitbox___.y == 30:
        bullet_hitbox.y = 30
        bullet_hitbox.x = 530
        laser_fx.play()

    if bullet__hitbox.x < 0 and score > 35 and alien_hitbox.y == 400:
        bullet__hitbox.y = 400
        bullet__hitbox.x = 630
        laser_fx.play()
    
    if bullet__hitbox.x < 0 and score > 35 and alien_hitbox.y == 132:
        bullet__hitbox.y = 132
        bullet__hitbox.x = 630
        laser_fx.play()

    if hitbox___.y >= 572:
        vel___ *= -1
    
    if hitbox___.y <= 0:
        vel___ *= -1
    
    if alien_hitbox.y >= 572:
        speed___ *= -1
    
    if alien_hitbox.y <= 0:
        speed___ *= -1

    # define if the hitboxes hit eachother
    if hitbox.colliderect(hitbox_):
        time.sleep(3)
        pygame.quit()

    if hitbox.colliderect(hitbox__):
        time.sleep(3)
        pygame.quit()

    if hitbox.colliderect(hitbox___):
        time.sleep(3)
        pygame.quit()

    if hitbox.colliderect(bullet_hitbox):
        time.sleep(3)
        pygame.quit()

    if hitbox.colliderect(bullet__hitbox):
        time.sleep(3)
        pygame.quit()
    
    if pbullet_hitbox.colliderect(hitbox_):
        hitbox_.y = -150
        ex.play()
    
    if pbullet_hitbox.colliderect(hitbox__):
        hitbox__.y = -150
        ex.play()

    screen.blit(playerImg, hitbox)
    screen.blit(asteroid_smallImg, hitbox_)
    screen.blit(big_asteroidImg, hitbox__)
    screen.blit(bulletImg, bullet_hitbox)
    screen.blit(bullet_Img, bullet__hitbox)
    screen.blit(player_bullet, pbullet_hitbox)
        
    if score >= 20:
        screen.blit(alienImg, hitbox___)

    if score >= 35:
        screen.blit(alien_Img, alien_hitbox)

    # update the window
    show_score()
    show_score()
    pygame.time.delay(3)
    pygame.display.update()    

