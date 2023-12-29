import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bg = (127,127,127) 
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      if event.type == pygame.QUIT:
         done = True
      font = pygame.font.SysFont("Arial", 36)
   txtsurf = font.render("Hello, World", True, white)
   screen.blit(txtsurf,(500, 500))
   pygame.display.update()
