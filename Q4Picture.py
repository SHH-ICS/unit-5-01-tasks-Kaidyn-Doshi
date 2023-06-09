import pygame
pygame.init()
screen = pygame.display.set_mode((720, 700))

# Shield
shield_rect = pygame.draw.ellipse(screen, (220, 20, 60), (220, 115, 200, 250))
pygame.draw.ellipse(screen, (70, 70, 70), shield_rect, 5)
symbol_center = (shield_rect.centerx, shield_rect.centery - 8)
pygame.draw.circle(screen, (219, 172, 52), symbol_center, 50)
pygame.draw.circle(screen, (70, 70, 70), symbol_center, 50, 2)
for angle in range(0, 360, 45):
    start_pos = pygame.math.Vector2(symbol_center) + pygame.math.Vector2(0, -40).rotate(angle)
    end_pos = start_pos + pygame.math.Vector2(0, -25).rotate(angle)
    pygame.draw.line(screen, (219, 172, 52), start_pos, end_pos, 10)

for angle_start, angle_end in [(45, 90), (135, 180), (225, 270), (315, 360)]:
    pygame.draw.arc(screen, (219, 172, 52), (symbol_center[0] - 30, symbol_center[1] - 30, 60, 60), angle_start, angle_end, 10)
pygame.draw.circle(screen, (150, 150, 150), symbol_center, 30)
pygame.draw.circle(screen, (50, 50, 50), symbol_center, 50, 2)


# Sword
sword_x = screen.get_width() // 4 + 300
sword_y = screen.get_height() // 2 + 50
pygame.draw.polygon(screen, (70, 70, 70), [(sword_x - 25 // 2, sword_y), 
                                           (sword_x + 25 // 2, sword_y),
                                           (sword_x + 25 // 2, sword_y - 80),
                                           (sword_x - 25 // 2, sword_y - 80)])
pygame.draw.polygon(screen, (0, 255, 160), [(sword_x - 100 // 2, sword_y - 80 - 20),
                                            (sword_x + 100 // 2, sword_y - 80 - 20),
                                            (sword_x + 100 // 2, sword_y - 80),
                                            (sword_x - 100 // 2, sword_y - 80)])
pygame.draw.polygon(screen, (0, 255, 255), [(sword_x - 20 // 2, sword_y - 80 - 20 - 250),
                                            (sword_x + 20 // 2, sword_y - 80 - 20 - 250),
                                            (sword_x + 20 // 2, sword_y - 80 - 20),
                                            (sword_x - 20 // 2, sword_y - 80 - 20)])
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
