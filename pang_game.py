import pygame
import os
import random

#########################################################################
pygame.init()  #초기화

# 화면 설정
SCREEN_WIDTH    = 640
SCREEN_HEIGHT   = 480
SCREEN_SIZE     = (SCREEN_WIDTH, SCREEN_HEIGHT)
GAME_TITLE      = "Pang Game"

CURRENT_PATH    = os.path.dirname(__file__)
IMAGE_PATH      = os.path.join(CURRENT_PATH, "images")
# print( IMAGE_PATH )

# FPS
SCREEN_FRAME    = 30
clock = pygame.time.Clock()
#########################################################################

# 사용자 게임 초기화 ( 배경, 게임이미지, 좌표, 폰트, 속도 )
# 1. 게임 타이틀 설정
pygame.display.set_caption( GAME_TITLE )

# 2. 배경 만들기
screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load( os.path.join(IMAGE_PATH, "background.png") )

# 3. 스테이지 만들기
stage = pygame.image.load( os.path.join(IMAGE_PATH, "stage.png") )
stage_rect      = stage.get_rect()
stage_width     = stage_rect.size[0]
stage_height    = stage_rect.size[1]

# 4. 캐릭터 만들기
CHARACTER_SPEED  = 5
character        = pygame.image.load( os.path.join(IMAGE_PATH, "character1.png") )
character_rect   = character.get_rect()
character_width  = character_rect.size[0]
character_height = character_rect.size[1]
character_xpos   = int( ( SCREEN_WIDTH / 2 ) - ( character_width / 2 ) )
character_ypos   = int( SCREEN_HEIGHT - stage_height - character_height  )
    # 캐릭터 이동
character_to_x = 0
character_to_y = 0

# 5. 무기 만들기
WEAPON_SPEED    = 10
weapon          = pygame.image.load( os.path.join(IMAGE_PATH, "weapon1.png") )
weapon_rect     = weapon.get_rect()
weapon_width    = weapon_rect.size[0]
weapon_height   = weapon_rect.size[1]
weapon_xpos     = 0
weapon_ypos     = 0
    # 여러개의 무기
weapons = []
    # 사라질 무기 정보 저장 변수
weapon_to_remove = -1

# 6. 공만들기
ball_images = [
    pygame.image.load( os.path.join(IMAGE_PATH, "ball1.png") ),
    pygame.image.load( os.path.join(IMAGE_PATH, "ball2.png") ),
    pygame.image.load( os.path.join(IMAGE_PATH, "ball3.png") ),
    pygame.image.load( os.path.join(IMAGE_PATH, "ball4.png") ),
]

    # 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

balls = []
balls.append({
    "pos_x": 50, "pos_y": 50, "img_idx": 0, "to_x": 3, "to_y": -6, "init_speed_y": ball_speed_y[0]
})

# 사라질 공 정보 저장 변수
ball_to_remove = -1

# font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()

# 게임종료 메시지  Timeout,  Mission Complete, Game Over
game_result = "Game Over"


##################################################################################################
running = True
while running:
    dt = clock.tick(SCREEN_FRAME)

    # # 1. 이벤트 처리 ( 키보드 , 마우스 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= CHARACTER_SPEED
            elif event.key == pygame.K_RIGHT:
                character_to_x += CHARACTER_SPEED
            elif event.key == pygame.K_SPACE:
                weapon_xpos = int( character_xpos + ( character_width / 2 ) - ( weapon_width / 2 ) )
                weapon_ypos = int( character_ypos - stage_height )
                weapons.append( [weapon_xpos, weapon_ypos] )

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 2. 게임 캐릭터 위치 정의
    character_xpos += character_to_x
    if ( character_xpos < 0 ):
        character_xpos = 0
    elif  character_xpos > ( SCREEN_WIDTH - character_width ):
        character_xpos = SCREEN_WIDTH - character_width

    #  3. 무기 사용
    # weapons = [ [w[0], w[1]-WEAPON_SPEED] for w in weapons ]
    for w in weapons:
        weapons = [ [w[0], w[1] - WEAPON_SPEED] ]

    # weapons = [ [w[0], w[1]-WEAPON_SPEED] for w in weapons if w[1] > 0 ]
    for w in weapons:
        if w[1] > 0:
            weapons = [ [w[0], w[1]-WEAPON_SPEED] ]
            
     # 4. 공 사용
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_width = ball_rect.size[0]
        ball_height = ball_rect.size[1]

        # 가로벽에 닿았을 경우 공의 위치 변경
        if ball_pos_x <=0 or ball_pos_x > SCREEN_WIDTH - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 스테이지에 튕겼을 경우
        if ball_pos_y >= SCREEN_HEIGHT - stage_height - ball_height:
           ball_val["to_y"] = ball_val["init_speed_y"]
        else:
           ball_val["to_y"] += 0.5

        ball_val["pos_x"] += int(ball_val["to_x"])
        ball_val["pos_y"] += int(ball_val["to_y"])

    #############################################################################################
    # 충돌 처리
        # 공과 캐릭터 충돌
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top  = character_ypos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        # 볼 위치 업데이트 중요
        ball_rect.left  = int(ball_pos_x)
        ball_rect.top   = int(ball_pos_y)

        # 공과 캐릭터 충돌 처리
        if character_rect.colliderect ( ball_rect ):
            print( "볼과 충돌")
            running = False
            break

        # 공과 무기의 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            # print( weapon_idx, weapon_val )
            weapon_xpos = weapon_val[0]
            weapon_ypos = weapon_val[1]
            # 무기 위치 갱신
            weapon_rect = weapon_rect
            weapon_rect.left = weapon_xpos
            weapon_rect.top = weapon_ypos

            if weapon_rect.colliderect(ball_rect):
                # print(weapon_idx)
                # 공과 무기 사라짐
                ball_to_remove = ball_idx
                weapon_to_remove = weapon_idx

                # 가장 작은 공의 크기가 아니며 다음단계 공으로 나누면 됨
                if ball_img_idx < 3:
                    # 현재 공 위치
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽 공
                    small_ball_pos_x = ball_pos_x + ( ball_width / 2 ) - ( small_ball_width / 2 )
                    small_ball_pos_y = ball_pos_y + ( ball_height / 2 ) - ( small_ball_height / 2 )
                    balls.append({
                        "pos_x": small_ball_pos_x, "pos_y": small_ball_pos_y, "img_idx": ball_img_idx+1, "to_x": -3, "to_y": -6, "init_speed_y": ball_speed_y[ball_img_idx+1]
                    })
                    # 오른쪽 공
                    balls.append({
                        "pos_x": small_ball_pos_x, "pos_y": small_ball_pos_y, "img_idx": ball_img_idx+1, "to_x": 3, "to_y": -6, "init_speed_y": ball_speed_y[ball_img_idx+1]
                    })

                break

    # 충돌된 공과 무기 제거
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공이 없어진 경우 게임 종료
    if len( balls ) == 0:
        game_result = "Mission Complete"
        running = False

    #######################################################################################

    # 5. 화면에 그리기
        # 배경 그리기
    screen.blit( background, (0, 0) )
        #  무기 그리기
    for weapon_xpos, weapon_ypos in weapons:
        screen.blit(weapon, (weapon_xpos, weapon_ypos) )
        # 공 그리기
    for inx, val in enumerate(balls):
        ball_pos_x = int(val["pos_x"])
        ball_pos_y = int(val["pos_y"])
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
        # 스테이지 그리기
    screen.blit( stage, (0, SCREEN_HEIGHT - stage_height) )
        # 캐릭터 그리기
    screen.blit(character, (character_xpos, character_ypos) )

    # 경과 시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks ) / 1000
    timer = game_font.render("Time : {}".format( int(total_time - elapsed_time)), True, (255, 255, 255) )
    screen.blit( timer, (10, 10))

    # 시간 초과
    if total_time - elapsed_time < 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()

#################################################################################################

msg = game_font.render(game_result, True, (255, 255, 0))
msg_center_x = int(SCREEN_WIDTH/2)
msq_senter_y = int(SCREEN_HEIGHT/2)
msg_rect = msg.get_rect( center=(msg_center_x, msq_senter_y) )
screen.blit( msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()