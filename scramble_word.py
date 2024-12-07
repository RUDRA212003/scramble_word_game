import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Scramble Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
FONT_LARGE = pygame.font.Font(None, 64)
FONT_MEDIUM = pygame.font.Font(None, 48)
FONT_SMALL = pygame.font.Font(None, 32)

# List of words
word_list = ["python", "computer", "programming", "developer", "keyboard", "algorithm", "interface", "software"]

# Game variables
current_word = ""
scrambled_word = ""
score = 0
input_text = ""
rounds = 5


def scramble_word(word):
    """Scrambles the letters of a word."""
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)


def get_new_word():
    """Generates a new word and scrambles it."""
    global current_word, scrambled_word
    current_word = random.choice(word_list)
    scrambled_word = scramble_word(current_word)


# Initial word
get_new_word()

# Game loop
running = True
clock = pygame.time.Clock()
round_counter = 0

while running:
    screen.fill(WHITE)

    # Display scrambled word
    scrambled_text = FONT_LARGE.render(f"Scrambled Word: {scrambled_word}", True, BLUE)
    screen.blit(scrambled_text, (50, 50))

    # Display input text
    input_display = FONT_MEDIUM.render(f"Your Guess: {input_text}", True, BLACK)
    screen.blit(input_display, (50, 150))

    # Display score
    score_display = FONT_SMALL.render(f"Score: {score}", True, GREEN)
    screen.blit(score_display, (650, 10))

    # Display rounds left
    round_display = FONT_SMALL.render(f"Round: {round_counter + 1}/{rounds}", True, GREEN)
    screen.blit(round_display, (650, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Submit answer
                if input_text.lower() == current_word:
                    score += 10
                else:
                    score -= 5
                input_text = ""
                round_counter += 1
                if round_counter < rounds:
                    get_new_word()
                else:
                    running = False  # End the game
            elif event.key == pygame.K_BACKSPACE:  # Remove last character
                input_text = input_text[:-1]
            else:
                input_text += event.unicode  # Add new character to input

    # End game if rounds are over
    if round_counter == rounds:
        screen.fill(WHITE)
        end_text = FONT_LARGE.render(f"Game Over!", True, RED)
        final_score_text = FONT_MEDIUM.render(f"Final Score: {score}", True, BLACK)
        screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 3))
        screen.blit(final_score_text, (WIDTH // 2 - 150, HEIGHT // 3 + 80))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
