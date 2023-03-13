import pygame

# 1. 기본 초기화 (무조건적으로 필요)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('PYGAME BASIC')

# FPS 설정
clock = pygame.time.Clock()
# 1-END. 기본 초기화 (무조건적으로 필요)

# 2. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)


# 2-END. 폰트 정의 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등등)

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # 화면 초당 프레임 수

    # 3. 이벤트 처리 (키보드, 마우스 등등)

    for event in pygame.event.get(): # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 창 X버튼이 눌렸는가?
            running = False # running False 로 만들어서 반복문 탈출

    # 3-END. 이벤트 처리 (키보드, 마우스 등등)

    # 4. 게임 캐릭터 위치 정의

    # 4-END. 게임 캐릭터 위치 정의

    # 5. 충돌 처리

    # 5-END. 충돌 처리

    # 6. 화면에 그리기

    # 6-END. 화면에 그리기

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000)

# 게임 종료
pygame.quit()