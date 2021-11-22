# Python classes - text based adventure game
# Michael Zhu
# Nov 10th, 2021
# CS30
# Ms.Cotcher

# Importing all of the modules
import mapping
import character
import inventory
import sys
import enemy
import time

""" This is a game where you are an adventurer trying to escape
a wasteland with a locked door, navigate through the biome with four
movements, encounter and defeat enemies, collect resources, and try to find
the key to the door. Now comes with mulitple modules,two inventories,
a map showing potential locations,along with descriptions for potential
characters and locations in the main menu"""
""" These variables set up the catagories for actions and the coordinate
system, the dictionaries holding your two inventories by executing the
inventory module, along with variables for combat"""

x = 2
y = 1

health = 0
max_health = 0
attack = 0
focus = 0
heal = 5
critical_stack = 0
perfect_stack = 0

enemy_hp = 0
enemy_att = 0
e_stat = []

choice = 0
key = 0
key_check = 1
ssd = 0

point_cleared_1 = 1
point_cleared_2 = 1
point_cleared_3 = 1
point_cleared_4 = 1

Mapp = [["end", "enemy", "enemy", "key"],
        ["supply", "nothing", "nothing", "enemy"],
        ["nothing", "start", "supply", "nothing"],
        ["enemy", "supply", "nothing", "enemy"]]

# The options for menus
general_action = ["explore", "character selection"]
explore = ["forward", "backward", "left", "right", "inventory", "quit"]
combat_menu = ["attack", "dodge", "defend", "inventory", "quit"]

# exploration inventory
exploring_bag = {}
exploring_bag = inventory.explore_inv(exploring_bag)

# Combat inventory
combat_pouch = {}
combat_pouch = inventory.combat_inv(combat_pouch)

# Potential characters and their descriptions
characters = ["beserker", "healer", "mage", "tank"]


def combat():
    global enemy_hp
    global health
    global perfect_stack
    global critical_stack
    global focus
    while enemy_hp > 0:
        if health < 1:
            break
        print("\nYou can do the following actions:\n")
        for i in combat_menu:
            print(i)
        combat_input = input("\nwhich one do you choose?\n")
        if combat_input.lower() == combat_menu[0]:
            if critical_stack < 1:
                enemy_hp -= attack
                health -= enemy_att
                perfect_stack += 1
                print("\nyou hit the enemy good job\n")
            else:
                enemy_hp -= attack * 2
                health -= enemy_att / 2
                print("\nthats a lot of damage\n")
                critical_stack -= 1
            if perfect_stack == 10:
                print("\nYou committed nuclear blast on the enemy\n")
                enemy_hp -= attack * 10
        elif combat_input.lower() == combat_menu[1]:
            if focus > 5:
                print("\nYou dodged the enemy's attack and regained some of " +
                      "your posture\n")
                if health < max_health:
                    health += 5
                perfect_stack += 1
                focus -= 1
                if critical_stack < 2:
                    critical_stack += 1
            else:
                print(
                    "\nYou didn't focus enough and got clapped by the " +
                    "enemy's fast hands\n")
                health -= enemy_att * 3
                focus += 1
                perfect_stack += 5
        elif combat_input.lower() == combat_menu[2]:
            health -= enemy_att / 2
            focus += 1
            print("\nyou blocked the enemy's hit and took half damage, " +
                  "regained one focus\n")
        elif combat_input.lower() == combat_menu[3]:
            print("\nstill in development\n")
        elif combat_input.lower() == combat_menu[4]:
            break
        time.sleep(1)
        print(f"\nYou have {health} health, your enemy has {enemy_hp} health")


# Print out to verify that all modules are imported successfully
if "inventory" in sys.modules and "character" in sys.modules and \
        "inventory" in sys.modules:
    print("Successfully imported character, inventory and mapping modules")
time.sleep(2)
""" The while loop that makes sure the general menu is running constantly until
quit is inputted, during this you can either select explore or combat"""
while True:
    print("\nyou can do the following catagory of actions:")
    for i in general_action:
        print(i)
    print("side note: you can type quit to quit anytime\n")
    time.sleep(1)
    cata_input = input("\nwhich one do you choose?\n")

    # The section is what happens when you select explore, it constantly
    # loops and ask for input until you type quit which will return to the
    # general menu
    if cata_input.lower() == general_action[0]:
        mapping.Map()
        time.sleep(1)
        if choice > 0:
            print(f"you are playing as {characters[choice-1]}")
            print(
                f"You have {health} health, {attack} damage, and {focus} focus"
            )
            time.sleep(1)
        while True:
            if choice == 0:
                print("choose a character first!\n")
                break
            if health < 1:
                print("\nYou have died of death\n")
                break
            print("\nu can go either")
            for option in explore:
                print(option)
            time.sleep(1)
            direction_input = input("\nwhich one do you choose?\n")

            # The coordinate system
            if direction_input.lower() in explore:
                y = mapping.loca_reset(y)
                x = mapping.loca_reset(x)
                coord_change = direction_input.lower()
                if coord_change == explore[0]:
                    x -= 1
                elif coord_change == explore[1]:
                    x += 1
                elif coord_change == explore[2]:
                    y -= 1
                elif coord_change == explore[3]:
                    y += 1

                time.sleep(1)
                mapping.MapReaction(x, y, Mapp)
                time.sleep(1)

                if x == 3 and y == 0:
                    if point_cleared_1 > 0:
                        p = enemy.assasin()
                        enemy_hp = p.assign_val()
                        enemy_att = p.assign_val_2()
                        combat()
                        if enemy_hp < 1:
                            print(f"congrates you beat {p.name}")
                            point_cleared_1 -= 1
                    else:
                        time.sleep(1)
                        print(f"\nthe {p.name} lays on the ground dead")
                        time.sleep(1)

                if x == 0 and y == 1:
                    if point_cleared_2 > 0:
                        p = enemy.theif()
                        enemy_hp = p.assign_val()
                        enemy_att = p.assign_val_2()
                        combat()
                        if enemy_hp < 1:
                            print(f"congrates you beat {p.name}")
                            point_cleared_2 -= 1
                    else:
                        time.sleep(1)
                        print(
                            f"\n{p.name} couldn't keep his most precious " +
                             "possession from being stolen: his life\n")
                        time.sleep(1)

                if x == 3 and y == 3:
                    if point_cleared_3 > 0:
                        p = enemy.swat_soul()
                        enemy_hp = p.assign_val()
                        enemy_att = p.assign_val_2()
                        combat()
                        if enemy_hp < 1:
                            print(f"congrates you beat {p.name}")
                            point_cleared_3 -= 1
                    else:
                        time.sleep(1)
                        print(
                            f"\nthe armor of {p.name} is broken on the " +
                             "ground just like his skull\n")
                        time.sleep(1)

                if x == 0 and y == 2 or x == 1 and y == 3:
                    if point_cleared_4 > 0:
                        p = enemy.emperor()
                        enemy_hp = p.assign_val()
                        enemy_att = p.assign_val_2()
                        combat()
                        if enemy_hp < 1:
                            print(f"congrates you beat {p.name}")
                            point_cleared_4 -= 1
                    else:
                        time.sleep(1)
                        print(
                            f"\nthe great {p.name} has fallen, he doesn't " +
                             "look so intiminating after all\n")
                        time.sleep(1)

                # Displays your exploration inventory
                elif direction_input.lower() == explore[4]:
                    for item in exploring_bag:
                        print(f"^{item}^:")
                        for thing in exploring_bag[item]:
                            print(f"{thing} - {exploring_bag[item][thing]}")
                        print("\n")
                elif direction_input.lower() == explore[5]:
                    print("going back to the main menu\n")
                    break

            else:
                print("\ninvalid action!")

    # prints descriptions of characters as statements if inputted characters
    elif cata_input.lower() == general_action[1]:
        print("\nYou can choose the following characters:\n")
        for i in characters:
            print(i)
        time.sleep(1)
        character_input = input("\nwhich one do you choose?\n")

        # Selecting characters and their attributes
        if character_input.lower() == characters[0]:
            print(f"you have chosen {characters[0]}")
            time.sleep(1)
            choice = 1
            ssd = character.beserker(health, attack, focus)
            health = ssd.hp
            max_health = ssd.hp
            attack = ssd.damage
            focus = ssd.focus
        elif character_input.lower() == characters[1]:
            print(f"you have chosen {characters[1]}")
            time.sleep(1)
            choice = 2
            ssd = character.healer(health, attack, focus)
            health = ssd.hp
            max_health = ssd.hp
            attack = ssd.damage
            focus = ssd.focus
        elif character_input.lower() == characters[2]:
            print(f"you have chosen {characters[2]}")
            time.sleep(1)
            choice = 3
            ssd = character.mage(health, attack, focus)
            health = ssd.hp
            max_health = ssd.hp
            attack = ssd.damage
            focus = ssd.focus
        elif character_input.lower() == characters[3]:
            print(f"you have chosen {characters[3]}")
            time.sleep(1)
            choice = 4
            ssd = character.tank(health, attack, focus)
            health = ssd.hp
            max_health = ssd.hp
            attack = ssd.damage
            focus = ssd.focus
        else:
            print("invalid action!")
            time.sleep(1)

    # Breaks the loop when inputted quit and accepts wrong inputs
    elif cata_input.lower() == "quit":
        break
    else:
        print("invalid action!")
        time.sleep(1)

    if health < 1:
        print("\nYou failed!\n")
        break
