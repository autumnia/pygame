import pygame

from doc import sprite, screen

#########################################################################
# 기본 초기화
pygame.init()

# 화면 크기 설정
# 화면 설정
SCREEN_WIDTH    = 480
SCREEN_HEIGHT   = 640
SCREEN_SIZE     = (SCREEN_WIDTH, SCREEN_HEIGHT)
GAME_TITLE      = 'My Game'
screen1         = screen.create_screen(pygame, GAME_TITLE, SCREEN_SIZE)

SPRITE_SPEED = 0.6

# FPS
clock = pygame.time.Clock()
#########################################################################


# 백그라운드 처리
background = screen.create_backgound(pygame)

# 스프라이트 불러오기
character = sprite.Sprite(SCREEN_SIZE, SPRITE_SPEED)
character.create_sprite(pygame, './resource/character.png')

character_x_pos = int( SCREEN_SIZE[0] / 2  - character.get_sprite_width / 2 )
character_y_pos = int( SCREEN_SIZE[1] - character.get_sprite_height )
# character_pos = character.get_sprite_pos

# 이동 좌펴
to_x = 0
to_y = 0

# 적 캐릭터
enomy = sprite.Sprite(SCREEN_SIZE, SPRITE_SPEED)
enomy.create_sprite(pygame, './resource/enomy.png')

enemy_x_pos =  int( SCREEN_SIZE[0]  / 2  - enomy.get_sprite_width / 2 )
enemy_y_pos =  int( SCREEN_SIZE[1]  / 2 - enomy.get_sprite_height / 2 )

# 폰트정의
game_font = pygame.font.Font(None, 40)
# 총시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(60)
    # print("fps: " + str( clock.get_fps()) )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character.get_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character.get_speed
            elif event.key == pygame.K_UP:
                to_y -= character.get_speed
            elif event.key == pygame.K_DOWN:
                to_y += character.get_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += int( to_x * dt )
    character_y_pos += int( to_y * dt )

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >  SCREEN_SIZE[0]  - character.get_sprite_width:
        character_x_pos =  SCREEN_SIZE[0]  - character.get_sprite_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >  SCREEN_SIZE[1]  - character.get_sprite_height:
        character_y_pos =  SCREEN_SIZE[1]  - character.get_sprite_height
        
    # 충돌 처리
    character_rect = character.get_rect
    character_rect.left = int(character_x_pos)
    character_rect.top = int(character_y_pos)

    enemy_rect = character.get_rect
    enemy_rect.left = int(enemy_x_pos)
    enemy_rect.top = int(enemy_y_pos)

    # 충돌 체크
    if character_rect.colliderect( enemy_rect ):
        print("충돌했어요")
        running = False

    screen1.blit(background, (0, 0))
    screen1.blit(character.get_sprite, (character_x_pos, character_y_pos))
    screen1.blit(enomy.get_sprite, (enemy_x_pos, enemy_y_pos) )

    # 경과 시간 계산
    elapsed_time =  ( pygame.time.get_ticks() - start_ticks ) / 1000
    timer = game_font.render(  str(int(total_time - elapsed_time)), True, (255,255,255)  )
    screen1.blit(timer, (10,10))

    if int(total_time - elapsed_time) <= 0 :
        print( "시간 종료 ")
        running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()