import pygame
import random

from doc import screen
from doc.sprite import Sprite

#########################################################################
pygame.init()  #초기화

# 화면 설정
SCREEN_WIDTH    = 480
SCREEN_HEIGHT   = 640
SCREEN_SIZE     = (SCREEN_WIDTH, SCREEN_HEIGHT)
GAME_TITLE      = "Quiz"
game_screen     = screen.create_screen(pygame, GAME_TITLE, SCREEN_SIZE)

# FPS
SCREEN_FRAME    = 30
clock = pygame.time.Clock()
#########################################################################

# 사용자 게임 초기화 ( 배경, 게임이미지, 좌표, 폰트, 속도 )
# 1. 배경 만들기
BACKGROUND_IMAGE = './resource/background.jpg'
background = screen.create_backgound(pygame, BACKGROUND_IMAGE)

# 2. 캐릭터 만들기
CHARACTER_SPEED = 20
CHARACTER_IMAGE = './resource/character.png'
character = Sprite(SCREEN_SIZE, CHARACTER_SPEED)
character.create_sprite(pygame, CHARACTER_IMAGE)
character.set_pos( ( SCREEN_SIZE[0]/2 ) - ( character.get_width/2  ),  SCREEN_SIZE[1] - character.get_height  )

# 3. 적 만들기
ENEMY_SPEED     = 2
ENEMY_IMAGE = './resource/enomy.png'
enemy = Sprite(SCREEN_SIZE, ENEMY_SPEED)
enemy.create_sprite(pygame, ENEMY_IMAGE)
enemy.set_pos( random.randint(0, SCREEN_WIDTH - enemy.get_width ),  0 )

running = True
while running:
    dt = clock.tick(SCREEN_FRAME)

    # 2. 이벤트 처리 ( 키보드 , 마우스 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.move_X( -CHARACTER_SPEED )
            elif event.key == pygame.K_RIGHT:
                character.move_X( CHARACTER_SPEED )

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         pass
        #         #character.set_pos(0, SCREEN_SIZE[1] - character.get_sprite_height )

    enemy.move_Y( ENEMY_SPEED )

    # 4. 충돌 처리

    # 5. 화면에 그리기
    game_screen.blit( background, (0, 0) ) # 5-1. 배경 그리기
    game_screen.blit(character.get_sprite, (character.get_spriteSize()))  # 캐릭터 그리기
    game_screen.blit(enemy.get_sprite, (enemy.get_spriteSize()))  # 캐릭터 그리기

    pygame.display.update()
pygame.quit()