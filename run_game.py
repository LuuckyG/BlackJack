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

# Load sounds
bulletSound = pygame.mixer.Sound('media/bullet.wav')
hitSound = pygame.mixer.Sound('media/hit.wav')
music = pygame.mixer.music.load('media/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()


def redraw_game_window():
    window.blit(bg, (0, 0))
    text = font.render("Score: " + str(player.score), 1, (0, 0, 0))
    window.blit(text, (360, 10))
    player.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()


# Game 'items'
font = pygame.font.SysFont("comicsans", 30, True)
player = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []
shootLoop = 0

# Main loop
run = True
while run:
    clock.tick(27)
    if goblin.visible:
        if player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[-1] \
                and player.hitbox[1] + player.hitbox[-1] > goblin.hitbox[1]:
            if player.hitbox[0] + player.hitbox[-2] > goblin.hitbox[0] \
                    and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[-2]:
                player.hit(window)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[-1] \
                    and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] \
                        and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[-2]:
                    hitSound.play()
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))
                    player.score += 1

        if screenWidth > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))  # Remove off screen bullets

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2),
                                      radius=6, color=(255, 0, 0), facing=facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and player.x > player.velocity:
        player.x -= player.velocity
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.velocity:
        player.x += player.velocity
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not player.isJump:
        if keys[pygame.K_UP]:
            player.isJump = True
            player.left = False
            player.right = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redraw_game_window()

pygame.quit()
