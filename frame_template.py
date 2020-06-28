import pygame

from doc import screen

#########################################################################
pygame.init()  #초기화

# 화면 설정
SCREEN_WIDTH    = 480
SCREEN_HEIGHT   = 640
SCREEN_SIZE     = (SCREEN_WIDTH, SCREEN_HEIGHT)
GAME_TITLE      = 'My Game'
screen1         = screen.create_screen(pygame, GAME_TITLE, SCREEN_SIZE)

# FPS
clock = pygame.time.Clock()
#########################################################################

# 1. 사용자 게임 초기화 ( 배경, 게임이미지, 좌표, 폰트, 속도 )
SCREEN_FRAME = 30

running = True
while running:
    dt = clock.tick(SCREEN_FRAME)

    # 2. 이벤트 처리 ( 키보드 , 마우스 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()