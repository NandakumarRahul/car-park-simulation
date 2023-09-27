import CarPark

print("*******WLECOME TO CAR PARK!*******")

while True:

  print("-------------MAIN MENU---------------- ")
  print("1.Enter car park.")
  print("2.Exit car park.")
  print("3.Enquire about car park.")
  print("4.Quit")

  try:
    num = int(input("Enter your choice : "))
    if num == 1:
      vehicle_id = input("Enter vehicle ID : ")
      vehicle_id,space_id,entry_time,available_spaces= CarPark.car_park.enter(vehicle_id)
      print(f"Vehicle {vehicle_id} has entered the car park.")
      print(f"Parking space ID: {space_id}")
      print(f"Entry time : {entry_time}")
      print(f"Remaining available space : {available_spaces}")
    if num == 2:
      vehicle_id = input("Enter vehicle ID :")
      vehicle_id, space_id,entry_time,exit_time,fare,available_spaces=CarPark.car_park.exit(vehicle_id)
      print(f"Vehicle {vehicle_id} has exited the car park.")
      print(f"Parking space ID:{space_id}")
      print(f"Entry time :{entry_time} ")
      print(f"Exit time : {exit_time}")
      print(f"Fare: £{fare}\n")
      print(f"Remaining available space : {available_spaces}")
    if num == 3:
      vehicle_id = input("Enter vehicle ID :")
      vehicle_id, space_id, entry_time=CarPark.car_park.enquire(vehicle_id)
      print(f"Vehicle {vehicle_id} is parked in space ID {space_id} ")
      print(f"Entry time : {entry_time}")
    if num == 4:
      break
  except ValueError as e:
    print("Enter a valid choice!")
1