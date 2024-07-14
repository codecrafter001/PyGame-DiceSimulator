import random

# Simulates the rolling of dice
def roll_dice():

    return random.randint(1, 6)

def display_dice(no):
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

while True:
    no = roll_dice()
    display_dice(no)

    x = input("Press 'y' to roll again and 'n' to exit: ")

    if x.lower() != 'y':
        print("Exiting dice simulation.")
        break

    print("\n")
import pygame

pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dice Roller")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Font for displaying text
font = pygame.font.Font(None, 36)

# Function to draw a die on the screen
def draw_die(no, x, y):
    # Draw the die outline
    pygame.draw.rect(screen, white, (x, y, 50, 50), 2)
    
    # Draw the dots based on the number
    if no == 1:
        pygame.draw.circle(screen, white, (x + 25, y + 25), 5)
    elif no == 2:
        pygame.draw.circle(screen, white, (x + 10, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 40), 5)
    elif no == 3:
        pygame.draw.circle(screen, white, (x + 10, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 25, y + 25), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 40), 5)
    elif no == 4:
        pygame.draw.circle(screen, white, (x + 10, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 10, y + 40), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 40), 5)
    elif no == 5:
        pygame.draw.circle(screen, white, (x + 10, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 10, y + 40), 5)
        pygame.draw.circle(screen, white, (x + 25, y + 25), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 40), 5)
    elif no == 6:
        pygame.draw.circle(screen, white, (x + 10, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 10, y + 40), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 10), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 40), 5)
        pygame.draw.circle(screen, white, (x + 10, y + 25), 5)
        pygame.draw.circle(screen, white, (x + 40, y + 25), 5)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Roll the die
    no = roll_dice()

    # Draw the die in the center of the screen
    draw_die(no, screen_width // 2 - 25, screen_height // 2 - 25)

    # Display the result text
    text = font.render(f"You rolled a {no}", True, white)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()