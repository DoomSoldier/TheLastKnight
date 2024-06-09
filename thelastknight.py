# Final project for Code in place. 
# The Last Knight, is going to be a single knight that is still left alive, holding off the undead
# in hopes that the mages behind him can finish casting the spell to dispel all the necromancy in the area.

# After a certain amount of kills, you can earn upgrades and skills

# after an even more amount of kills stronger enemies will start to spawn forcing you to adapt playstyles, or if you are lucky brute force it

# What ablities would be good for the player as they get X amount of kills, Shield bash to stun and gain an extra turn
# Self healing? 
# upgrade damage, armor, or health max amount that is 
# still need to make the undead roll a number of attack and set it as the high and then roll the dice for it 
# 25 kills and a boss appears that is somewhat on par to a player npc? 
import random
import time

KNIGHT_HP = 20
KNIGHT_ATTACK = 4
KNIGHT_SPEED = 6
KNIGHT_BLOCK = 5
KNIGHT_ARMOR = 3
TOTAL_KILLS = 0
SOULS = 0


def main():
    global TOTAL_KILLS, SOULS, KNIGHT_HP
    TOTAL_KILLS = 0
    SOULS = 0
    KNIGHT_HP = 20

    intro()
    while True:
        user_input = input("You have but a moment before the first undead is on you, when you are ready, type begin, or type tutorial. ")
        print()
        lowercase_input = convert_to_lowercase(user_input)
        
        if lowercase_input == "begin":
            start_game()
        elif lowercase_input == "tutorial":
            tutorial()
            user_input = input("Are you ready? ")
            lowercase_input = convert_to_lowercase(user_input)
            if lowercase_input == "yes" or lowercase_input == "begin":
                start_game()
            else:
                while KNIGHT_HP > 0:
                    battle_erupts()    
                    undead_stats()
                    turn_based_combat()
                print("You have fallen, and the kingdom along with it.")
                print(f"The amount of undead you had slain, {TOTAL_KILLS}")
                if KNIGHT_HP == 0:
                    break
        else:
            print("Invalid input. Please type 'begin' or 'tutorial'. ")

def intro():
    print("(--------------------------------------------------------------------------------------)")
    print("You are the final knight remaining in the kingdom of Restora.")
    print("The undead have entered the outer castle walls in overwhelming numbers.")
    print("Your fellow knights were torn apart due to the sheer number of enemies...") 
    print("...but there is a spell on the main door of the hall.")
    print("Luckily for you it only allows a single undead creature to enter at a time...")
    time.sleep(3)
    print("... or a long drawn out fate that you know is coming. For this is, the last night.")
    print("(--------------------------------------------------------------------------------------)")
    print()

def start_game():
    print("These are your knight's stats, remember them well...")
    knight_stats()
    print("(--------------------------)")
    time.sleep(3)
    while KNIGHT_HP > 0:
        if TOTAL_KILLS > 0:
            print("Another undead squeezes through the doors rushing towards you.")
            undead_stats()
            turn_based_combat()
        battle_start()
        undead_stats()
        turn_based_combat()
    print("You have fallen, and the kingdom along with it.")
    print(f"The amount of undead you had slain, {TOTAL_KILLS}")

def battle_start():
    print("The battle begins")
    print("The undead pushes through the door and rushes at you.")

def battle_erupts():
    print("The front door of the main hall is forced open as you take too much time to prepare. ")
    print("The undead pushes through the door and rushes at you.")

def tutorial():
    print(f"This is your Health {KNIGHT_HP}, when it reaches zero the knight, along with the kingdom will fall")
    print(f"This is the Attack damage of your sword {KNIGHT_ATTACK}, bringing an enemy's health to zero is your goal")
    print(f"This is your Speed {KNIGHT_SPEED}, if it's higher than your enemy you act first")
    print(f"This is your Block {KNIGHT_BLOCK}, this will stop an enemy attack if your block is higher, if their attack is higher, it goes through at half damage")
    print(f"This is your Armor {KNIGHT_ARMOR}, if an enemy attacks this is the amount of damage your armor will block")

def knight_stats():
    print(f"Health: {KNIGHT_HP}")
    print(f"Attack: {KNIGHT_ATTACK}")
    print(f"Block: {KNIGHT_BLOCK}")
    print(f"Speed: {KNIGHT_SPEED}")
    print(f"Armor: {KNIGHT_ARMOR}")

def undead_stats():
    global undead_hp, undead_speed, undead_max_attack
    undead_hp = random.randint(1, 20)
    undead_speed = random.randint(1, 10)
    undead_max_attack = random.randint(1, 10)
    print(f"Health: {undead_hp}")
    print(f"Attack: {undead_max_attack}")
    print(f"Speed: {undead_speed}")

def turn_based_combat():
    global KNIGHT_HP, undead_hp, undead_speed
    knight_blocked = False
    while KNIGHT_HP > 0 and undead_hp > 0:
        if KNIGHT_SPEED >= undead_speed:
            knight_blocked = knight_turn()
            if undead_hp > 0 and not knight_blocked:
                undead_turn()
        if undead_speed > KNIGHT_SPEED:
            if not knight_blocked:
                undead_turn()
            if KNIGHT_HP > 0:
                knight_blocked = knight_turn()

def knight_turn():
    global KNIGHT_HP, undead_attack
    user_input = input("What do you wish to do? (attack/block) ")
    lowercase_input = convert_to_lowercase(user_input)
    if lowercase_input == "attack":
        attack()
        return False
    elif lowercase_input == "block":
        block()
        return True

def undead_turn():
    enemy_attack()

def attack():
    global undead_hp, TOTAL_KILLS, SOULS, KNIGHT_ATTACK
    damage = KNIGHT_ATTACK
    undead_hp -= damage
    if undead_hp <= 0:
        print("You have slain the undead before you.")
        print()
        TOTAL_KILLS += 1
        SOULS += 1
        if TOTAL_KILLS % 3 == 0:
            blessing_intro()
            blessing()
    elif undead_hp <= KNIGHT_ATTACK:
        print("The undead looks weak, and enough to be taken down in the next blow.")
        print()
    elif undead_hp <= undead_hp / 2:
        print("It seems injured but not enough.")
    else:
        print("It takes the blow but is still standing.") # This line is for more mechanics like a creature having innate armor similar to our knight

def enemy_attack():
    global KNIGHT_HP, undead_max_attack
    undead_attack = random.randint(1, undead_max_attack)
    print("The undead charges forward and attacks!")
    damage1 = undead_attack - KNIGHT_ARMOR
    if damage1 < 0:
        damage1 = 0
    KNIGHT_HP -= damage1
    KNIGHT_HP = max(KNIGHT_HP, 0)
    print(f"Your armor softens the blow, and you take {damage1} damage")
    print()
    print(f"Your remaining hp is {KNIGHT_HP}")
    print()

def block():
    global KNIGHT_HP, undead_attack, KNIGHT_ARMOR, KNIGHT_BLOCK
    undead_attack = random.randint(1, 10)
    print("The undead charges forward and attacks!")
    if undead_attack <= KNIGHT_BLOCK:
        print("Your shield blocks the attack, and the enemy does no damage")
    elif undead_attack > KNIGHT_BLOCK:
        damage = (undead_attack - KNIGHT_BLOCK - KNIGHT_ARMOR) / 2
        if damage < 0:
            damage = 0
        KNIGHT_HP -= damage
        KNIGHT_HP = max(KNIGHT_HP, 0)
        print(f"Your block and armor soften the blow, and you take {damage} damage")
    print(f"Your remaining hp is {KNIGHT_HP}")
    print()

def blessing_intro():
    print("*Magic starts to swirl in the air, a giant void-like portal appears as a entity steps through it and stares at you*")
    #time.sleep(5)
    print("(-------------------------------------------------------------------------------------------------------------------)")
    print("I am Xalphina, Goddess of Time, even if you don't remember me I remember you well Knight.")
    print("As you fight the onslaught of undead, I will return and claim their souls if you wish to give them to me")
    print("in exchange for blessings. If you want to accumulate more souls in exchange for a bigger blessing you may.")
    print("I will warn you, as the dark magic that takes a hold on this kingdom grows, the harder it will be for me to return.")
    print("(-------------------------------------------------------------------------------------------------------------------)")
    #time.sleep(10)
    print("*She waves her hand and a spectral door appears, snapping her fingers the door opens inwards revealing a lovely tavern*")
    print("*Within the same moment of seeing the tavern, you are inside sitting with Xalphina at a table with a scroll in your hand* ")
    print("Before you is a list of Blessings and tavern items costing souls (The Kills you have earned so far)")

def blessing():
    global KNIGHT_HP, KNIGHT_ATTACK, KNIGHT_ARMOR, KNIGHT_SPEED, KNIGHT_BLOCK, SOULS

    print(f"You have {SOULS} souls.")
    print("1. Hearty Ale (Full Heal) 1 coin.")
    print("2. Get your sword blessed (+1 Damage) for 2 souls.")
    print("3. Get your armor blessed (+1 Armor)  for 2 souls.")
    print("4. Make your body lighter (+1 Speed)  for 2 souls.")
    print("5. Get your shield blessed (+2 Block) for 2 souls.")
    user_input = input("Make a choice (1/2/3/4/5). ")

    if user_input == "1":
        KNIGHT_HP = 20
        SOULS -= 1
        print(f"You order an ale, Your health is now {KNIGHT_HP}, Xalphina takes 1 soul from you and throws 1 coin onto the table. Souls remaining: {SOULS}")
    elif user_input == "2":
        KNIGHT_ATTACK += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Sword. Your sword damage is now {KNIGHT_ATTACK}. Souls remaining: {SOULS}")
        print()
    elif user_input == "3":
        KNIGHT_ARMOR += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Armor. Your armor is now {KNIGHT_ARMOR}. Souls remaining: {SOULS}")
        print()
    elif user_input == "4":
        KNIGHT_SPEED += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Speed. Your speed is now {KNIGHT_SPEED}. Souls remaining: {SOULS}")
        print()
    elif user_input == "5":
        KNIGHT_BLOCK += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Block. Your block is now {KNIGHT_BLOCK}. Souls remaining: {SOULS}")
        print()
    else:
        print("You place the scroll on the table and take your souls with you as walk out spectral tavern back into the main hall.")

def blessing():
    global KNIGHT_HP, KNIGHT_ATTACK, KNIGHT_ARMOR, KNIGHT_SPEED, KNIGHT_BLOCK, SOULS

    print(f"You have {SOULS} souls.")
    print("1. Hearty Ale (Full Heal) 2 coin.")
    print("2. Get your sword blessed (+1 Damage) for 4 souls.")
    print("3. Get your armor blessed (+1 Armor)  for 4 souls.")
    print("4. Make your body lighter (+1 Speed)  for 4 souls.")
    print("5. Get your shield blessed (+2 Block) for 4 souls.")
    user_input = input("Make a choice (1/2/3/4/5). ")

    if user_input == "1":
        KNIGHT_HP = 20
        SOULS -= 1
        print(f"You order an ale, Your health is now {KNIGHT_HP}, Xalphina takes 2 soul from you and throws 2 coins onto the table. Souls remaining: {SOULS}")
    elif user_input == "2":
        KNIGHT_ATTACK += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Sword. Your sword damage is now {KNIGHT_ATTACK}. Souls remaining: {SOULS}")
        print()
    elif user_input == "3":
        KNIGHT_ARMOR += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Armor. Your armor is now {KNIGHT_ARMOR}. Souls remaining: {SOULS}")
        print()
    elif user_input == "4":
        KNIGHT_SPEED += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Speed. Your speed is now {KNIGHT_SPEED}. Souls remaining: {SOULS}")
        print()
    elif user_input == "5":
        KNIGHT_BLOCK += 1
        SOULS -= 2
        print(f"You have Xalphina bless your Block. Your block is now {KNIGHT_BLOCK}. Souls remaining: {SOULS}")
        print()
    else:
        print("You place the scroll on the table and take your souls with you as walk out spectral tavern back into the main hall.")

def convert_to_lowercase(user_input):
    return user_input.lower()

if __name__ == "__main__":
    main()