import pygame, random, math

pygame.init()

class Particle:
    #_ _init_ _#
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.mass = random.randint(3,10)
        self.dx = random.uniform(-0.25, 0.25)
        self.dy = random.uniform(-0.25, 0.25)
        self.color = (self.mass*25, self.mass*25, self.mass*25)
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 2)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        if self.x > screenX - self.size:
            self.x = 2*(screenX - self.size) - self.x
            self.dx = -1*self.dx #0-self.dx - self.dx 

        if self.x < self.size:
            self.x = 2*self.size - self.x
            self.dx = -self.dx

        if self.y > screenY - self.size:
            self.y = 2*(screenY - self.size) - self.y
            self.dy = -1*self.dy #0-self.dx - self.dx 

        if self.y < self.size:
            self.y = 2*self.size - self.y
            self.dy = -self.dy

def collide(p1,p2):
    distX = p1.x - p2.x 
    distY = p1.y - p2.y
    dist = math.hypot(distX, distY)

    if dist < p1.size + p2.size:
        p1.dx, p2.dx = p2.dx, p1.dx
        p2.dy, p1.dy = p1.dy, p2.dy



particle1 = Particle(300,300,10)
particles = [] # empty list for the particles :3
running = True
screenX = 1600
screenY = 900
screen = pygame.display.set_mode((screenX, screenY))
screencolor = ((64,118,255))
for i in range(10):
    size = random.randint(5,20)
    x = random.randint(size, screenX-size)
    y = random.randint(size, screenY-size)
    p = Particle(x,y,size)
    particles.append(p)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    screen.fill((0,0,0))

    for i,p in enumerate(particles):
        p.move()
        p.bounce()
        for part in particles[i+1:]: ### sillyness intensifies
            collide(p, part)
        p.draw()


 
    pygame.display.flip()
