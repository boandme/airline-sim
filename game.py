##### Airline Simulator ####
import random
import time


#### Aircrafts Dictionary ####
aircrafts = {
  "dc 3": {
    "cost": 1000,
    "passengers": 30,
    "per_passenger": 80,
    "comfort": 25,
    "safety": 40,
    "time": 2
    
  },
  "airbus a318": {
    "cost": 15000,
    "passengers": 122,
    "per_passenger": 110,
    "comfort": 45,
    "safety": 60,
    "time": 7
  },
  "airbus a319": {
    "cost": 35000,
    "passengers": 145,
    "per_passenger": 118,
    "comfort": 50,
    "safety": 60,
    "time": 7
    
  },
  "airbus a350": {
    "cost": 100000,
    "passengers": 325,
    "per_passenger": 115,
    "comfort": 50,
    "safety": 40,
    "time": 5
  },
  "airbus a340": {
    "cost": 175000,
    "passengers": 372,
    "per_passenger": 126,
    "comfort": 55, 
    "safety": 45,
    "time": 5
  },
  "boeing 777": {
    "cost": 300000,
    "passengers": 500,
    "per_passenger": 146,
    "comfort": 75,
    "safety": 70,
    "time": 3
  },
  "boeing 747": {
    "cost": 500000,
    "passengers": 537,
    "per_passenger": 175,
    "comfort": 75,
    "safety": 60, 
    "time": 4
  },
  "airbus a380": {
    "cost": 1000000,
    "passengers": 705,
    "per_passenger": 180,
    "comfort": 70,
    "safety": 60,
    "time": 2.5
    
  },
  "concorde": {
    "cost": 90000,
    "passengers":75,
    "per_passenger": 60,
    "comfort": 40,
    "safety": 20,
    "time": 0.5
  }


}

 



my_aircrafts = ["dc 3"]

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

##### Buy Plane Function #####
def buy_plane():
  global money
  print('Available Aircrafts: ')
  for plane in aircrafts:
    print(f'{plane} - ${aircrafts[plane]["cost"]}')
  plane_choice = input('Which plane would you like to buy? ')
  plane_choice = plane_choice.lower()
  if plane_choice in aircrafts and money >= aircrafts[plane_choice]['cost']:
    money -= aircrafts[plane_choice]['cost']
    my_aircrafts.append(plane_choice)
  else:
    print("Either that plane does not exist or you don't have enough money to buy it")

##### Disaster Function #####
def disaster():
  global money
  global main_cost
  global aircraft
  global aircrafts
  print("Disaster Strikes!")
  num = random.randint(1,2)
  if num == 1:
    num2 = random.randint(1,2)
    if num2 == 1:
      print("Your plane's engine overheated and exploded midway through the flight! Unfortunately, the plane therefore crashed and all passengers died")
      loss = random.randint(15000,100000)
      print(f"The victims' families sued your company and in total, you lost ${loss}")
      aircrafts[aircraft]["safety"] -= 4
      money -= loss
      main_cost = 0
    else:
      print("Your plane's cabin lost a high amount of pressure at the beggining of the flight and the nose of your aircraft broke apart.  Unfortunately, the plane therefore crashed and all passengers died")
      loss = random.randint(5000,20000)
      aircrafts[aircraft]["safety"] -= 2
      print(f"The victims' families sued your company and in total, you lost ${loss}")
      money -= loss
      main_cost = 0
  elif num == 2:
    opt2 = input("A terrible lightning storm is ahead of your flight path, but there might be a chance of making it through. Do you emergency land the plane in a nearby city(1) or take the risk(2)? - enter 1 or 2: ")
    if opt2 == "1":
      print("You successfully managed to perform an emergency landing and not damage the aircraft")
      print("However you did lose some money due to the passengers not being able to arrive at their destination timely.")
      loss2 = random.randint(1000,2000)
      main_cost -= loss2
    else:
      num3 = random.randint(1,10)
      if num3 < 3.5:
        print("You successfully navigated the storm and landed at your destination in time! Good Work! ")
        print("You also earned some extra money because of the tips from passengers who enjoyed your pilots' flying skills")
        tips = random.randint(100,1500)
        print(f"You earned an extra ${tips} in tips!")
      else:
        print("Sadly, your plane coudln't make it through the dangerous storm... should have played it safe ")
        print("Many passengers sued your airline for terrible flying skills and bad decision making. ")
        aircrafts[aircraft]["safety"] -= 5
        loss3 = random.randint(1000,2100)
        main_cost -= loss3
        

  print(f"Final Earnings: ${main_cost}")
  money += main_cost
        
        
        
##### Main Loop ####    
print('Welcome to Airline Simulator')
print("You can create and simulate an airline in this game")
name = input("Enter the name of your airline: ")
print("Your airline: " + name + " has been created!")
playing = True
while playing:
  print(f"""-------------------- Main Menu --------------------
                Total Cash: ${money}
                1. View Your Airline
                2. Buy Aircrafts
                3. Upgrades 
                4. Fly Plane
                5. Quit
    """)
  options = input("What would you like to do? ")
  if options == "2":
    buy_plane()
  elif options == "4":
    print()
    print("Here are your aircrafts: ")
    for plane in my_aircrafts:
      print(plane)
    while True:
      aircraft = input("Which Aircraft from your collection would you like to choose? ")
      
      if aircraft.lower in my_aircrafts:
        aircraft = aircraft.lower()
        break
      else:
        print('Please enter an aircraft you have in your collection')
        print()
      
  
    
    
    p1 = random.choice(destinations)
    destinations.remove(p1)
    p2 = random.choice(destinations)
    destinations.append(p1)
    hours = random.randint(1,12)
    minutes = random.randint(1,59)
    if minutes < 10:
      minutes = "0" + str(minutes)
    time_of_day = random.choice(["AM", "PM"])
    print()
    print(f"Your flight from {p1} to {p2} has been scheduled for {hours}:{minutes} {time_of_day}")
    input("Press enter to begin the boarding process")
    time.sleep(2)
    input("Press enter to takeoff")
    print("Your plane has taken off")
    print()
    print("Flying...")
    speed = aircrafts[aircraft]["time"]
    time.sleep(speed)
    print("Reached Cruising Altitude")
    time.sleep(speed)
    print("Starting Initial Descent")
    time.sleep(speed)
    print("Landed!")
    print()
    print()
    print("---------- Flight Summary --------")
    hours_spent = 0

    ##### Calculate flight duration #####
    if (p1 in west and p2 in west) or (p1 in east and p2 in east) or (p1 in mid and p2 in mid):
      hours_spent = random.randint(1,3)
    elif (p1 in west and p2 in mid) or (p2 in west and p1 in mid):
      hours_spent = random.randint(2,4)
    elif (p1 in east and p2 in mid) or (p2 in east and p1 in mid):
      hours_spent = random.randint(2,4)
    elif (p1 in west and p2 in east) or (p2 in west and p1 in east):
      hours_spent = random.randint(3,6)
    minutes_spent = random.randint(0,59)
    for i in range(hours_spent):
      hours += 1
      if hours > 12:
        hours = 1
        if time_of_day == "AM":
          time_of_day = "PM"
        elif time_of_day == "PM":
          time_of_day = "AM"
    minutes = int(minutes)
    for i in range(minutes_spent):
      minutes += 1
      if minutes > 59:
        minutes = 0
        hours += 1
    if minutes < 10:
      minutes = "0" + str(minutes)
    num4 = random.randint(1,6)
    main_cost = 0
    main_cost = aircrafts[aircraft]['passengers'] * aircrafts[aircraft]['per_passenger']


    #### Calculate Final Earning Totals ####
    print("----- Earning Totals -----")
    print(f"Tickets paid - ${main_cost}")
    comfort_rand = random.randint(0, aircrafts[aircraft]['comfort'])
    main_cost += comfort_rand
    safety_rand = random.randint(0, aircrafts[aircraft]['safety'])
    main_cost += safety_rand
    
    print(f"Extra earnings(comfort,safety,tips) - ${safety_rand + comfort_rand}")
    landing,landing_pt = random.choice(list(landings.items()))
    main_cost += landing_pt
    print(f"Landing Earnings: ${landing_pt}")
    
    money += main_cost
    if num4 == 6:
      disaster()
    else:
      print(f"Your flight landed at {hours}:{minutes} {time_of_day}")
      print(f"Total flight time: {hours_spent} hour(s) and {minutes_spent} minute(s)")
      print(f"The landing was {landing}")
      print()
      print(f"Final Earnings: ${main_cost}")
      
  

  

  

