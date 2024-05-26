import pygame
import sys
import random
from drum import Drum
from note import Note

# INITIALIZATION
pygame.init()

drum_path = 'assets/drum.png'
note1_path = 'assets/note1.png'
note2_path = 'assets/note2.png'
background_path = 'assets/background.png'

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Taiko no Tatsujin')

drum_image = pygame.image.load(drum_path)
note1_image = pygame.image.load(note1_path)
note2_image = pygame.image.load(note2_path)
background_image = pygame.image.load(background_path)

# We got them SPRITE groups.
drums = pygame.sprite.Group()
notes = pygame.sprite.Group()

drum_width = drum_image.get_width()
drum_height = drum_image.get_height()
drum_x = 0  # Move the drum to the most left
drum_y = SCREEN_HEIGHT - drum_height - 50

drum = Drum(drum_x, drum_y, drum_image)
drums.add(drum)

score = 0
font = pygame.font.Font(None, 74)
message_font = pygame.font.Font(None, 50)
message = ""
message_timer = 0
message_duration = 1000
last_action_time = 0
action_interval = 2000

# Run the game :)
clock = pygame.time.Clock()
running = True

while running:
    current_time = pygame.time.get_ticks()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # If we press f.
            if event.key == pygame.K_f:
                last_action_time = current_time

                # Decide if hit or miss.
                hits = pygame.sprite.spritecollide(drum, notes, False)
                hit_detected = False
                for hit in hits:
                    if hit.note_type == 'note1':
                        hit.kill()
                        score += 10
                        hit_detected = True
                        message = "Hit!"
                        message_timer = current_time
                        print("Hit note1!")
                if not hit_detected:
                    message = "Miss!"
                    message_timer = current_time
            
            # If we press j.
            elif event.key == pygame.K_j:
                last_action_time = current_time

                # Decide if hit or miss.
                hits = pygame.sprite.spritecollide(drum, notes, False)
                hit_detected = False
                for hit in hits:
                    if hit.note_type == 'note2':
                        hit.kill()  # Remove the note
                        score += 10
                        hit_detected = True
                        message = "Hit!"
                        message_timer = current_time
                        print("Hit note2!")
                if not hit_detected:
                    message = "Miss!"
                    message_timer = current_time

    # Add notes at intervals (simple example)
    if current_time % action_interval < 20:  # Adjust timing for real gameplay
        # Check if there's already a note on the screen
        note1_exists = any(note.note_type == 'note1' for note in notes)
        note2_exists = any(note.note_type == 'note2' for note in notes)

        if not note1_exists and not note2_exists:
            note_type = random.choice(['note1', 'note2'])
            if note_type == 'note1':
                note = Note(SCREEN_WIDTH, SCREEN_HEIGHT - 150, 5, note1_image, 'note1')
            else:
                note = Note(SCREEN_WIDTH, SCREEN_HEIGHT - 150, 5, note2_image, 'note2')
            notes.add(note)

    # Update notes
    notes.update()

    # Check for notes that have passed out of the screen
    for note in notes:
        if note.rect.right < 0:
            message = "Miss!"
            print("Miss")
            message_timer = current_time
            print('i killed it here.')
            note.kill()

    # Draw everything
    screen.blit(background_image, (0, 0))  # Clear screen with background
    drums.draw(screen)
    notes.draw(screen)

    # Render the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Do we let the message stay on there? Depends on how long has elapsed from the message generation time.
    if current_time - message_timer < message_duration:
        message_text = message_font.render(message, True, WHITE)
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2 - message_text.get_height() // 2))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
