import pygame
from game_characters import Player, Enemy, Projectile

pygame.init()

# Set game window
screenWidth = 500
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

# Load images
bg = pygame.image.load('images/bg.jpg')  # Background
char = pygame.image.load('images/standing.png')

clock = pygame.time.Clock()


def redraw_game_window():
    window.blit(bg, (0, 0))
    man.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()


# Main loop
man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []
run = True
while run:
    clock.tick(27)

    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if screenWidth > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))  # Remove off screen bullets

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2),
                                      radius=6, color=(1, 1, 0), facing=facing))

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redraw_game_window()

pygame.quit()
