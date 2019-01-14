# ========================= IMPORTS ============================

import random


# ====================== WELCOME SCREEN =========================
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


# ========================== CHARACTER CLASS =======================
def pick_class():
    print(" ")
    print("Choose your class")
    print(" ")
    global char_class
    char_class = input("Choose Mage, Giant, Knight, or Elf: ")
    if char_class.lower() == "mage" or char_class == "giant" or char_class == "knight" or char_class == "elf":
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


# ============================= CHARACTER STATS ==========================

stat_default = ("1) Health = ", "2) Damage = ", "3) Agility = ")  # Agility stat out of 10
mage_stats = (100, 22, 4)
giant_stats = (250, 12, 2)
knight_stats = (170, 17, 5)
elf_stats = (150, 20, 7)


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


# ======================= PRINT INVENTORY ============================
coins = 0
inventory_guide = ["1) Weapon Level: ", "2) Coin amount: ", "3) Damage booster: "]
inventory = ["Basic Attack Weapon", coins, "DmgBoost: 0"]


def inventory_print():
    print("-------------Inventory-------------")
    i = 0
    while i < len(inventory):
        print(inventory_guide[i] + str(inventory[i]))
        i += 1
    return 0


# ========================= MAP LOCATION CLASS =========================
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


# ======================= PRINTS MAP ======================
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


start_text()
pick_class()
inventory_print()
print_map()

# main game play loop
def path_choose():

    return 0

