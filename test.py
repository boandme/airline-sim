import pygame
pygame.init()
w = pygame.display.set_mode([500,500])
r = pygame.Rect(200,200,200,200)
running = True
while running:
   w.fill((0,0,0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         x,y = pygame.mouse.get_pos()
         if r.collidepoint(x,y):
            print("hi")
   pygame.draw.rect(w, (255,255,255),r)
   pygame.display.flip()
