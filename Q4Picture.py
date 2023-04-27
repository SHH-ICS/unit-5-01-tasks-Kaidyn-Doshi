import pygame

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

colors = {
    "blade": (70, 70, 70), # Dark gray
    "crossguard": (0, 255, 160), # Light blue
    "grip": (0, 255, 255) # Light gray
}

sword_dims = {
    "blade_length": 80,
    "blade_width": 25,
    "grip_length": 250,
    "grip_width": 20,
    "crossguard_length": 100,
    "crossguard_width": 10,
    "crossguard_height": 20
}

sword_x, sword_y = screen_width // 1.8, screen_height - 50

# Draw sword
blade_points = [(sword_x - sword_dims["blade_width"]//2, sword_y), 
                (sword_x + sword_dims["blade_width"]//2, sword_y),
                (sword_x + sword_dims["blade_width"]//2, sword_y - sword_dims["blade_length"]),
                (sword_x - sword_dims["blade_width"]//2, sword_y - sword_dims["blade_length"])]
pygame.draw.polygon(screen, colors["blade"], blade_points)

crossguard_points = [(sword_x - sword_dims["crossguard_length"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"]),
                     (sword_x + sword_dims["crossguard_length"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"]),
                     (sword_x + sword_dims["crossguard_length"]//2, sword_y - sword_dims["blade_length"]),
                     (sword_x - sword_dims["crossguard_length"]//2, sword_y - sword_dims["blade_length"])]
pygame.draw.polygon(screen, colors["crossguard"], crossguard_points)

grip_points = [(sword_x - sword_dims["grip_width"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"] - sword_dims["grip_length"]),
               (sword_x + sword_dims["grip_width"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"] - sword_dims["grip_length"]),
               (sword_x + sword_dims["grip_width"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"]),
               (sword_x - sword_dims["grip_width"]//2, sword_y - sword_dims["blade_length"] - sword_dims["crossguard_height"])]
pygame.draw.polygon(screen, colors["grip"], grip_points)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
