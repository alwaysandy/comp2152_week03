#Lab03

# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# Dice option created with list() and range()
diceOptions = list(range(1, 7))

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 
print("Available Weapons:")
for i, weapon in enumerate(weapons):
    print(f"{i + 1}. {weapon}")
print()

while True:
    combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
    if(combatStrength < 1 or combatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        break

while True:
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
    if (mCombatStrength  < 1 or mCombatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        break
    
for j in range(1, 21, 2):
    if j == 11:
        print("Battle Truce declared in Round 11. Game over!")
        break
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    print(f"Round {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected: {weapons[heroRoll - 1]}, Monster selected: {weapons[monsterRoll - 1]}")
    
    combatStrength += heroRoll
    mCombatStrength += monsterRoll
    print(f"Hero Total Strenght: {combatStrength}, Monster Total Strength: {mCombatStrength}")

    if combatStrength > mCombatStrength:
        print("Hero wins the round!")
    elif mCombatStrength > combatStrength:
        print("Monster wins the round!")
    else:
        print("Battle was tied!")
    print()