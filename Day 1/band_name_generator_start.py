#1. Create a greeting for your program.
print("Hello outsider! Are you ready to name your band?!")
#2. Ask the user for the city that they grew up in.
city = input("First, tell me. What city did you grow up?\n")
#3. Ask the user for the name of a pet.
pet = input(f"Hm... {city}. That's an interesting name. Now, tell me your pet's name.\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = "Congrats! Here's your band name:\n" + city + " " + pet
#5. Make sure the input cursor shows on a new line:
print(band_name)
# Solution: https://replit.com/@appbrewery/band-name-generator-end