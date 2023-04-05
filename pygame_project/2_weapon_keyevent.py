import pygame
import os

# 1. 기본 초기화 (무조건적으로 필요)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('NADO PANG!')

# FPS 설정
clock = pygame.time.Clock()
# 1-END. 기본 초기화 (무조건적으로 필요)

# 2. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, 'img') # img 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해서 사용함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 ㄱㄴ
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 2-END. 폰트 정의 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)

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
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3-END. 이벤트 처리 (키보드, 마우스 등등)

    # 4. 게임 캐릭터 위치 정의

    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # x = 100, y = 200 -> y = 180, 160, 140..
    # x = 500, y = 200 -> y = 180, 160, 140..
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 4-END. 게임 캐릭터 위치 정의

    # 5. 충돌 처리

    # 5-END. 충돌 처리

    # 6. 화면에 그리기

    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))



    # 6-END. 화면에 그리기

    pygame.display.update()

# 잠시 대기
# pygame.time.delay(2000)

# 게임 종료
pygame.quit()