player_health = 25
print("Health: ", player_health)
print("You're starving. Across the room you see a peanut.")
choice = input("Do you eat it? Y/N ")

if choice == "N":
    print("You stare at the unassuming peanut. It is unassuming, but you're alive.")
if choice == "Y":
    print("Why did you do that? You're allergic to peanuts! You Died.")
    player_health = 149
    print("Health: ", player_health)










