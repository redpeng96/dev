#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import pygame

########################### Initial Configuraiton ###########################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("DROP THE SHEAT!!")

# FPS
clock = pygame.time.Clock()

########################### Initial Configuraiton ###########################


############### Background, Images, Positions, Font and etc. ###############

background = pygame.image.load("./background.png")


character = pygame.image.load("./character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.5

enemy = pygame.image.load("./enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 5


game_font = pygame.font.Font(None, 40)
total_time = 60
start_ticks = pygame.time.get_ticks()

############### Background, Images, Positions, Font and etc. ###############



running = True

while running:
    dt = clock.tick(60)
    


############################## Event Handling ##############################

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
      
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        enemy_speed = random.randint(2, 20)
        
## Collision Handling    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
   
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
        
    if character_rect.colliderect(enemy_rect):
        running = False

## Timer Handling        
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))

    if total_time - elapsed_time <= 0:
        running = False
        
############################## Event Handling ##############################


    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    screen.blit(timer, (440, 10))

    pygame.display.update()
    
pygame.time.delay(2000)
pygame.quit()

