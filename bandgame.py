# BAND NAME GENERATOR

print("Welcome to the band name generator!")
print()

city = input("What city did you grow up in? ")
pet = input("What is your pet's name? ")

# Create band names
band_name1 = city + " " + pet
band_name2 = "The " + city + " " + pet + "s"
band_name3 = pet + " of " + city

print()
print("Here are your band names:")
print(band_name1)
print(band_name2)
print(band_name3)