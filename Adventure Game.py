# ========================================== IMPORTS ======================================================

import random
import time
import sys

# ====================================== WELCOME SCREEN ========================================================
def start_text():
    print(" #_______________________________________________# ")
    print(" |------You have accessed the adventure app------| ")
    print(" |------------Play your own adventure------------| ")
    print(" |---------------Choose your class---------------| ")
    print(" #_______________________________________________# ")
    print(" ")
    print(" _    _        _                                 _             ___       _                     _                      ")
    print("| |  | |      | |                               | |           / _ \     | |                   | |                     ")
    print("| |  | |  ___ | |  ___  ___   _ __ ___    ___   | |_  ___    / /_\ \  __| |__   __ ___  _ __  | |_  _   _  _ __  ___  ")
    print("| |/\| | / _ \| | / __|/ _ \ | '_ ` _ \  / _ \  | __|/ _ \   |  _  | / _` |\ \ / // _ \| '_ \ | __|| | | || '__|/ _ \ ")
    print("\  /\  /|  __/| || (__| (_) || | | | | ||  __/  | |_| (_) |  | | | || (_| | \ V /|  __/| | | || |_ | |_| || |  |  __/ ")
    print(" \/  \/  \___||_| \___|\___/ |_| |_| |_| \___|   \__|\___/   \_| |_/ \__,_|  \_/  \___||_| |_| \__| \__,_||_|   \___| ")
    return 0


# =========================================== CHARACTER CLASS ==================================================

classes = ["mage", "giant", "knight", "elf"]


def pick_class():
    global char_class
    print(" ")
    print("Choose your class")
    print(" ")
    char_class = input("Choose Mage, Giant, Knight, or Elf: ")
    if char_class.lower() in classes:
        print("You selected the " + char_class + " class!")
    else:
        print("Sorry you did not type the class correctly. Make sure to type it exactly as it is shown")
        pick_class()
    print_stats()
    # allows the player to see stats and confirm the class
    global accept_class
    accept_class = input("Do you want to confirm the " + char_class + " class? Y/N")
    if accept_class.lower() == "y" or accept_class == "yes":
        print("You have confirmed the " + char_class + " class!")
    else:
        print(" ")
        pick_class()
    return 0


# ======================================= CHARACTER STATS ======================================================


# +++++++++++++++ Class Stat Variables ++++++++++
stat_default = ("1) Health = ", "2) Damage = ", "3) Agility = ")  # Agility stat out of 10
mage_stats = (100, 22, 4)
giant_stats = (250, 12, 2)
knight_stats = (170, 17, 5)
elf_stats = (150, 20, 7)


# +++++++++++++++ Prints Stats ++++++++++++++++
def print_stats():
    print("------------Stats------------")
    if char_class.lower() == "mage":
        i = 0
        while i < len(stat_default):
            print(str(stat_default[i]) + str(mage_stats[i]))
            i += 1
    elif char_class.lower() == "giant":
        i = 0
        while i < len(stat_default):
            print(str(stat_default[i]) + str(giant_stats[i]))
            i += 1
    elif char_class.lower() == "knight":
        i = 0
        while i < len(stat_default):
            print(str(stat_default[i]) + str(knight_stats[i]))
            i += 1
    elif char_class.lower() == "elf":
        i = 0
        while i < len(stat_default):
            print(str(stat_default[i]) + str(elf_stats[i]))
            i += 1
    return 0


# +++++++++++++ Defines Player Variables ++++++++++++
def player_variables():
    global class_stats
    global can_use_magic
    if char_class.lower() == "mage":
        class_stats = mage_stats
        can_use_magic = False
    if char_class.lower() == "giant":
        class_stats = giant_stats
        can_use_magic = False
    if char_class.lower() == "knight":
        class_stats = knight_stats
        can_use_magic = False
    if char_class.lower() == "elf":
        class_stats = elf_stats
        can_use_magic = False


# ========================================= PLAYER CLASS ==========================================================
class Player:
    def __init__(self, race, player_stats, magic):
        self.race = race
        self.player_stats = player_stats
        self.magic = magic


def generate_player_card():
    global main_character
    main_character = Player(char_class, class_stats, can_use_magic)


# ========================================== INVENTORY ===========================================================

# ++++++++++ Inventory Variables +++++++++++++
coins = 0
inventory_guide = ["1) Weapon Level: ", "2) Coin amount: ", "3) Damage booster: "]
inventory = ["Basic Attack Weapon", coins, "DmgBoost: 0"]


# +++++++++ Prints Inventory +++++++++
def inventory_print():
    print("-------------Inventory-------------")
    i = 0
    while i < len(inventory):
        print(inventory_guide[i] + str(inventory[i]))
        i += 1
    return 0


# =============================================Enemies===========================================================


# +++++++++++++++++++ Enemy Types ++++++++++++++++
enemy_types = ["Slime", "Goblin", "-Witch Sister-", "Mutant Rat", "-Mutant Bear-", "Sand Crawler", "Small Crab",
               "Large Crab", "Squid", "-Kraken-", "Castle Guard", "Archer Guard", "-Behemoth Dragon-"]


class Enemy:
    def __init__(self, type, health, damage_range, is_boss):
        self.type = type
        self.health = health
        self.damage = damage_range
        self.is_boss = is_boss


slime = Enemy(enemy_types[0], 20, (1, 10), False)
goblin = Enemy(enemy_types[1], 30, (3, 12), False)
witch_sister1 = Enemy(enemy_types[2], 45, (10, 25), True)
witch_sister2 = Enemy(enemy_types[2], 45, (10, 25), True)
witch_sister3 = Enemy(enemy_types[2], 45, (10, 25), True)
mutant_rat = Enemy(enemy_types[3], 35, (13, 15), False)
mutant_bear = Enemy(enemy_types[4], 60, (20, 30), True)
sand_crawler = Enemy(enemy_types[5], 35, (15, 30), False)


# ============================================== MAP ============================================================


# ++++++++++++++++++ Map Location Class +++++++++++++++
class Location:
    def __init__(self, map_name, true_name, grid_location, description, can_access, is_completed):
        self.map_name = map_name
        self.true_name = true_name
        self.grid_location = grid_location
        self.description = description
        self.can_access = can_access
        self.is_completed = is_completed


your_home = Location("      Your Home",
                     "Your Home",
                     "A1",
                     "A cozy spot to rest. You feel a sense of comfort around here.",
                     can_access=True,
                     is_completed=True)
grasslands = Location("     Grasslands",
                      "Grasslands",
                      "A2",
                      "Grassy hills as far as the eye can see... Seems like a good picnic spot.",
                      can_access=True,
                      is_completed=False)
mossy_ruins = Location("     Mossy Ruins",
                       "Mossy Ruins",
                       "A3",
                       "A clearing with large flat stones piled on each other... I get a weird feeling from this place",
                       can_access=True,
                       is_completed=False)
forbidden_cave = Location("Forbidden Cave",
                          "Forbidden Cave",
                          "A4",
                          "A dark entrance to a big cave... I wonder what's in there.",
                          can_access=True,
                          is_completed=False)
grasslands2 = Location("     Grasslands",
                       "Grasslands",
                       "B1",
                       "Grassy hills as far as the eye can see... Seems like a good picnic spot.",
                       can_access=True,
                       is_completed=False)
windy_desert = Location("   Windy Desert",
                        "Windy Dessert",
                        "B2",
                        "Grassy hills as far as the eye can see... Seems like a good picnic spot.",
                        can_access=True,
                        is_completed=False)
rocky_shore = Location("     Rocky Shore",
                       "Rocky Shore",
                       "B3",
                       "The waves crash against the giant boulders... The ocean ahead looks vast and unexplored",
                       can_access=True,
                       is_completed=False)
deep_below = Location("    Deep Below",
                      "Deep Below",
                      "B4",
                      "The water is filled with sea life and critters... I wonder if there are sharks in here",
                      can_access=True,
                      is_completed=False)
castle_wall = Location("    Castle Wall",
                       "Castle Wall",
                       "C1",
                       "A huge stone wall stand before you... Don't think I'm getting through this anytime soon.",
                       can_access=False,
                       is_completed=True)
castle_wall2 = Location("    Castle Wall",
                        "Castle Wall",
                        "C2",
                        "A huge stone wall stand before you... Don't think I'm getting through this anytime soon.",
                        can_access=False,
                        is_completed=True)
castle_entrance = Location(" Castle Entrance",
                           "Castle Entrance",
                           "C3",
                           "A big gated entrance with some tough guards in front of it... Man they look tough.",
                           can_access=True,
                           is_completed=False)
castle_wall3 = Location("    Castle Wall",
                        "Castle Wall",
                        "C4",
                        "A huge stone wall stand before you... Don't think I'm getting through this anytime soon.",
                        can_access=False,
                        is_completed=True)
unkown1 = Location("         uNkoWN",
                   "Dragon's Treasure",
                   "D1",
                   "A blinding light shines through the door... I can't see whats inside",
                   can_access=True,
                   is_completed=False)
unkown2 = Location("         UnkOwN",
                   "Empty Room",
                   "D2",
                   "A big empty room...",
                   can_access=True,
                   is_completed=False)
unkown3 = Location("         uNKowN",
                   "Grand Palace",
                   "D3",
                   "A huge empty dining hall with three chairs on a raised platform...Why is this place still guarded",
                   can_access=True,
                   is_completed=False)
unkown4 = Location("         UnKoWn",
                   "Seaside Balcony",
                   "D4",
                   "A single bench looks out to the deep blue ocean... This looks like a good place to rest.",
                   can_access=True,
                   is_completed=False)


# +++++++++++++++++++++ Prints Map +++++++++++++++++++++++++++
def print_map():
    print("\n------------------------------- M A P -----------------------------")
    print("###################################################################")
    print("#|      Your Home|     Grasslands|     Mossy Ruins|Forbidden Cave|#")
    print("#-----------------------------------------------------------------#")
    print("#|     Grasslands|   Windy Desert|     Rocky Shore|    Deep Below|#")
    print("#-----------------------------------------------------------------#")
    print("#|    Castle Wall|    Castle Wall| Castle Entrance|   Castle Wall|#")
    print("#-----------------------------------------------------------------#")
    print("#|" + unkown1.map_name + "|" + unkown2.map_name + "|" + unkown3.map_name + "|" + unkown4.map_name + "|#")
    print("#-----------------------------------------------------------------#")
    print("###################################################################")


# ================================================= SMOOTH PRINT ===================================================
def smooth_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10)
    return


def on_start():
    start_text()
    pick_class()
    player_variables()
    generate_player_card()
    return


def gameplay():
    print_map()
    inventory_print()



