import pygame
import pygame.font
import random
import time
num = 0

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
aircraft_names = ["Dc 3", "Airbus A318", "Airbus A319", "Airbus A350", "Airbus A340", "Boeing 777", "Boeing 747", "Airbus A380"]
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

 



my_aircrafts = ["Dc 3"]

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

##### Upgrades Dictionary ####
upgrade_names = ["In-Flight Drinks Service", "In-Flight Food Service","Google Sponsership","Business class seating","First class seating","Apple Sponorship","Amazon Sponsorship","EntyFish Pilot", "dod"]
upgrades= {
  "In-Flight Drinks Service": 75000,
  "In-Flight Food Service": 250000,
  "Google Sponsership": 350000,
  "Business class seating": 500000,
  "First class seating": 750000,
  "Apple Sponorship": 900000,
  "Amazon Sponsorship": 1000000,
  "EntyFish Pilot": 1200000,
  "dod": 500,
}
money = 50000


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
        for i in range(len(my_aircrafts)):
          if (x > 150 and x < 550) and (y> 140+ i*75 and y < 200 + i*75):
            showing = False
            aircraft = my_aircrafts[i]
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
    w.blit(end, (575,75))
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
      w.blit(end, (575,75))
      w.blit(start, (75, 75))
      w.blit(plane, (i, 118))
      i += 1
      pygame.time.wait(int(1000 * (aircrafts[aircraft]['speed']/distance)))
      pygame.display.flip()

  
      
    pygame.draw.line(w,black, (0,375), (750,375), 5)
    summary_txt = title_font.render("---- Flight Summary ---- ", True, white)
    main_cost = 0
    main_cost = aircrafts[aircraft]['passengers'] * aircrafts[aircraft]['per_passenger']
    ticket = font.render(f"Ticket cost earning:   ${main_cost}", True, white)
    comfort_rand = random.randint(0, aircrafts[aircraft]['comfort'])
    main_cost += comfort_rand
    safety_rand = random.randint(0, aircrafts[aircraft]['safety'])
    main_cost += safety_rand
    comfort = font.render(f"Comfort/Seating Earnings:   ${comfort_rand}", True, white)
    landing,landing_pt = random.choice(list(landings.items()))
    main_cost += landing_pt
    safety = font.render(f"Safety Earnings:   ${safety_rand + landing_pt}", True, white)
    total = font.render(f"Total Earnings:   $ {main_cost}", True, white)
    money += main_cost
    w.blit(summary_txt, (125,450))
    w.blit(ticket, (150, 500))
    w.blit(comfort, (150, 550))
    w.blit(safety, (150,600))
    w.blit(total, (150, 650))
    pygame.display.flip()
    pygame.time.wait(5000)
    flying = False

def buyplane():
  buying = True
  while buying:
    global money
    w.fill(bg)
    aircraft_opt = title_font.render("Aircraft Shop", True, white)
    w.blit(aircraft_opt, (225,25))
    for i in range(len(aircraft_names)):
      aircraft = aircraft_names[i]
      a = font.render(f"{aircraft_names[i]} - ${aircrafts[aircraft]['cost']}", True, white)
      w.blit(a,(200, int(150 + i * 75)))
      r = pygame.Rect(150, 140 + i * 75, 500, 60 )
      pygame.draw.rect(w,red,r, 5)
    quit = font.render("Leave", True, white)
    w.blit(quit, (60, 0))
    quit_box = pygame.Rect(50,0, 150, 50)
    pygame.draw.rect(w,black,quit_box, 5)
    cash_rect = pygame.Rect(600,0, 150,50)
    pygame.draw.rect(w,black,cash_rect, 2)
    coin = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coin, (40,40))
    w.blit(coin, (610,5))
    cash = small_font.render(str(money), True, white)
    w.blit(cash, (660, 10))
    pygame.display.flip()

    for event in pygame.event.get():
      x,y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if (x > 50 and x < 200) and (y > 0 and y < 50):
          buying = False
        for i in range(len(aircraft_names)):
          aircraft = aircraft_names[i]
          if (x > 150 and x < 650) and (y> 140+ i*75 and y < 200 + i*75):
            if money >= aircrafts[aircraft]['cost']:
              if aircrafts[aircraft] not in my_aircrafts:
                my_aircrafts.append(str(aircraft))
                money -= aircrafts[aircraft]['cost']
                buying = False
              else:
                bought = small_font.render("* Already Owned Plane *", True, red)
                w.blit(bought, (85, 85))
                pygame.display.flip()
                pygame.time.wait(500)

            else:
              broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
              w.blit(broke, (85, 85))
              pygame.display.flip()
              pygame.time.wait(500)
        


      if event.type == pygame.QUIT:
        pygame.quit()
      pygame.display.flip()


def view_airline():
  viewing = True
  while viewing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            viewing = False
    w.fill(bg)
    airline = title_font.render("-------- World Air --------", True, white)
    cash = font.render(f"Money: {money}", True, white)
    leave_view = font.render("Press enter to leave", True, red)
    aircraft_title = font.render("----- Aircrafts In Use ----- ", True, white)
    for i in range(len(my_aircrafts)):
      a = small_font.render(f"{i+1}: {my_aircrafts[i]}", True, white)
      w.blit(a, (225, 350 + i * 40))
    w.blit(airline, (140, 50))
    w.blit(cash, (150, 150))
    w.blit(leave_view, (200, 700))
    w.blit(aircraft_title, (150, 300))
    pygame.draw.line(w,black, (0, 685), (750,685), 5)
    pygame.display.flip()
  
def upgrade():
  global money
  upgrading = True
  while upgrading:
    num2 = 0
    x = 20
    w.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          for i in range(len(upgrade_names)):
            if ((x > 10 and x < 310) or (x > 400 and x < 700)) and (y > 140 + i * 75 and y < 215 + i * 75):
              num2 = i + 1
              
              if x > 400:
                num2 = i + 8

              print(f"hi {num2}" )
    if num2 == 1:
      up = upgrade_names[num2-1]
      money -= upgrades[up]
      for k in my_aircrafts:
        aircrafts[k]['comfort'] += 3
      
      
      """In-Flight Drinks Service": 75000
  "In-Flight Food Service": 250000
  "Google Sponsership": 350000
  "Business class seating": 500000
  "First class seating": 750000
  "Apple Sponorship": 900000
  "Amazon Sponsorship": 1000000
  "EntyFish Pilot": 1200000
"""



          

    upgrade_title = title_font.render("Upgrades", True, white)
    pygame.draw.line(w,black, (0,75), (750,75), 5)
    w.blit(upgrade_title, (250,15))
    num = 0
    for i in range(len(upgrade_names)):
      u = upgrade_names[i]
      a = small_font.render(f"{u}",True, white)
      m = small_font.render(f" ${upgrades[u]}", True, white)
      y = num * 75
      w.blit(a, (x, 150 + y))
      w.blit(m, (x, 175 + y))
      r = pygame.Rect(x-10,140 + y, 300, 75)
      pygame.draw.rect(w, black, r, 5)  
      if num >= 6:
        x = 400
        num = -1
      num += 1
            
    pygame.display.flip()








running = True
while running:
  w.fill(bg)
  title_font = pygame.font.SysFont("Arial", 50)
  font = pygame.font.SysFont("Arial", 40)
  title = title_font.render("Airline Simulator", True, white)
  w.blit(title,(225, 50))
  opt1 = font.render("Fly Plane", True, white)
  opt2 = font.render("Buy Aircrafts", True, white)
  opt3 = font.render("Airline Profile", True, white)
  opt4 = font.render("Upgrades", True, white)
  opt5 = font.render("coming soon", True, white)
  w.blit(opt1, (200,200))
  w.blit(opt2, (200, 300))
  w.blit(opt3, (200,400))
  w.blit(opt4, (200,500))
  w.blit(opt5, (200, 600))
  coin = pygame.image.load("coin.png")
  coin = pygame.transform.scale(coin, (40,40))
  w.blit(coin, (610,5))
  cash = small_font.render(str(money), True, white)
  w.blit(cash, (660, 10))
  r = pygame.Rect(150, 175, 400, 85)
  r2 = pygame.Rect(150, 275, 400, 85)
  r3 = pygame.Rect(150, 375, 400, 85)
  r4= pygame.Rect(150, 475, 400, 85)
  r5 = pygame.Rect(150, 575, 400, 85)
  cash_rect = pygame.Rect(600,0, 150,50)
  pygame.draw.rect(w,black,cash_rect, 2)
  #pygame.draw.rect(w,red,r1, 5)
  #pygame.draw.rect(w,red,r2, 5)
  #pygame.draw.rect(w,red,r3, 5)
  #pygame.draw.rect(w,red,r4, 5)
  #pygame.draw.rect(w,red,r5, 5)
  options = 5
  for i in range(options):
    r = pygame.Rect(150, 175 + i * 100, 400, 85)
    pygame.draw.rect(w,red,r, 5)

  pygame.display.flip()
    



 
   #### Conditions ####
  x,y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      for i in range(options):
        if (x > 150 and x < 650) and (y > 175 + i * 100 and y < 260 + i * 100):
          num = i + 1
          print(num)
        
          

  #### Main Options ####
  if num == 1:
    flyplane()
    num = 0
  elif num == 2:
    buyplane()
    num = 0
  elif num == 3:
    view_airline()
    num = 0
  elif num == 4:
    upgrade()
    num = 0



pygame.display.update()
   


