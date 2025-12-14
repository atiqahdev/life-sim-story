print("Welcome to Life Sim Story")

energy = 50
mood = "neutral"

print("You wake up late for the day.")
print("1. Rush out immediately")
print("2. Stay in bed a little longer")

choice = input("Choose 1 or 2: ")

if choice == "1":
    energy -= 10
    mood = "stressed"
    print("You rush out. You're tired but on time.")
elif choice == "2":
    energy += 5
    mood = "calm"
    print("You rest a bit more. You feel calmer, but you're late.")
else:
    print("You freeze and do nothing.")

print("Energy:", energy)
print("Mood:", mood)
