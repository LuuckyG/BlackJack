import pygame


class Player(object):
    walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'),
                 pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'),
                 pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
                 pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),
                 pygame.image.load('images/R9.png')]
    walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'),
                pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'),
                pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
                pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'),
                pygame.image.load('images/L9.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:  # 27 images
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy(object):
    walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'),
                 pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'),
                 pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'),
                 pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'),
                 pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'),
                 pygame.image.load('images/R11E.png')]
    walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'),
                pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'),
                pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'),
                pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'),
                pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'),
                pygame.image.load('images/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.velocity = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity  # self.velocity is negative in this case
            else:
                self.velocity *= -1
                self.walkCount = 0
