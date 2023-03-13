import pygame
import random

# 1. 기본 초기화 (무조건적으로 필요)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('DODGE THE METEOR')

# FPS 설정
clock = pygame.time.Clock()
# 1-END. 기본 초기화 (무조건적으로 필요)

# 2. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)
# 배경 만들기
background = pygame.image.load(r'img\quiz_background.png')

# 캐릭터 만들기
character_sprite = [pygame.image.load("img/quiz_character1.png"), pygame.image.load("img/quiz_character2.png"), pygame.image.load("img/quiz_character_stop.png")]
value = 2
character = character_sprite[value]
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# DDONG
ddong_sprite = [pygame.image.load("img/ddong0.png"), pygame.image.load("img/ddong1.png")]
ddong_value = 0
ddong = ddong_sprite[ddong_value]
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 0.8

# 2-END. 폰트 정의 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)

# 이동 위치
to_x = 0
character_speed = 0.6

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # 화면 초당 프레임 수

    # 3. 이벤트 처리 (키보드, 마우스 등등)

    for event in pygame.event.get(): # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 창 X버튼이 눌렸는가?
            running = False # running False 로 만들어서 반복문 탈출

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
                value = 0

            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                value = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                value = 2

    # 3-END. 이벤트 처리 (키보드, 마우스 등등)

    # 4. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed * dt

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)


    # 4-END. 게임 캐릭터 위치 정의

    # 5. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print('충돌!')
        running = False

    # 5-END. 충돌 처리

    # 6. 화면에 그리기


    # value += 0.05

    if value >= len(character_sprite):
        value = 0

    ddong_value += 0.05

    if ddong_value >= len(ddong_sprite):
        ddong_value = 0

    character = character_sprite[int(value)]
    ddong = ddong_sprite[int(ddong_value)]

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    # 6-END. 화면에 그리기

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000)

# 게임 종료
pygame.quit()