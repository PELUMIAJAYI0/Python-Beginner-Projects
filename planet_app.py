planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input("Please input the name of the planet (use a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than "+ user_planet)
print(planets[0:planet_index])
print("Here are the planets closer than " + user_planet)
print(planets[planet_index + 1:])