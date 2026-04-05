import pygame
import random
pygame.init()

screen_width=800
screen_height=600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
colors=[white,black,red,green,blue,yellow]

game_state={
    'score': 0,
    "lives": 3,
    "level": 1,
    "game_over": False,
    'fall_speed': 3
}

basket_w=180
basket_h=175
basket_x=screen_width//2-basket_w//2
basket_y=screen_height-50
basket_speed=8

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Catch the Falling Objects')
clock=pygame.time.Clock()
font=pygame.font.SysFont('Arial', 28)

falling_objects = []
frame_count = 0

def create_object():
    return {
        'x': random.randint(0, screen_width - 20),
        'y': 0,
        "color": random.choice(colors),
        'size': 8
    }

def game_over_screen(screen, score):
    font_big = pygame.font.SysFont('Montserrat', 65)
    font_small = pygame.font.SysFont('Montserrat', 30)

    while True:
        screen.fill(white)
        title=font_big.render("GAME OVER",True,black)
        score=font_small.render(f"Score: {game_state['score']}",True,green)
        restart=font_small.render('Press R to Restart',True,red)
        quit=font_small.render('Press Q to Quit',True,red)

        screen.blit(title, (screen.get_width()//2 - title.get_width()//2, 150))
        screen.blit(score, (screen.get_width()//2 - score.get_width()//2, 250))
        screen.blit(quit, (screen.get_width()//2 - quit.get_width()//2, 400))
        screen.blit(restart, (screen.get_width()//2 - restart.get_width()//2, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "quit"
                if event.key == pygame.K_r:
                    return "restart"

running = True

while running:

    # 🔁 СБРОС ИГРЫ
    game_state = {
        'score': 0,
        "lives": 3,
        "level": 1,
        "game_over": False,
        'fall_speed': 3
    }

    falling_objects.clear()
    basket_x = screen_width // 2 - basket_w // 2
    frame_count = 0

    # 🎮 ИГРА
    while not game_state['game_over']:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_state['game_over'] = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        elif keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        if basket_x < 0:
            basket_x = 0
        if basket_x > screen_width - basket_w:
            basket_x = screen_width - basket_w

        frame_count += 1
        if frame_count % 90 == 0:
            falling_objects.append(create_object())

        for obj in falling_objects[:]:
            obj['y'] += game_state['fall_speed']

            if basket_x < obj['x'] <= basket_w + basket_x and obj['y'] + obj['size'] >= basket_y:
                game_state['score'] += 1
                falling_objects.remove(obj)
                continue

            if obj['y'] > screen_height:
                falling_objects.remove(obj)
                game_state['lives'] -= 1

                if game_state['lives'] == 0:
                    game_state['game_over'] = True

            new_level = game_state['score'] // 5 + 1
            if new_level > game_state['level']:
                game_state['level'] = new_level
                game_state['fall_speed'] += 1

        pygame.draw.rect(screen, black, (basket_x, basket_y, basket_w, basket_h))

        for obj in falling_objects:
            pygame.draw.rect(screen, obj['color'], (obj['x'], obj['y'], obj['size'], obj['size']))

        score_text = font.render(f"Score:{game_state['score']}", True, blue)
        lives_text = font.render(f"Lives:{game_state['lives']}", True, black)

        screen.blit(score_text, (30, 30))
        screen.blit(lives_text, (30, 50))

        pygame.display.flip()
        clock.tick(60)


    result = game_over_screen(screen, game_state['score'])

    if result == "quit":
        running = False


pygame.quit()

