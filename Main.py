import pygame
from sys import exit
import math

pygame.display.set_caption("Mario Wannabe")
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
test_font = pygame.font.Font('settings/font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('settings/graphics/Sky.png').convert()

ground_surface = pygame.image.load('settings/graphics/ground.png').convert()

score_surf = test_font.render('Mario Wannabe', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('settings/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load('settings/graphics/Player/player_stand.png').convert_alpha()
player_walk_1_surf = pygame.image.load('settings/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2_surf = pygame.image.load('settings/graphics/Player/player_walk_2.png').convert_alpha()
current_player_surf = player_surf

fly_surf = pygame.image.load('settings/graphics/Fly/Fly1.png').convert_alpha()

default_horizontal_offset = 80
default_vertical_offset = 300
player_rect = player_surf.get_rect(midbottom=(default_horizontal_offset, default_vertical_offset))

fly_default_y = 100
fly_rect = fly_surf.get_rect(midbottom=(100, fly_default_y))

player_gravity = 0

game_name = test_font.render('Thank you for playing , Mario Wannabe',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,130))

game_message = test_font.render('Press space to restart',False,(111,196,169))
game_message_rect= game_message.get_rect(center = (400,320))

score = 0
horizontal_offset = default_horizontal_offset
vertical_offset = default_vertical_offset
horizontal_speed = 5

frame_count = 0

key_states = {'A': False, 'D': False}

"""def update_player_rect(index, horizontal_offset, vertical_offset):
    if index == 1:
        _player_surf = player_walk_1_surf
    elif index == 2:
        _player_surf = player_walk_2_surf
    else:
        _player_surf = player_surf
    return _player_surf.get_rect(midbottom = (horizontal_offset,vertical_offset))"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    key_states['A'] = True
                if event.key == pygame.K_d:
                    key_states['D'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    key_states['A'] = False
                if event.key == pygame.K_d:
                    key_states['D'] = False

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score_surf = test_font.render('Mario Wannabe', False, (64, 64, 64))
                score = 0
                horizontal_offset = default_horizontal_offset
                snail_rect.left = 800

    if key_states['A']:
        horizontal_offset -= horizontal_speed
    if key_states['D']:
        horizontal_offset += horizontal_speed
    if key_states['A'] or key_states['D']:
        if frame_count // 5 % 2 == 0:
            current_player_surf = player_walk_1_surf
        else:
            current_player_surf = player_walk_2_surf
    else:
        current_player_surf = player_surf

    #    player_rect = update_player_rect(1, horizontal_offset, vertical_offset)
    # else:
    #    player_rect = update_player_rect(0, horizontal_offset, vertical_offset)"""

    # blit=block transfer

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        screen.blit(score_surf, score_rect)  # ---
        screen.blit(snail_surf, snail_rect)
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
            score += 1
            score_surf = test_font.render(str(score), False, (64, 64, 64))

        fly_rect.x -= 6
        fly_rect.y = fly_default_y + 50 * math.sin(frame_count / 5)
        if fly_rect.right <= 0:
            fly_rect.left = 800
            # score += 1
            # score_surf = test_font.render(str(score),False,(64,64,64))

        player_gravity += 1
        player_rect.y += player_gravity
        # vertical_offset += player_gravity

        player_rect.x = horizontal_offset
        # player_rect.y = vertical_offset
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(current_player_surf, player_rect)
        screen.blit(fly_surf, fly_rect)

        # collision
        if fly_rect.colliderect(player_rect):
            score += 10
            score_surf = test_font.render(str(score), False, (64, 64, 64))
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_surf, player_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message,game_message_rect)

    pygame.display.update()
    frame_count += 1
    clock.tick(60)
