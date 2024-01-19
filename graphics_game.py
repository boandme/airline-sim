import pygame
import pygame.font
import random
import time
num = 0

pygame.init() 
w = pygame.display.set_mode((750,750))
pygame.display.set_caption('Airline Simulator v2.0.3 | Vyom')
c = pygame.time.Clock()
timer = 0


white=(255,255,255)
red = (255,0,0)
green = (17,140,79)
blue = (8,118,219)
bg = (135, 206, 235)
black = (0,0,0)
title_font = pygame.font.SysFont("Comic Sans", 50)
font = pygame.font.SysFont("Comic Sans", 40)
small_font = pygame.font.SysFont("Arial", 25)
money = 0
planing = False
#### Aircrafts Dictionary ####
aircraft_names = ["Dc 3", "Airbus A318", "Airbus A319", "Airbus A350", "Airbus A340", "Boeing 777", "Boeing 747", "Airbus A380"]
aircrafts = {
  "Dc 3": {
    "cost": 1000,
    "passengers": 30,
    "per_passenger": 80,
    "comfort": 25,
    "safety": 40,
    "speed": 8
    
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
    "speed": 6
    
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
    "speed": 4
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
    "speed": 2.5
  },
  "Airbus A380": {
    "cost": 1000000,
    "passengers": 705,
    "per_passenger": 180,
    "comfort": 70,
    "safety": 60,
    "speed": 2
    
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

 

move = False
times = []
my_aircrafts = []

##### Destinations #####
destinations = ["DTW", "ORD", "MSP", "ATL", "MIA", "MSY", "IAD", "JFK", "DEN", "SLC", "SEA", "SFO", "LAX", "SAN", "DFW", "IAH", "MCI", "CVG", "Boston", "PDX", "PHL"]
west = ["SEA", "PDX", "SFO", "LAX", "SAN", "SLC"]
mid = ["DTW", "ORD", "DEN", "DFW", "IAH", "MCI", "CVG", "MSP"]
east = ["ATL", "MIA", "MSY", "IAD", "JFK", "BOS", "PHL"]
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
upgrade_names = ["In-Flight Drinks Service", "In-Flight Food Service","Google Sponsership","Business class seating","First class seating","Apple Sponorship","Amazon Sponsorship","EntyFish Pilot"]
upgrades= {
  "In-Flight Drinks Service": 75000,
  "In-Flight Food Service": 250000,
  "Google Sponsership": 350000,
  "Business class seating": 500000,
  "First class seating": 750000,
  "Apple Sponorship": 900000,
  "Amazon Sponsorship": 1000000,
  "EntyFish Pilot": 1200000,
}
p1 = random.choice(destinations)
destinations.remove(p1)
p2 = random.choice(destinations)
destinations.append(p1)
time_of_day = random.choice(["AM", "PM"])
my_aircrafts.append({
   "Name": "Dc 3",
   "p1":p1,
   "p2": p2,
   "x": 5,
})

money = 100000
for i in my_aircrafts:
  times.append(timer)

def draw_background():
   bg = pygame.image.load("sky_bg.jpeg")
   bg = pygame.transform.scale(bg, (750,750))
   w.blit(bg, (0,0))

def advance_planes():
  global money
  global times
  global my_aircrafts
  global planing
  for i in range(len(my_aircrafts)):
    distance = 315
    name = my_aircrafts[i]["Name"]
    cover_dist = int(distance/(aircrafts[name]["speed"]))
    my_aircrafts[i]["x"] += cover_dist/100
    pygame.time.wait(10)
    if my_aircrafts[i]["x"] > 320:
        p1 = random.choice(destinations)
        destinations.remove(p1)
        p2 = random.choice(destinations)
        destinations.append(p1)
        my_aircrafts[i]["p1"] = p1
        my_aircrafts[i]["p2"] = p2
        my_aircrafts[i]["x"] = 5
        main_cost = 0
        name = my_aircrafts[i]["Name"]
        main_cost = aircrafts[name]['passengers'] * aircrafts[name]['per_passenger']
        comfort_rand = 3 * random.randint(0, aircrafts[name]['comfort'])
        main_cost += comfort_rand
        safety_rand = 2 * random.randint(0, aircrafts[name]['safety'])
        main_cost += safety_rand
        
        landing,landing_pt = random.choice(list(landings.items()))
        main_cost += landing_pt
        money += main_cost
        
        
     
    
    
def autoplane():
  planeX = 5
  global money
  global move
  global times
  planing = True
  distance = 315
  while planing:
    draw_background()
    title = title_font.render("--- Your current flights ---", True, white)
    w.blit(title, (150, 50))

    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        if (x > 10 and x < 160) and (y > 0 and y < 50):
          planing = False
    for i in range(len(my_aircrafts)):
      distance = 315
      name = my_aircrafts[i]["Name"]
      cover_dist = int(distance/(aircrafts[name]["speed"]))
      my_aircrafts[i]["x"] += cover_dist/100
      pygame.time.wait(10)
      d = pygame.Rect(0, 150 + i * 75, 375, 75)
      pygame.draw.rect(w,black, d, 5)
      pygame.draw.line(w,black, (25, 200 + i * 75), (350, 200 + i * 75), 3)
      pygame.draw.circle(w,black,(25,200 + i * 75),4)
      pygame.draw.circle(w,black,(350,200 + i * 75), 4)
      coin = pygame.image.load("coin.png")
      coin = pygame.transform.scale(coin, (40,40))
      w.blit(coin, (610,5))
      cash = small_font.render(str(money), True, white)
      w.blit(cash, (660, 15))
      cash_rect = pygame.Rect(600,0, 150,50)
      pygame.draw.rect(w,black,cash_rect, 3)
      quit = font.render("Leave", True, white)
      quit_box = pygame.Rect(10,0, 150, 50)
      pygame.draw.rect(w,blue,quit_box, 0, 16)
      w.blit(quit, (40, 10))
      plane_name = small_font.render(my_aircrafts[i]["Name"], True, black)
      point1 = small_font.render(my_aircrafts[i]["p1"], True, black)
      point2 = small_font.render(my_aircrafts[i]["p2"], True, black)
      w.blit(plane_name, (172, 165 + i * 75))
      w.blit(point1, (15,165 + i * 75))
      w.blit(point2, (330,165 + i * 75))
      plane = pygame.image.load("airliner.png")
      plane = pygame.transform.scale(plane, (50,35))
      w.blit(plane, (my_aircrafts[i]["x"], 182 + i * 75))
      name = my_aircrafts[i]["Name"]
      cover_dist = int(distance/(aircrafts[name]["speed"]))
      my_aircrafts[i]["x"] += cover_dist/1000
      pygame.time.wait(1)
      
      if my_aircrafts[i]["x"] > 320:
        p1 = random.choice(destinations)
        destinations.remove(p1)
        p2 = random.choice(destinations)
        destinations.append(p1)
        my_aircrafts[i]["p1"] = p1
        my_aircrafts[i]["p2"] = p2
        my_aircrafts[i]["x"] = 5
        main_cost = 0
        name = my_aircrafts[i]["Name"]
        main_cost = aircrafts[name]['passengers'] * aircrafts[name]['per_passenger']
        comfort_rand = 3 * random.randint(0, aircrafts[name]['comfort'])
        main_cost += comfort_rand
        safety_rand = 2 * random.randint(0, aircrafts[name]['safety'])
        main_cost += safety_rand
        
        landing,landing_pt = random.choice(list(landings.items()))
        main_cost += landing_pt
        total = font.render("+ " + str(main_cost), True, green)
        money += main_cost
        w.blit(total, (375, 180 + i * 75))
        pygame.display.flip()
        
        
         
      
      
      
         

    

      
      

      ac = my_aircrafts[i]["Name"]
      #if times[i] > aircrafts[ac]['speed'] * 1000:
        #print("hih")
        #times[i] -= aircrafts[ac]['speed'] * 1000
        #print("complete")
        
        
        
        
      
        
        
    c.tick(60)
    pygame.display.flip()

    
          
  

def flyplane():
  global money
  global aircrafts
  global my_aircrafts
  showing = True
  while showing:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
    draw_background()
    
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
    w.blit(aircraft_opt, (175,50))
    final_hours = hours
    final_minutes = minutes
    final_time_of_day = time_of_day
    if ((p1 in west and p2 in west) or (p1 in east and p2 in east) or (p1 in mid and p2 in mid)):
            hours_spent = random.randint(1, 3)
    elif (p1 in west and p2 in mid) or (p2 in west and p1 in mid):
            hours_spent = random.randint(2, 4)
    elif (p1 in east and p2 in mid) or (p2 in east and p1 in mid):
            hours_spent = random.randint(2, 4)
    elif (p1 in west and p2 in east) or (p2 in west and p1 in east):
            hours_spent = random.randint(3, 6)
    else:
       hours_spent = random.randint(1,3)
    minutes_spent = random.randint(0, 59)
    for i in range(hours_spent):
        final_hours += 1
        if final_hours > 12:
            final_hours = 1
            if time_of_day == "AM":
              final_time_of_day = "PM"
            elif time_of_day == "PM":
              final_time_of_day = "AM"
        final_minutes = int(final_minutes)
        for i in range(minutes_spent):
            final_minutes += 1
            if final_minutes > 59:
                final_minutes = 0
                final_hours += 1
        if final_minutes < 10:
            final_minutes = "0" + str(final_minutes)
    for i in range(len(my_aircrafts)):
      a = font.render(my_aircrafts[i], True, white)
      r = pygame.Rect(150, 140 + i * 75, 400, 60 )
      pygame.draw.rect(w,blue,r, 0, 16)
      w.blit(a,(275, 150 + i * 75) )
      
      


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
    draw_background()
    details = title_font.render("--- Flight Details ---", True, white)
    airline = font.render("World Air", True, white)
    num = font.render(f"Flight Number: {flight_num} ", True, white)
    path = font.render(f"{p1} ---> {p2}", True, white)
    takeoff = font.render(f"Takeoff: {hours}:{minutes} {time_of_day}", True, white)
    directions = title_font.render("Press Enter to take off", True, white)
    
    landing = font.render(f"Landing: {final_hours}:{final_minutes} {final_time_of_day}", True, white)
    w.blit(details, (200,50))
    w.blit(airline, (100,150))
    w.blit(num, (100,200))
    w.blit(path, (100,250))
    w.blit(takeoff, (100,300))
    w.blit(landing, (100, 350))
    
    r = pygame.Rect(0,600, 750, 150)
    pygame.draw.rect(w,blue,r, 0, 16)
    w.blit(directions, (150, 650))  
    pygame.display.flip()

  flying = True
  while flying:
    draw_background()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    if aircraft == "Boeing 747":
      plane = pygame.image.load("747.png]")
    else:
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
      draw_background()
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

  
      
    
    r = pygame.Rect(0,375, 750, 375)
    pygame.draw.rect(w,blue,r)
    summary_txt = title_font.render("---- Flight Summary ---- ", True, white)
    main_cost = 0
    main_cost = aircrafts[aircraft]['passengers'] * aircrafts[aircraft]['per_passenger']
    ticket = font.render(f"Ticket cost earning:   ${main_cost}", True, white)
    comfort_rand = 3 * random.randint(0, aircrafts[aircraft]['comfort'])
    main_cost += comfort_rand
    safety_rand = 2 * random.randint(0, aircrafts[aircraft]['safety'])
    main_cost += safety_rand
    comfort = font.render(f"Comfort/Seating Earnings:   ${comfort_rand}", True, white)
    landing,landing_pt = random.choice(list(landings.items()))
    main_cost += landing_pt
    safety = font.render(f"Safety Earnings:   ${safety_rand + landing_pt}", True, white)
    total = font.render(f"Total Earnings:   $ {main_cost}", True, white)
    money += main_cost
    w.blit(summary_txt, (125,400))
    w.blit(ticket, (125, 500))
    w.blit(comfort, (125, 550))
    w.blit(safety, (125,600))
    w.blit(total, (125, 650))
    pygame.display.flip()
    pygame.time.wait(5000)
    flying = False

def buyplane():
  buying = True
  while buying:
    advance_planes()
    global money
    draw_background()
    aircraft_opt = title_font.render("Aircraft Shop", True, white)
    w.blit(aircraft_opt, (225,25))
    for i in range(len(aircraft_names)):
      aircraft = aircraft_names[i]
      a = font.render(f"{aircraft_names[i]} - ${aircrafts[aircraft]['cost']}", True, white)
      
      r = pygame.Rect(150, 140 + i * 75, 500, 60 )
      pygame.draw.rect(w,blue,r, 0, 16)
      w.blit(a,(200, int(150 + i * 75)))
    quit = font.render("Leave", True, white)
    
    quit_box = pygame.Rect(50,0, 150, 50)
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (60, 0))
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
                my_aircrafts.append({
                   "Name": aircraft,
                   "p1": p1,
                   "p2": p2,
                   "x": 5
                })
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
    advance_planes()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            viewing = False
    draw_background()
    airline = title_font.render("-------- World Air --------", True, white)
    cash = font.render(f"Money: ${money}", True, white)
    leave_view = font.render("Press enter to leave", True, white)
    aircraft_title = font.render("----- Aircrafts In Use ----- ", True, white)
    for i in range(len(my_aircrafts)):
      a = small_font.render(f"{i+1}: {my_aircrafts[i]['Name']}", True, white)
      w.blit(a, (225, 350 + i * 40))
    w.blit(airline, (100, 50))
    w.blit(cash, (150, 150))
    
    w.blit(aircraft_title, (150, 300))
    r = pygame.Rect(0,685, 750, 65)
    pygame.draw.rect(w,blue,r, 0, 16)
    w.blit(leave_view, (200, 700))
    pygame.display.flip()
  
def upgrade():
  global money
  upgrading = True
  while upgrading:
    advance_planes()
    num2 = 0
    
    draw_background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          if (x > 50 and x < 200) and (y > 0 and y < 50):
            upgrading = False
          
          for i in range(len(upgrade_names)):
            if ((x > 10 and x < 310) or (x > 400 and x < 700)) and (y > 140 + i * 75 and y < 215 + i * 75):
              num2 = i + 1
              
              if x > 400:
                num2 = i + 8

    upgrade_title = title_font.render("Upgrades", True, white)
    pygame.draw.line(w,black, (0,100), (750,100), 5)
    w.blit(upgrade_title, (250,15))
    num = 0
    x = 20
    for i in range(len(upgrade_names)):
      advance_planes()
      u = upgrade_names[i]
      a = small_font.render(f"{u}",True, white)
      m = small_font.render(f" ${upgrades[u]}", True, white)
      y = num * 85
      
      r = pygame.Rect(x-10,140 + y, 300, 75)
      pygame.draw.rect(w, blue, r, 0, 16) 
      w.blit(a, (x, 150 + y))
      w.blit(m, (x, 175 + y)) 
      if num >= 6:
        x = 400
        num = -1
      num += 1

    quit = font.render("Leave", True, white)
    quit_box = pygame.Rect(50,0, 150, 50)
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (70, 10))
    cash_rect = pygame.Rect(600,0, 150,50)
    pygame.draw.rect(w,black,cash_rect, 2)
    coin = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coin, (40,40))
    w.blit(coin, (610,5))
    cash = small_font.render(str(money), True, white)
    w.blit(cash, (660, 10))
            
    pygame.display.flip()
 
    if num2 == 1:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          n = k["Name"]
          aircrafts[n]['comfort'] += 9

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)
    elif num2 == 2:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['comfort'] += 15

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)

    elif num2 == 3:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['per_passenger'] += 2

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)
      
    elif num2 == 4:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['comfort'] += 25

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)
      
    elif num2 == 5:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['comfort'] += 39

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)

    elif num2 == 6:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['per_passenger'] += 6

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)

    elif num2 == 7:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['per_passenger'] += 10

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)

    elif num2 == 8:
      up = upgrade_names[num2-1]
      if money >= upgrades[up]:
        money -= upgrades[up]
        for k in my_aircrafts:
          k = k["Name"]
          aircrafts[k]['safety'] += 19

      else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 85))
          pygame.display.flip()
          pygame.time.wait(500)

def credits():
   draw_background()
   crediting = True
   while crediting:
    advance_planes()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            crediting = False
       
    credit_title = title_font.render("-------- Credits --------", True, white)
    test_title = font.render("Game Testers: ", True, white)
    test1 = small_font.render("EntyXD", True, white)
    test2 = small_font.render("Monke", True, white)
    leave_view = font.render("Press enter to leave", True, white)
    w.blit(credit_title, (100, 50))
    w.blit(test_title, (150, 150))
    
    w.blit(test1, (150, 250))
    w.blit(test2, (150, 275))
    
    r = pygame.Rect(0,685, 750, 65)
    pygame.draw.rect(w,blue,r, 0, 16)
    w.blit(leave_view, (200, 700))
    pygame.display.flip()

      







running = True
music = pygame.mixer.Sound("cosmic-love.mp3")
while running:
  pygame.mixer.Sound.play(music)
  draw_background()
  title_font = pygame.font.SysFont("Playfair Display", 50)
  font = pygame.font.SysFont("Karla", 40)
  small_font = pygame.font.SysFont("Karla", 25)
  title = title_font.render("Airline Simulator", True, white)
  w.blit(title,(200, 50))
  opt1 = font.render("Fly Plane ", True, white)
  opt2 = font.render("Buy Aircrafts", True, white)
  opt3 = font.render("Airline Profile", True, white)
  opt4 = font.render("Upgrades", True, white)
  opt5 = font.render("Credits", True, white)
  
  #w.blit(opt5, (200, 600))
  coin = pygame.image.load("coin.png")
  coin = pygame.transform.scale(coin, (40,40))
  w.blit(coin, (610,5))
  cash = small_font.render(str(money), True, white)
  cash_rect = pygame.Rect(600,0, 150,50)
  pygame.draw.rect(w,black,cash_rect, 3)
  w.blit(cash, (660, 10))
  r = pygame.Rect(175, 175, 400, 85)
  r2 = pygame.Rect(150, 275, 400, 85)
  r3 = pygame.Rect(150, 375, 400, 85)
  r4= pygame.Rect(150, 475, 400, 85)
  #r5 = pygame.Rect(150, 575, 400, 85)
  
  #pygame.draw.rect(w,red,r1, 5)
  #pygame.draw.rect(w,red,r2, 5)
  #pygame.draw.rect(w,red,r3, 5)
  #pygame.draw.rect(w,red,r4, 5)
  #pygame.draw.rect(w,red,r5, 5)
  options = 5
  for i in range(options):
    r = pygame.Rect(175, 175 + i * 100, 400, 85)
    pygame.draw.rect(w,blue,r, 0, 16)

  w.blit(opt1, (250,190))
  w.blit(opt2, (235, 290))
  w.blit(opt3, (235,390))
  w.blit(opt4, (235,490))
  w.blit(opt5, (235, 590))

  pygame.display.flip()
    



 
   #### Conditions ####
  x,y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      for i in range(options):
        if (x > 175 and x < 575) and (y > 175 + i * 100 and y < 260 + i * 100):
          num = i + 1
          
        
          

  #### Main Options ####
  if num == 1:
    autoplane()
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
  elif num == 5:
    credits()
    num = 0

  advance_planes()
  c.tick(60)
pygame.display.update()
   