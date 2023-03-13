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

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 창 X버튼이 눌렸는가?
            running = False # running False 로 만들어서 반복문 탈출

    # screen.fill((255, 0, 255)) # 이런식으로 RGB 값을 넣어 그릴수도 잇음
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update()

# 게임 종료
pygame.quit()