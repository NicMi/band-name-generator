constant = True
while constant:
  print("Welcome to the band name generator!")
  def band_name(city,pet):
    print(f"Your band name should be: {city} {pet}")
  city_name = input("Tell me the city where you grew up in: ")
  pet_name = input("Tell me the name of your pet: ")
  band_name(city = city_name, pet = pet_name)
  should_continue = input("Do you want to continue? type 'y' for yes or anything to go out: ")
  if should_continue != "y":
    break
  # constant = False