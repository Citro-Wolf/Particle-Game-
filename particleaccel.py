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
        pygame.draw.circle(screen, part.color, (part.x, part.y), part.size, 2)
    def move(self):
        self.x += self.dx
        self.y += self.dy
   
particle1 = Particle(300,300,10)
particles = [] ## ik its long :3 ##
running = True
screen = pygame.display.set_mode((1280,720))
for i in range(50):
    size = random.randint(5,20)
    x = random.randint(size, 600-size)
    y = random.randint(size, 600-size)
    p = Particle(x,y,size)
    particles.append(p)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    screen.fill((0,0,0))

    for part in particles:
        part.move()
        part.draw()
    pygame.display.flip()
