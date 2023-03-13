import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('PYGAME BASIC')

# 배경 이미지 불러오기
background = pygame.image.load(r'img\background.png')

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load(r'img\character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가운데
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 두기

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 창 X버튼이 눌렸는가?
            running = False # running False 로 만들어서 반복문 탈출

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 화긴
            if event.key == pygame.K_LEFT:
                to_x -= 2
            elif event.key == pygame.K_RIGHT:
                to_x += 2
            elif event.key == pygame.K_UP:
                to_y -= 2
            elif event.key == pygame.K_DOWN:
                to_y += 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update()

# 게임 종료
pygame.quit()