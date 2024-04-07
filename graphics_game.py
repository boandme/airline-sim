import pygame
import pygame.font
import random
import time
import math
num = 0
pygame.init() 
w = pygame.display.set_mode((750,750))
pygame.display.set_caption('Airline Simulator v2.2.5 | Vyom')
c = pygame.time.Clock()

white=(255,255,255)
red = (255,0,0)
green = (17,140,79)
blue = (8,118,219)
bg = (135, 206, 235)
black = (0,0,0)
light_grey =(211,211,211)
light_green = (117,193,34)
title_font = pygame.font.SysFont("Comic Sans", 50)
font = pygame.font.SysFont("Comic Sans", 40)
small_font = pygame.font.SysFont("Arial", 25)
mid_small_font = pygame.font.SysFont("Comic Sans", 33)
sell_rate = 0.45
pilots = []
copilots = []
planing = False
my_pilots = []
my_copilots  = []
#### Aircrafts Dictionary ####
aircraft_names = ["Dc 3", "Airbus A318", "Airbus A319", "Airbus A350", "Boeing 777", "Boeing 747", "Airbus A380", "Concorde"]
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
  },
  "Airbus A340": {
    "cost": 175000,
    "passengers": 372,
    "per_passenger": 126,
    "comfort": 55, 
    "safety": 45,
    "speed": 4
  },


}

 

move = False
times = []
my_aircrafts = []
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
first_name = ''
surname = ''
def getname():
  global first_name
  global surname
  first_name = ''
  for i in range(random.randint(1, 3)):
    first_name += random.choice(vowels) + ''.join(random.choices(consonants, k = 2)) 
  surname = ''
  for i in range(random.randint(1, 2)):
    surname += random.choice(vowels) + ''.join(random.choices(consonants, k = 2))
  if random.randrange(1):
    first_name += random.choice(vowels)
  if random.randrange(1):
    surname += random.choice(vowels)
  
  

for i in range(5):
  getname()
  rating = random.randint(1,5)
  price = int((rating * 10000) * random.randint(80, 100)/100)
  pilots.append({
    "Name": first_name.capitalize() + " " +  surname.capitalize(),
    "Price": price,
    "Rating": rating

    })

for i in range(5):
  rating = random.randint(1,5)
  price = int((rating * 10000) * random.randint(80, 100)/100)
  getname()

  copilots.append({
    "Name": first_name.capitalize() + " " +  surname.capitalize(),
    "Price": price,
    "Rating": rating

    })






##### Destinations #####
destinations = ["DTW", "ORD", "MSP", "ATL", "MIA", "MSY", "IAD", "JFK", "DEN", "SLC", "SEA", "SFO", "LAX", "SAN", "DFW", "IAH", "MCI", "CVG", "Boston", "PDX", "PHL"]

international_destinations = [{
    "Name": "New York City", 
    "x": 214,
    "y": 118
      },
    {   
    "Name": "Los Angeles",
    "x": 132,
    "y": 128
    },
    {
    "Name": "Chicago",
    "x": 186,
    "y": 114
  },
  {
    "Name": "Houston",
    "x": 170,
    "y": 134
  },
  {
    "Name": "Philadelphia",
    "x": 208,
    "y": 120
  },
  {
    "Name": "Indianapolis",
    "x": 188,
    "y": 121
  },
  {
    "Name": "San Francisco",
    "x": 127,
    "y": 121
  },
  {
    "Name": "Seattle",
    "x": 129,
    "y": 107
  },
  {
    "Name": "Denver",
    "x": 150,
    "y": 120
  },
  {
    "Name": "Boston",
    "x": 218,
    "y": 114
  },
  ]
 
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
domestic_destinations = [{
    "Name": "New York City", 
    "x": 718,
    "y": 244
      },
    {   
    "Name": "Los Angeles",
    "x": 77,
    "y": 381
    },
    {
    "Name": "Chicago",
    "x": 529,
    "y": 259
  },
  {
    "Name": "Houston",
    "x": 429,
    "y": 505
  },
  {
    "Name": "Philadelphia",
    "x": 711,
    "y": 258
  },
  {
    "Name": "Indianapolis",
    "x": 553,
    "y": 296
  },
  {
    "Name": "San Francisco",
    "x": 37,
    "y": 297
  },
  {
    "Name": "Seattle",
    "x": 86,
    "y": 103
  },
  {
    "Name": "Denver",
    "x": 288,
    "y": 301
  },
  {
    "Name": "Boston",
    "x": 751,
    "y": 204
  },
  ]

    
p1 = random.choice(domestic_destinations)
domestic_destinations.remove(p1)
p2 = random.choice(domestic_destinations)

domestic_destinations.append(p1)
time_of_day = random.choice(["AM", "PM"])
my_aircrafts.append({
   "Name": "Dc 3",
   "p1":p1["Name"],
   "p2": p2["Name"],
   "x": p1["x"],
   "y": p1["y"],
   "Pilot": "none",
   "Copilot": "none"
})




money = 150000

def draw_background():
   bg = pygame.image.load("sky_bg.jpeg")
   bg = pygame.transform.scale(bg, (800,800))
   w.blit(bg, (0,0))

def advance_planes():
  global money
  global times
  global my_aircrafts
  global planing
  global money
  final_x = 0
  final_y = 0
  start_x = 500
  start_y = 500
  if len(my_pilots) >= len(my_aircrafts):
    for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]
  else:
    for i in range(len(my_pilots)):
      my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]

  if len(my_copilots) >= len(my_aircrafts):
    for i in range(len(my_aircrafts)):
      my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
  else:
    for i in range(len(my_copilots)):
      my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  for i in range(len(my_aircrafts)):
    for d in range(len(domestic_destinations)):
      if my_aircrafts[i]["p2"] == domestic_destinations[d]["Name"]:
        
        destination = domestic_destinations[d]["Name"]
        final_x = domestic_destinations[d]["x"]
        final_y = domestic_destinations[d]["y"]
         
          
      if my_aircrafts[i]["p1"] == domestic_destinations[d]["Name"]:
          
        start_x = domestic_destinations[d]["x"]
        start_y = domestic_destinations[d]["y"]
    delta_x = final_x - start_x
    delta_y = final_y - start_y
      

    # Calculate the distance using the Pythagorean theorem
    distance = math.sqrt(delta_x**2 + delta_y**2)

    # Calculate velocity for both x and y axes
    name = my_aircrafts[i]["Name"] 
    speed = aircrafts[name]["speed"] * 80
    velocity_x = delta_x / speed
    velocity_y = delta_y / speed
    if my_aircrafts[i]["Pilot"] != "none" and my_aircrafts[i]["Copilot"] != "none":
      my_aircrafts[i]["x"] += velocity_x
      my_aircrafts[i]["y"] += velocity_y
    print(f"Current plane0 coordinates {my_aircrafts[0]['x']},{my_aircrafts[0]['y']}")
   
    print(velocity_y)
      

    x_range_low = final_x - 10
    x_range_high = final_x + 10
    y_range_low = final_y - 10
    y_range_high = final_y + 10
    if (my_aircrafts[i]["x"] >= x_range_low and my_aircrafts[i]["x"] <=  x_range_high) and (my_aircrafts[i]["y"] >= y_range_low and my_aircrafts[i]["y"] <=  y_range_high):
      p1 = random.choice(domestic_destinations)
      domestic_destinations.remove(p1)
      p2 = random.choice(domestic_destinations)
        
      domestic_destinations.append(p1)
      my_aircrafts[i]["p1"] = p1["Name"]
      my_aircrafts[i]["p2"] = p2["Name"]
      my_aircrafts[i]["x"] = p1["x"]
      my_aircrafts[i]["y"] = p1["y"]
      main_cost = 0
      name = my_aircrafts[i]["Name"]
      main_cost = aircrafts[name]['passengers'] * aircrafts[name]['per_passenger']
      comfort_rand = 3 * random.randint(0, aircrafts[name]['comfort'])
      main_cost += comfort_rand
      safety_rand = 2 * random.randint(0, aircrafts[name]['safety'])
      main_cost += safety_rand
      pilot = my_aircrafts[i]["Pilot"]
        
        
      copilot = my_aircrafts[i]["Copilot"]
      for d in range(len(my_pilots)):
          
        if my_pilots[d]["Name"] == pilot:
          my_pilots[d]["Level"] += 0.6

      for d in range(len(my_copilots)):
        if my_copilots[d]["Name"] == copilot:
          my_copilots[d]["Level"] += 0.3

      landing,landing_pt = random.choice(list(landings.items()))
      main_cost += landing_pt
        #total = font.render("+ " + str(main_cost), True, green)
      money += main_cost
        #w````.blit(total, (375, 180 + i * 75))
        
        
    
      
    



    
    
def autoplane():
  
 
  
  global money
  global move
  global times
  planing = True
  distance = 315
  while planing:
    if len(my_pilots) >= len(my_aircrafts):
      for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]
    else:
      for i in range(len(my_pilots)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]

    if len(my_copilots) >= len(my_aircrafts):
      for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
    else:
      for i in range(len(my_copilots)):
        my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
    draw_background()
    title = title_font.render("--- Your current flights ---", True, white)
    w.blit(title, (100, 50))
    coin = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coin, (40,40))
    w.blit(coin, (610,5))
    cash = small_font.render(str(money), True, white)
    w.blit(cash, (660, 15))
    cash_rect = pygame.Rect(600,0, 150,50)
    pygame.draw.rect(w,black,cash_rect, 3)
    quit = font.render("< Back", True, white)
    quit_box = pygame.Rect(10,0, 150, 50)
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (30, 0))
    
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
      d = pygame.Rect(0, 150 + i * 100, 375, 75)
      pygame.draw.rect(w,black, d, 5)
      pygame.draw.line(w,black, (25, 200 + i * 100), (350, 200 + i * 100), 3)
      pygame.draw.circle(w,black,(25,200 + i * 100),4)
      pygame.draw.circle(w,black,(350,200 + i * 100), 4)
      plane_name = small_font.render(my_aircrafts[i]["Name"], True, black)
      point1 = small_font.render(my_aircrafts[i]["p1"], True, black)
      point2 = small_font.render(my_aircrafts[i]["p2"], True, black)
      w.blit(plane_name, (150, 165 + i * 100))
      w.blit(point1, (15,165 + i * 100))
      w.blit(point2, (310,165 + i * 100))
      plane = pygame.image.load("airliner.png")
      plane = pygame.transform.scale(plane, (50,35))
      w.blit(plane, (my_aircrafts[i]["x"], 182 + i * 100))
      name = my_aircrafts[i]["Name"]
      exclam = pygame.image.load("red-exclam.jpg")
      exclam = pygame.transform.scale(exclam ,(50,50))
      if my_aircrafts[i]["Pilot"] != "none" and my_aircrafts[i]["Copilot"] != "none":
        
        if aircrafts[name]["speed"] < 0.25:
          aircrafts[name]["speed"] = 0.25
        cover_dist = int(distance/(aircrafts[name]["speed"]))
        my_aircrafts[i]["x"] += cover_dist/100
        pygame.time.wait(10)
      elif my_aircrafts[i]["Pilot"] == "none" and my_aircrafts[i]["Copilot"] == "none":
        nopilot = mid_small_font.render("No Pilot or Copilot", True, red)
        w.blit(exclam, (375, 165 + i * 100))
        w.blit(nopilot, (450, 175 + i * 100))
      elif my_aircrafts[i]["Pilot"] == "none":
        w.blit(exclam, (375, 165 + i * 100))
        nopilot = mid_small_font.render("No Pilot", True, red)
        w.blit(nopilot, (450, 175 + i * 100))
      elif my_aircrafts[i]["Copilot"] == "none":
        w.blit(exclam, (375, 165 + i * 100))
        nopilot = mid_small_font.render("No Copilot", True, red)
        w.blit(nopilot, (450, 175 + i * 100))
      
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
        pilot = my_aircrafts[i]["Pilot"]
        
        copilot = my_aircrafts[i]["Copilot"]
        for d in range(len(my_pilots)):
          
          if my_pilots[d]["Name"] == pilot:
            my_pilots[d]["Level"] += 0.6

        for d in range(len(my_copilots)):
          if my_copilots[d]["Name"] == copilot:
            my_copilots[d]["Level"] += 0.3

        landing,landing_pt = random.choice(list(landings.items()))
        main_cost += landing_pt
        #total = font.render("+ " + str(main_cost), True, green)
        money += main_cost
        #w````.blit(total, (375, 180 + i * 75))
        pygame.display.flip()
        
    c.tick(60)
    pygame.display.flip()

    
          
  
def sellplane():
   global sell_rate
   global money
   global aircrafts
   global my_aircrafts
   selling = True
   while selling:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        for i in range(len(my_aircrafts)):
          if (x > 150 and x < 550) and (y> 140+ i*100 and y < 200 + i*100):
          
            
            aircraft = my_aircrafts[i]
            sold_r = pygame.Rect(150,140 + i * 100, 400, 60)
            pygame.draw.rect(w,green, sold_r, 0, 16)
            sold = font.render("SOLD", True, white)
            w.blit(sold, (275, 150 + i * 100))
            money += price
            my_aircrafts.remove(my_aircrafts[i])
            pygame.display.flip()
            pygame.time.wait(1000)

        if (x > 10 and x < 160) and (y > 0 and y < 50):
          selling = False

      if event.type == pygame.QUIT:
        pygame.quit()
    
    draw_background()
    quit = font.render("< Back", True, white)
    quit_box = pygame.Rect(10,0, 150, 50)
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (30, 0))
    coin = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coin, (40,40))
    w.blit(coin, (610,5))
    cash = small_font.render(str(money), True, white)
    w.blit(cash, (660, 15))
    cash_rect = pygame.Rect(600,0, 150,50)
    pygame.draw.rect(w,black,cash_rect, 3)
    aircraft_opt = title_font.render("Sell Planes", True, white)
    w.blit(aircraft_opt, (250,25))
    for i in range(len(my_aircrafts)):
      name = my_aircrafts[i]["Name"]
      price = int(aircrafts[name]["cost"] * sell_rate)
      sell_price = small_font.render("$" + str(price), True, white)
      sell_r = pygame.Rect(450, 120 + i * 100, 150, 50)
      a = font.render(my_aircrafts[i]["Name"], True, white)
      r = pygame.Rect(150, 140 + i * 100, 400, 60 )
      pygame.draw.rect(w,blue,r, 0, 16)
      pygame.draw.rect(w, light_green, sell_r, 0, 16)
      w.blit(sell_price, (470, 125 + i * 100))
      w.blit(a,(275, 150 + i * 100) )

    
    pygame.display.flip()
    advance_planes()
    
      
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
  global getname
  global surname
  global first_name
  upgradebuy = False
  planebuy = True
  global copilots
  global pilots
  pilotbuy = False
  copilotbuy = False
  global money
  buying = True
  
  while buying:
    num2 = 0
    draw_background()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    
    ##### #BUYPLANES ####
  
    while planebuy :
      advance_planes()
      draw_background()
      aircraft_opt = title_font.render("Aircraft Shop", True, white)
      w.blit(aircraft_opt, (225,0))
      r1 = pygame.Rect(0, 70, 190, 50)
      r2 = pygame.Rect(190,70, 190, 50)
      r3 = pygame.Rect(380, 70, 190, 50)
      r4 = pygame.Rect(570, 70, 180, 50)
      planes = font.render("Aircrafts", True, white)
      upgs = font.render("Upgrades", True, white)
      pils = font.render("Pilots", True, white)
      copils = font.render("Copilots", True, white)
      pygame.draw.rect(w, blue, r1)
      pygame.draw.rect(w, blue,r2 )
      pygame.draw.rect(w, blue, r3)
      pygame.draw.rect(w, blue, r4)
      pygame.draw.rect(w, white, r1, 3)
      pygame.draw.rect(w, white,r2, 3)
      pygame.draw.rect(w, white,r3, 3)
      pygame.draw.rect(w, white,r4, 3)
      w.blit(planes, (10, 70))
      w.blit(upgs, (200, 70))
      w.blit(pils, (390, 70))
      w.blit(copils, (580,70))
      quit = font.render("< Back", True, white)     
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
      

      for i in range(len(aircraft_names)):
        aircraft = aircraft_names[i]
        a = font.render(f"{aircraft_names[i]} - ${aircrafts[aircraft]['cost']}", True, white)    
        r = pygame.Rect(150, 140 + i * 75, 500, 60 )
        pygame.draw.rect(w,blue,r, 0, 16)
        w.blit(a,(200, int(150 + i * 75)))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          
          if r1.collidepoint(x,y):
            planebuy = True
            upgradebuy = False
            copilotbuy = False
            pilotbuy = False
          if r2.collidepoint(x,y):
            upgradebuy = True
            planebuy = False
            copilotbuy = False
            pilotbuy = False
          if r3.collidepoint(x,y):
            pilotbuy = True
            copilotbuy = False
            planebuy = False
            upgradebuy = False
          if r4.collidepoint(x,y):
            copilotbuy = True
            pilotbuy = False
            planebuy = False
            upgradebuy = False
            
          if (x > 50 and x < 200) and (y > 0 and y < 50):
            buying = False
            planebuy = False
            upgradebuy = False
        
          
          
          if len(my_aircrafts) < 6:
            for i in range(len(aircraft_names)):
              aircraft = aircraft_names[i]
              if (x > 150 and x < 650) and (y> 140+ i*75 and y < 200 + i*75):
                if money >= aircrafts[aircraft]['cost']:
                  if aircrafts[aircraft] not in my_aircrafts:
                    p1 = random.choice(domestic_destinations)
                    domestic_destinations.remove(p1)
                    p2 = random.choice(domestic_destinations)
                   
                    domestic_destinations.append(p1)
                    my_aircrafts.append({
                      "Name": aircraft,
                      "p1":p1["Name"],
                      "p2": p2["Name"],
                      "x": p1["x"],
                      "y": p1["y"],
                      "Pilot": "none",
                      "Copilot": "none"
                })


                    money -= aircrafts[aircraft]['cost']
                  

                else:
                  broke = font.render("*Insufficient Funds*", True, white)
                  r = pygame.Rect(150, 140 + i * 75, 500, 60 )
                  pygame.draw.rect(w, red,r, 0, 16)
                  w.blit(broke,(210, int(150 + i * 75)))
                  pygame.display.flip()
                  pygame.time.wait(500)

          else:
            max = font.render("* Plane Limit Reached *", True, white)
            r = pygame.Rect(150, 140 + i * 75, 500, 60 )
            pygame.draw.rect(w, red,r, 0, 16)
            w.blit(max,(210, int(150 + i * 75)))
            pygame.display.flip()
            pygame.time.wait(500)

      pygame.display.flip()

        ###### UPGRADE PLANES OPTION #####
    while upgradebuy:
      advance_planes()
      draw_background()
      aircraft_opt = title_font.render("Aircraft Shop", True, white)
      w.blit(aircraft_opt, (225,0))
      r1 = pygame.Rect(0, 70, 190, 50)
      r2 = pygame.Rect(190,70, 190, 50)
      r3 = pygame.Rect(380, 70, 190, 50)
      r4 = pygame.Rect(570, 70, 180, 50)
      planes = font.render("Aircrafts", True, white)
      upgs = font.render("Upgrades", True, white)
      pils = font.render("Pilots", True, white)
      copils = font.render("Copilots", True, white)
      pygame.draw.rect(w, blue, r1)
      pygame.draw.rect(w, blue,r2 )
      pygame.draw.rect(w, blue, r3)
      pygame.draw.rect(w, blue, r4)
      pygame.draw.rect(w, white, r1, 3)
      pygame.draw.rect(w, white,r2, 3)
      pygame.draw.rect(w, white,r3, 3)
      pygame.draw.rect(w, white,r4, 3)
      w.blit(planes, (10, 70))
      w.blit(upgs, (200, 70))
      w.blit(pils, (390, 70))
      w.blit(copils, (580,70))
      quit = font.render("< Back", True, white)     
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
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          if r1.collidepoint(x,y):
            planebuy = True
            upgradebuy = False
            copilotbuy = False
            pilotbuy = False
          if r2.collidepoint(x,y):
            upgradebuy = True
            planebuy = False
            copilotbuy = False
            pilotbuy = False
          if r3.collidepoint(x,y):
            pilotbuy = True
            planebuy = False
            upgradebuy = False
            copilotbuy = False
          if r4.collidepoint(x,y):
            copilotbuy = True
            pilotbuy = False
            planebuy = False
            upgradebuy = False
          if (x > 50 and x < 200) and (y > 0 and y < 50):
            buying = False
            planebuy = False
            upgradebuy = False
          
          
          for i in range(len(upgrade_names)):
            if ((x > 10 and x < 310) or (x > 400 and x < 700)) and (y > 140 + i * 75 and y < 215 + i * 75):
              num2 = i + 1
              
              if x > 400:
                num2 = i + 8

      
      
      num = 0
      x = 20
      for i in range(len(upgrade_names)):
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
          w.blit(broke, (85,720))
          pygame.display.flip()
          pygame.time.wait(500)
        num2 = 0
      elif num2 == 2:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['comfort'] += 15

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))
            pygame.display.flip()
            pygame.time.wait(500)
        num2 = 0

      elif num2 == 3:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['per_passenger'] += 2

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))
            pygame.display.flip()
            pygame.time.wait(500)
        num2 = 0
      
      elif num2 == 4:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['comfort'] += 25

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))
            pygame.display.flip()
            pygame.time.wait(500)
        num2 = 0
            
      elif num2 == 5:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['comfort'] += 39

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))
            pygame.display.flip()
            pygame.time.wait(500)
        num2 = 0

      elif num2 == 6:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['per_passenger'] += 6

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))
            pygame.display.flip()
            pygame.time.wait(500)

        num2 = 0

      elif num2 == 7:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['per_passenger'] += 10

        else:
            broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
            w.blit(broke, (85, 720))   
            pygame.display.flip()
            pygame.time.wait(500)
        num2 = 0

      elif num2 == 8:
        up = upgrade_names[num2-1]
        if money >= upgrades[up]:
          money -= upgrades[up]
          for k in my_aircrafts:
            k = k["Name"]
            aircrafts[k]['safety'] += 19
            aircrafts[k]["speed"] -= 2

        else:
          broke = small_font.render("* Insufficient Funds - Try again when you're not broke *", True, red)
          w.blit(broke, (85, 720))
          pygame.display.flip()
          pygame.time.wait(500)
        num2 = 0

      pygame.display.flip()
      c.tick(30)

    while pilotbuy:
      advance_planes()
      draw_background()
      aircraft_opt = title_font.render("Aircraft Shop", True, white)
      w.blit(aircraft_opt, (225,0))
      r1 = pygame.Rect(0, 70, 190, 50)
      r2 = pygame.Rect(190,70, 190, 50)
      r3 = pygame.Rect(380, 70, 190, 50)
      r4 = pygame.Rect(570, 70, 180, 50)
      planes = font.render("Aircrafts", True, white)
      upgs = font.render("Upgrades", True, white)
      pils = font.render("Pilots", True, white)
      copils = font.render("Copilots", True, white)
      pygame.draw.rect(w, blue, r1)
      pygame.draw.rect(w, blue,r2 )
      pygame.draw.rect(w, blue, r3)
      pygame.draw.rect(w, blue, r4)
      pygame.draw.rect(w, white, r1, 3)
      pygame.draw.rect(w, white,r2, 3)
      pygame.draw.rect(w, white,r3, 3)
      pygame.draw.rect(w, white,r4, 3)
      w.blit(planes, (10, 70))
      w.blit(upgs, (200, 70))
      w.blit(pils, (390, 70))
      w.blit(copils, (580,70))
      quit = font.render("< Back", True, white)     
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
      pfp = pygame.image.load("user-icon.png")
      pfp = pygame.transform.scale(pfp, (75,75))
      star = pygame.image.load("star.png")
      star = pygame.transform.scale(star, (40,40))
      for i in range(len(pilots)):
        p = pygame.Rect(100, 150 + i * 125, 550, 100)
        a = mid_small_font.render(pilots[i]["Name"], True, white)
        price = font.render("$" + str(pilots[i]["Price"]), True, white)
        pygame.draw.rect(w,blue,p, 0, 16)
        w.blit(a, (225,150 + i * 125 ))
        w.blit(price, (500, 195 + i * 125))
        w.blit(pfp, (125, 160 + i * 125))

        for d in range(pilots[i]["Rating"]):
          w.blit(star, (225+d * 50, 195 + i * 125))

      pygame.display.flip()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          for i in range(len(pilots)):
            if x > 100 and x < 650 and y > 150 + i * 125 and y < 250 + i * 125:
              if money > pilots[i]["Price"]:
                
                my_pilots.append({
                  "Name" : pilots[i]["Name"],
                  "Level" : 1
                                  
                                  
                                  })
                money -= pilots[i]["Price"]
                pilots.remove(pilots[i])
                getname()
                rating = random.randint(1,5)
                price = int((rating * 10000) * random.randint(80, 100)/100)
                pilots.append({
                 "Name": first_name.capitalize() + " " +  surname.capitalize(),
                  "Price": price,
                 "Rating": rating

                 })
              else:
                broke = font.render("*Insufficient Funds*", True, white)
                p = pygame.Rect(100, 150 + i * 125, 550, 100)
                pygame.draw.rect(w, red,p, 0, 16)
                w.blit(broke,(190, int(175 + i * 125)))
                pygame.display.flip()
                pygame.time.wait(500)

          if r1.collidepoint(x,y):
            planebuy = True
            upgradebuy = False
            copilotbuy = False
            pilotbuy = False
          if r2.collidepoint(x,y):
            upgradebuy = True
            planebuy = False
            copilotbuy = False
            pilotbuy = False
          if r3.collidepoint(x,y):
            pilotbuy = True
            planebuy = False
            upgradebuy = False
            copilotbuy = False
          if r4.collidepoint(x,y):
            copilotbuy = True
            pilotbuy = False
            planebuy = False
            upgradebuy = False
          if (x > 50 and x < 200) and (y > 0 and y < 50):
            buying = False
            planebuy = False
            upgradebuy = False
            pilotbuy = False
            copilotbuy = False
      pygame.display.flip()
          
          

    while copilotbuy and not pilotbuy:
      advance_planes()
      draw_background()
      aircraft_opt = title_font.render("Aircraft Shop", True, white)
      w.blit(aircraft_opt, (225,0))
      r1 = pygame.Rect(0, 70, 190, 50)
      r2 = pygame.Rect(190,70, 190, 50)
      r3 = pygame.Rect(380, 70, 190, 50)
      r4 = pygame.Rect(570, 70, 180, 50)
      planes = font.render("Aircrafts", True, white)
      upgs = font.render("Upgrades", True, white)
      pils = font.render("Pilots", True, white)
      copils = font.render("Copilots", True, white)
      pygame.draw.rect(w, blue, r1)
      pygame.draw.rect(w, blue,r2 )
      pygame.draw.rect(w, blue, r3)
      pygame.draw.rect(w, blue, r4)
      pygame.draw.rect(w, white, r1, 3)
      pygame.draw.rect(w, white,r2, 3)
      pygame.draw.rect(w, white,r3, 3)
      pygame.draw.rect(w, white,r4, 3)
      w.blit(planes, (10, 70))
      w.blit(upgs, (200, 70))
      w.blit(pils, (390, 70))
      w.blit(copils, (580,70))
      quit = font.render("< Back", True, white)     
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
      pfp = pygame.image.load("user-icon.png")
      pfp = pygame.transform.scale(pfp, (75,75))
      star = pygame.image.load("star.png")
      star = pygame.transform.scale(star, (40,40))
      for i in range(len(copilots)):
        p = pygame.Rect(100, 150 + i * 125, 550, 100)
        a = mid_small_font.render(copilots[i]["Name"], True, white)
        price = font.render("$" + str(copilots[i]["Price"]), True, white)
        pygame.draw.rect(w,blue,p, 0, 16)
        w.blit(a, (225,150 + i * 125 ))
        w.blit(price, (500, 195 + i * 125))
        w.blit(pfp, (125, 160 + i * 125))

        for d in range(copilots[i]["Rating"]):
          w.blit(star, (225+d * 50, 195 + i * 125))

      pygame.display.flip()
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          for i in range(len(copilots)):
            if x > 100 and x < 650 and y > 150 + i * 125 and y < 250 + i * 125:
              if money > copilots[i]["Price"]:
                
                my_copilots.append({
                  "Name": copilots[i]["Name"],
                  "Level": 1
                                    
                                    })
                money -= copilots[i]["Price"]
                copilots.remove(copilots[i])
                getname()
                rating = random.randint(1,5)
                price = int((rating * 10000) * random.randint(80, 100)/100)
                copilots.append({
                 "Name": first_name.capitalize() + " " +  surname.capitalize(),
                  "Price": price,
                 "Rating": rating

                 })
              else:
                broke = font.render("*Insufficient Funds*", True, white)
                p = pygame.Rect(100, 150 + i * 125, 550, 100)
                pygame.draw.rect(w, red,p, 0, 16)
                w.blit(broke,(190, int(175 + i * 125)))
                pygame.display.flip()
                pygame.time.wait(500)

          if r1.collidepoint(x,y):
            planebuy = True
            upgradebuy = False
            copilotbuy = False
            pilotbuy = False
          if r2.collidepoint(x,y):
            upgradebuy = True
            planebuy = False
            copilotbuy = False
            pilotbuy = False
          if r3.collidepoint(x,y):
            pilotbuy = True
            planebuy = False
            upgradebuy = False
            copilotbuy = False
          if r4.collidepoint(x,y):
            copilotbuy = True
            pilotbuy = False
            planebuy = False
            upgradebuy = False
          if (x > 50 and x < 200) and (y > 0 and y < 50):
            buying = False
            planebuy = False
            upgradebuy = False
            pilotbuy = False
            copilotbuy = False
      pygame.display.flip()
        

def view_airline():
  viewing = True
  piloting = False
  global my_pilots
  global my_aircrafts
  while viewing:
    advance_planes()
    if len(my_pilots) >= len(my_aircrafts):
      for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]
    else:
      for i in range(len(my_pilots)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]

    if len(my_copilots) >= len(my_aircrafts):
      for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Copilot"] = my_copilots[i]
    else:
      for i in range(len(my_copilots)):
        my_aircrafts[i]["Copilot"] = my_copilots[i]
    view_pilot = pygame.Rect(100, 600, 550, 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          if view_pilot.collidepoint(x,y):
            viewing = False
            piloting = True
          for i in range(len(my_aircrafts)):
            if (x > 10 and x < 160) and (y > 0 and y < 50):
               viewing = False
            
    draw_background()
    airline = title_font.render("-------- World Air --------", True, white)
    cash = font.render(f"Money: ${money}", True, white)
    aircraft_title = font.render("----- Aircrafts In Use ----- ", True, white)
    for i in range(len(my_aircrafts)):
      a = small_font.render(f"{i+1}: {my_aircrafts[i]['Name']}", True, white)
      w.blit(a, (225, 350 + i * 40))
    w.blit(airline, (50, 50))
    w.blit(cash, (150, 150))
    quit = font.render("< Back", True, white)
    quit_box = pygame.Rect(10,0, 150, 50)
    p = font.render("View your Pilots/Copilots", True, white)
    
    
    pygame.draw.rect(w, blue, view_pilot, 0, 16)
    pygame.draw.rect(w,blue,quit_box, 0, 16) 
    w.blit(quit, (30, 0))
    w.blit(p, (150, 625))
    w.blit(aircraft_title, (150, 300))
  
    pygame.display.flip()
  while piloting:
    
    draw_background()
    advance_planes()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        if (x > 300 and x < 450) and (y > 0 and y < 50):
            piloting = False

    quit = font.render("< Back", True, white)     
    quit_box = pygame.Rect(300,0, 150, 50)
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (320, 0))
    pygame.draw.line(w, black, (375, 0), (375, 750), 3)
    pygame.draw.line(w, black, (0, 100), (750, 100), 3)
    p = title_font.render("Pilots", True, white)
    c = title_font.render("Copilots", True, white)
    w.blit(p, ( 100, 15))
    w.blit(c, (475, 15))
    pfp = pygame.image.load("user-icon.png")
    pfp = pygame.transform.scale(pfp, (60,60))
    for i in range(len(my_pilots)):
      t = pygame.Rect(30, 130 + i * 100, 300, 75)
      pygame.draw.rect(w, blue, t, 0, 16)
      name = small_font.render(my_pilots[i]["Name"], True, white)
      w.blit(name, (110, 140 + i * 100))
      level = rly_small_font.render("Level " + str(int(my_pilots[i]["Level"])), True, white)
      w.blit(level,(150, 180 + i * 100))
      w.blit(pfp, (45, 140 + i * 100)) 

    for i in range(len(my_copilots)):
      t = pygame.Rect(405, 130 + i * 100, 300, 75)
      pygame.draw.rect(w, blue, t, 0, 16)
      name = small_font.render(my_copilots[i]["Name"], True, white)
      w.blit(name, (485, 140 + i * 100))
      level = rly_small_font.render("Level " + str(int(my_copilots[i]["Level"])), True, white)
      w.blit(level,(525, 180 + i * 100))
      w.blit(pfp, (420, 140 + i * 100)) 

    pygame.draw.rect(w,blue,quit_box, 0, 16)  
    w.blit(quit, (320, 0)) 
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
    music = small_font.render("Music - Cosmic Love", True, white)
    leave_view = font.render("Press enter to leave", True, white)
    w.blit(credit_title, (100, 50))
    w.blit(test_title, (150, 150))
    
    w.blit(test1, (150, 250))
    w.blit(test2, (150, 275))
    w.blit(music, (150, 325))
    r = pygame.Rect(0,685, 750, 65)
    pygame.draw.rect(w,blue,r, 0, 16)
    w.blit(leave_view, (200, 700))
    pygame.display.flip()

def mapview():
  global money
  final_x = 0
  final_y = 0
  mapping = True
  w = pygame.display.set_mode([800,700])
 

  start_x = 500
  start_y = 500
  plane = pygame.image.load("2d airliner.png")
  plane = pygame.transform.scale(plane, (25,25))
  plane = pygame.transform.rotate(plane, 335)
  if len(my_pilots) >= len(my_aircrafts):
    for i in range(len(my_aircrafts)):
        my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]
  else:
    for i in range(len(my_pilots)):
      my_aircrafts[i]["Pilot"] = my_pilots[i]["Name"]

  if len(my_copilots) >= len(my_aircrafts):
    for i in range(len(my_aircrafts)):
      my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
  else:
    for i in range(len(my_copilots)):
      my_aircrafts[i]["Copilot"] = my_copilots[i]["Name"]
  while mapping:
    
    draw_background()
    quit_box = pygame.Rect(10,630, 150, 50)
    map = pygame.image.load("us_map.jpeg")
    map = pygame.transform.scale(map, (800,600))
    w.blit(map, (0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        if quit_box.collidepoint(x,y):
          mapping = False
        
    
    flightmap = title_font.render("Flight Map", True, black)
    quit = font.render("< Back", True, white)
    
    pygame.draw.rect(w,blue,quit_box, 0, 16)
    w.blit(quit, (30, 630))
    coin = pygame.image.load("coin.png")
    coin = pygame.transform.scale(coin, (40,40))
    w.blit(coin, (600,630))
    cash = small_font.render(str(money), True, black)
    w.blit(cash, (650, 640))
    pygame.draw.circle(w, black, (218,114), (1))
    cash_rect = pygame.Rect(590,630, 150,50)
    pygame.draw.rect(w,black,cash_rect, 3)
    for i in range(len(my_aircrafts)):
      
      w.blit(plane, (my_aircrafts[i]["x"], my_aircrafts[i]["y"] - 20))
      for d in range(len(domestic_destinations)):
        if my_aircrafts[i]["p2"] == domestic_destinations[d]["Name"]:
          
          destination = domestic_destinations[d]["Name"]
          final_x = domestic_destinations[d]["x"]
          final_y = domestic_destinations[d]["y"]
         
          
        if my_aircrafts[i]["p1"] == domestic_destinations[d]["Name"]:
          
          start_x = domestic_destinations[d]["x"]
          start_y = domestic_destinations[d]["y"]
      delta_x = final_x - start_x
      delta_y = final_y - start_y
      

    # Calculate the distance using the Pythagorean theorem
      distance = math.sqrt(delta_x**2 + delta_y**2)

    # Calculate velocity for both x and y axes
      name = my_aircrafts[i]["Name"] 
      speed = aircrafts[name]["speed"] * 80
      velocity_x = delta_x / speed
      velocity_y = delta_y / speed
      print(velocity_x)
      if my_aircrafts[i]["Pilot"] != "none" and my_aircrafts[i]["Copilot"] != "none":
        my_aircrafts[i]["x"] += velocity_x
        my_aircrafts[i]["y"] += velocity_y
      print(f"Current plane0 coordinates {my_aircrafts[0]['x']},{my_aircrafts[0]['y']}")
      print(velocity_y)
      

      x_range_low = final_x - 10
      x_range_high = final_x + 10
      y_range_low = final_y - 10
      y_range_high = final_y + 10
      if (my_aircrafts[i]["x"] >= x_range_low and my_aircrafts[i]["x"] <=  x_range_high) and (my_aircrafts[i]["y"] >= y_range_low and my_aircrafts[i]["y"] <=  y_range_high):
        p1 = random.choice(domestic_destinations)
        domestic_destinations.remove(p1)
        p2 = random.choice(domestic_destinations)
        
        domestic_destinations.append(p1)
        my_aircrafts[i]["p1"] = p1["Name"]
        my_aircrafts[i]["p2"] = p2["Name"]
        my_aircrafts[i]["x"] = p1["x"]
        my_aircrafts[i]["y"] = p1["y"]
        main_cost = 0
        name = my_aircrafts[i]["Name"]
        main_cost = aircrafts[name]['passengers'] * aircrafts[name]['per_passenger']
        comfort_rand = 3 * random.randint(0, aircrafts[name]['comfort'])
        main_cost += comfort_rand
        safety_rand = 2 * random.randint(0, aircrafts[name]['safety'])
        main_cost += safety_rand
        pilot = my_aircrafts[i]["Pilot"]
        for d in range(len(domestic_destinations)):
          if my_aircrafts[i]["p2"] == domestic_destinations[d]["Name"]:
          
            destination = domestic_destinations[d]["Name"]
            final_x = domestic_destinations[d]["x"]
            final_y = domestic_destinations[d]["y"]
         
          
          if my_aircrafts[i]["p1"] == domestic_destinations[d]["Name"]:
          
            start_x = domestic_destinations[d]["x"]
            start_y = domestic_destinations[d]["y"]
        if (start_x > final_x):
          plane = pygame.transform.rotate(plane,  180)
        if start_x < final_x:
          plane = pygame.transform.rotate(plane, 180)
        
        
        copilot = my_aircrafts[i]["Copilot"]
        for d in range(len(my_pilots)):
          
          if my_pilots[d]["Name"] == pilot:
            my_pilots[d]["Level"] += 0.6

        for d in range(len(my_copilots)):
          if my_copilots[d]["Name"] == copilot:
            my_copilots[d]["Level"] += 0.3

        landing,landing_pt = random.choice(list(landings.items()))
        main_cost += landing_pt
        #total = font.render("+ " + str(main_cost), True, green)
        money += main_cost
        #w````.blit(total, (375, 180 + i * 75))
        
        
    
    pygame.display.flip()
    c.tick(30)



   

    
running = True
music = pygame.mixer.Sound("cosmic-love.mp3")

while running:
  pygame.mixer.Sound.play(music)
  draw_background()
  title_font = pygame.font.SysFont("Playfair Display", 50)
  font = pygame.font.SysFont("Karla", 40)
  small_font = pygame.font.SysFont("Karla", 25)
  mid_small_font = pygame.font.SysFont("Karla", 33)
  rly_small_font = pygame.font.SysFont("Karla", 20)
  title = title_font.render("Airline Simulator", True, white)
  w.blit(title,(200, 50))
  opt1 = font.render("View Current Planes ", True, white)
  opt2 = font.render("Shop", True, white)
  opt3 = font.render("Airline Profile", True, white)
  opt4 = font.render("Sell Planes", True, white)
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

  w.blit(opt1, (200,190))
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
    mapview()
    w = pygame.display.set_mode([750,750])
    num = 0
  elif num == 2:
    buyplane()
    num = 0
  elif num == 3:
    view_airline()
    num = 0
  elif num == 4:
    sellplane()
    num = 0
  elif num == 5:
    credits()
    num = 0

  advance_planes()
  c.tick(60)
pygame.display.update()
   