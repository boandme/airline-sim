
import pygame
import pygame.font
import random
import time


pygame.init()
w = pygame.display.set_mode((750,750))



white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg = (135, 206, 235)
w.fill(white)
black = (0,0,0)
title_font = pygame.font.SysFont("Arial", 50)
font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 25)

#### Aircrafts Dictionary ####
aircrafts = {
  "Dc 3": {
    "cost": 1000,
    "passengers": 30,
    "per_passenger": 80,
    "comfort": 25,
    "safety": 40,
    "speed": 10
    
  },
  "Airbus A318": {
    "cost": 15000,
    "passengers": 122,
    "per_passenger": 110,
    "comfort": 45,
    "safety": 60,
    "speed": 7
  },
  "Airbus A319": {
    "cost": 35000,
    "passengers": 145,
    "per_passenger": 118,
    "comfort": 50,
    "safety": 60,
    "speed": 7
    
  },
  "Airbus A350": {
    "cost": 100000,
    "passengers": 325,
    "per_passenger": 115,
    "comfort": 50,
    "safety": 40,
    "speed": 5
  },
  "Airbus A340": {
    "cost": 175000,
    "passengers": 372,
    "per_passenger": 126,
    "comfort": 55, 
    "safety": 45,
    "speed": 5
  },
  "Boeing 777": {
    "cost": 300000,
    "passengers": 500,
    "per_passenger": 146,
    "comfort": 75,
    "safety": 70,
    "speed": 3
  },
  "Boeing 747": {
    "cost": 500000,
    "passengers": 537,
    "per_passenger": 175,
    "comfort": 75,
    "safety": 60, 
    "speed": 4
  },
  "Airbus A380": {
    "cost": 1000000,
    "passengers": 705,
    "per_passenger": 180,
    "comfort": 70,
    "safety": 60,
    "speed": 2.5
    
  },
  "Concorde": {
    "cost": 90000,
    "passengers":75,
    "per_passenger": 60,
    "comfort": 40,
    "safety": 20,
    "speed": 0.5
  }


}

 



my_aircrafts = ["Dc 3", "diddly doe"]

##### Destinations #####
destinations = ["Detroit", "Chicago", "Minneapolis", "Atlanta", "Miami", "New Orleans", "Washington DC", "New York City", "Denver", "Salt Lake City", "Seattle", "San Francisco", "Los Angeles", "San Diego", "Dallas", "Houston", "Kansas City", "Cincinnati", "Boston", "Portland", "Philadelphia"]
west = ["Seattle", "Portland", "San Francisco", "Los Angeles", "San Diego", "Salt Lake City"]
mid = ["Detroit", "Chicago", "Denver", "Dallas", "Houston", "Kansas City", "Cincinnati", "Minneapolis"]
east = ["Atlanta", "Miami", "New Orleans", "Washington DC", "New York City", "Boston", "Philadelphia"]
landings = {
  "rough": 20,
  "terrible": 10,
  "smooth": 50, 
  "pleasant": 40,
  "decent": 35,
  "ok": 30,
  "amazing": 60,
  "so bad it damaged the aircraft": -50

}
money = 500


def flyplane():
  global money
  global aircrafts
  global my_aircrafts
  showing = True
  while showing:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
    w.fill(bg)
    
    p1 = random.choice(destinations)
    destinations.remove(p1)
    p2 = random.choice(destinations)
    destinations.append(p1)
    hours = random.randint(1,12)
    minutes = random.randint(1,59)
    if minutes < 10:
      minutes = "0" + str(minutes)
    time_of_day = random.choice(["AM", "PM"])
    aircraft_opt = title_font.render("Pick your Aircraft", True, white)
    w.blit(aircraft_opt, (225,50))
    for i in range(len(my_aircrafts)):
      a = font.render(my_aircrafts[i], True, white)
      w.blit(a,(200, 150 + i * 75) )
      r = pygame.Rect(150, 140 + i * 75, 400, 60 )
      pygame.draw.rect(w,red,r, 5)


    for event in pygame.event.get():
      x,y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        print("ggs")
        print(i)
        print(str(x) + str(y))
        for i in range(len(my_aircrafts)):
          if (x > 150 and x < 550) and (y> 140+ i*75 and y < 200 + i*75):
            showing = False
            print("hiii")
            aircraft = my_aircrafts[i]
            print(aircraft)
      if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

  flight_num = random.randint(1000,9999)
  boarding = True
  while boarding:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          boarding = False
    w.fill(bg)
    details = title_font.render("Flight Details", True, white)
    airline = font.render("United", True, white)
    num = font.render(f"Flight Number: {flight_num} ", True, white)
    path = font.render(f"{p1} ---> {p2}", True, white)
    time = font.render(f"{hours}:{minutes} {time_of_day}", True, white)
    directions = font.render("Press Enter to take off", True, white)
    w.blit(details, (175,50))
    w.blit(airline, (100,150))
    w.blit(num, (100,250))
    w.blit(path, (100,350))
    w.blit(time, (100,450))
    w.blit(directions, (175, 650))
    pygame.draw.line(w, (0,0,0), (0,600), (750,600), 10)
    pygame.display.flip()

  flying = True
  while flying:
    w.fill(bg)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    plane = pygame.image.load("airliner.png")
    pygame.draw.line(w,black, (100, 150), (650, 150), 3)
    pygame.draw.circle(w,black,(650,150), 5)
    pygame.draw.circle(w,black, (100,150), 5)
    start = small_font.render(p1, True, white)
    end = small_font.render(p2, True, white)
    w.blit(end, (625,75))
    w.blit(start, (75, 75))
    plane = pygame.transform.scale(plane, (90,67.5))
    i = 75
    distance= 550
    while i <= 625:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
      w.fill(bg)
      pygame.draw.line(w,black, (100, 150), (650, 150), 3)
      pygame.draw.circle(w,black,(650,150), 5)
      pygame.draw.circle(w,black, (100,150), 5)
      start = small_font.render(p1, True, white)
      end = small_font.render(p2, True, white)
      w.blit(end, (625,75))
      w.blit(start, (75, 75))
      w.blit(plane, (i, 118))
      i += 1
      print(int(1000 * (aircrafts[aircraft]['speed']/distance)))
      pygame.time.wait(int(1000 * (aircrafts[aircraft]['speed']/distance)))
      pygame.display.flip()
    pygame.display.flip()

    if i >= 625:
      summary = True
      #while summary:


    




     

      
          
    
    

  
  





running = True
while running:
  w.fill(bg)
  title_font = pygame.font.SysFont("Arial", 50)
  font = pygame.font.SysFont("Arial", 40)
  title = title_font.render("Airline Simulator", True, white)
  w.blit(title,(225, 50))
  opt1 = font.render("Fly Plane", True, white)
  opt2 = font.render("coming soon", True, white)
  opt3 = font.render("coming soon", True, white)
  opt4 = font.render("coming soon", True, white)
  opt5 = font.render("coming soon", True, white)
  w.blit(opt1, (200,200))
  w.blit(opt2, (200, 300))
  w.blit(opt3, (200,400))
  w.blit(opt4, (200,500))
  w.blit(opt5, (200, 600))
  r1 = pygame.Rect(150, 175, 400, 85)
  r2 = pygame.Rect(150, 275, 400, 85)
  r3 = pygame.Rect(150, 375, 400, 85)
  r4= pygame.Rect(150, 475, 400, 85)
  r5 = pygame.Rect(150, 575, 400, 85)
  pygame.draw.rect(w,red,r1, 5)
  pygame.draw.rect(w,red,r2, 5)
  pygame.draw.rect(w,red,r3, 5)
  pygame.draw.rect(w,red,r4, 5)
  pygame.draw.rect(w,red,r5, 5)
 
   #### Conditions ####
  x,y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if (x > 150 and x < 650) and (y > 175 and y < 260):
        flyplane()

  pygame.display.update()
   



#### Start of Game ###


#name = input("Enter the name of your airline: ")




