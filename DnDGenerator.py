###https://online.anyflip.com/ofsj/cxmj/mobile/index.html#p=19###

# from tkinter import *
# from tkinter.messagebox import *
from self import self
import time
# class DnD:
#     def __init__(self,parent):
        #GUI
#         parent = parent
#         label = Label(parent, text="Welcome To The Dungeons and Dragons Character Generator")
#         label.grid(column=0,row=0)
#         start_button = Button(parent,text="Click Here To Begin",command=select_character_race)
#         start_button.grid(column=0,row=2)
#         quit_button = Button(parent,text="Exit",fg="red",command=parent.destroy)
#         quit_button.grid(column=1,row=2)
        
 ###Define Variables###
self.strength = 0
self.dexterity = 0
self.constitution = 0
self.intelligence = 0
self.wisdom = 0
self.charisma = 0
self.character_race = ""
self.character_class = ""
self.character_speed = 0
self.character_initiative = 0
self.character_armor_class = 0
self.character_hit_points = 0
self.character_size = ""
self.proficiency_bonus = 0
self.skills = []
self.character_alignment = ""
self.character_languages = []
self.copper_pieces = 0
self.silver_pieces = 0
self.emerald_pieces = 0
self.gold_pieces = 0
self.platinum_pieces = 0
self.proficiencies = []
self.draconic_ancestry = []
self.breath_weapon_range = []
self.cantrips = []
self.spells = []
self.experience = 0
self.level = 1
self.dwarf_choice = ""
self.dwarf_tool = ""
self.hp = 0





###Changes stats in relation to race selection###
def race_dragonborn():
    print("You have chosen to become a Dragonborn\n")
    self.character_race = "Dragonborn"
    f = open('dragonborn_description.txt','r')
    description = f.read()
    print(description)
    f.close()
    self.strength = 2
    self.charisma = 1
    self.speed = 30
    self.size = "Medium"
    self.character_languages.append("Common")
    self.character_languages.append("Draconic")
    self.draconic_ancestry_choice = input("What draconic ancestry type are you?: ")
    self.draconic_ancestry_choice = self.draconic_ancestry_choice.lower()
    ### Changes breath weapon list and range depending on the colour that is selected by user ###
    if self.draconic_ancestry_choice == "black":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Acid Breath Weapon")
        self.skills.append("Acid Damage Resistance")
        self.breath_weapon_range.append("5 by 30 ft. line (Dex. save)")
        
    elif self.draconic_ancestry_choice == "blue":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Lightning Breath Weapon")
        self.skills.append("Lightning Damage Resistance")
        self.breath_weapon_range.append("5 by 30 ft. line (Dex. save)")
        
    elif self.draconic_ancestry_choice == "brass":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Fire Breath Weapon")
        self.skills.append("Fire Damage Resistance")
        self.breath_weapon_range.append("5 by 30 ft. line (Dex. save)")
        
    elif self.draconic_ancestry_choice == "bronze":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Lightning Breath Weapon")
        self.skills.append("Lightning Damage Resistance")
        self.breath_weapon_range.append("5 by 30 ft. line (Dex. save)")
        
    elif self.draconic_ancestry_choice == "copper":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Acid Breath Weapon")
        self.skills.append("Acid Damage Resistance")
        self.breath_weapon_range.append("5 by 30 ft. line (Dex. save)")
        
    elif self.draconic_ancestry_choice == "gold":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Fire Breath Weapon")
        self.skills.append("Fire Damage Resistance")
        self.breath_weapon_range.append("15 ft. cone (Dex. save)")
        
    elif self.draconic_ancestry_choice == "green":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Poison Breath Weapon")
        self.skills.append("Poison Damage Resistance")
        self.breath_weapon_range.append("15 ft. cone (Con. save)")
        
        
    elif self.draconic_ancestry_choice == "red":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Fire Breath Weapon")
        self.skills.append("Fire Damage Resistance")
        self.breath_weapon_range.append("15 ft. cone (Dex. save)")
        
        
    elif self.draconic_ancestry_choice == "silver":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Cold Breath Weapon")
        self.skills.append("Cold Damage Resistance")
        self.breath_weapon_range.append("15 ft. cone (Con. save)")
        
    elif self.draconic_ancestry_choice == "white":
        self.draconic_ancestry_choice = self.draconic_ancestry_choice.capitalize()
        self.draconic_ancestry.append(self.draconic_ancestry_choice)
        self.skills.append("Cold Breath Weapon")
        self.skills.append("Cold Damage Resistance")
        self.breath_weapon_range.append("15 ft. cone (Con. save)")
        
    else:
        print("Please select the dragon colour not damage type")
        time.sleep(2)
        race_dragonborn()
        
    print("Your Strength Modifier is",self.strength,"\nYour Dexterity Modifier is",self.dexterity,"\nYour Constitution Modifier is",self.constitution,"\nYour Intelligence Modifier is",self.intelligence,"\nYour Wisdom Modifier is",self.wisdom,"\nYour Charisma Modifier is",self.charisma,"\nYou speak",self.character_languages,"\nYour draconic ancestry is",self.draconic_ancestry,"\nYou have proficiency in",self.proficiencies,"\nYour breath weapon range is",self.breath_weapon_range,"\nYour self.skills include",self.skills)
        


def race_dwarf():
    print("You have chosen to become a Dwarf\n")
    f = open('dwarf_description.txt','r')
    description = f.read()
    print(description)
    f.close()
    self.constitution += 2
    self.speed = 25
    self.size = "Medium"
    self.character_languages.append("Common")
    self.character_languages.append("Dwarvish")
    self.skills.append("Darkvision")
    self.skills.append("Dwarven Resilience")
    self.skills.append("Stonecunning")
    self.proficiencies.append("Battleaxe")
    self.proficiencies.append("Handaxe")
    self.proficiencies.append("Light Hammer")
    self.proficiencies.append("Warhammer")
    print("Dwarves gain profiency in an artisan tool of their choice. The options are smith's tools, brewer's supplies, or mason's tools")
    self.dwarf_tool = input("Which set of tools are you proficient in?: ")
    self.dwarf_tool = self.dwarf_tool.lower()
    if self.dwarf_tool == "smith":
        self.proficiencies.append("Smith's Tools")

    if self.dwarf_tool == "brewer":
        self.proficiencies.append("Brewer's Supplies")

    if self.dwarf_tool == "mason":
        self.proficiencies.append("Mason's Tools")

    print("There are 2 subraces pf dwarves: hill dwarves and mountain dwarves")
    race_dwarf_choice()
    

def race_dwarf_choice():
    f = open('hill_dwarf_description.txt')
    description = f.read()
    print(description)
    f.close()
    f = open('mountain_dwarf_description.txt')
    description = f.read()
    print(description)
    f.close()
    self.dwarf_choice = input("Please select either Hill Dwarf or Mountain Dwarf: ")
    self.dwarf_choice = self.dwarf_choice.lower()
    if self.dwarf_choice == "hill":
        self.character_race = "Hill Dwarf"
        self.wisdom += 1
        self.hp = self.hp + self.level
    elif self.dwarf_choice == "mountain":
        self.strength +=2
        self.proficiencies.append("Light Armour")
        self.proficiencies.append("Heavy Armour")
    else:
        print("Please select either hill or mountain")  
        race_dwarf_choice()    

    print("You are a",self.character_race,"\nYour Strength Modifier is",self.strength,"\nYour Dexterity Modifier is",self.dexterity,"\nYour Constitution Modifier is",self.constitution,"\nYour Intelligence Modifier is",self.intelligence,"\nYour Wisdom Modifier is",self.wisdom,"\nYour Charisma Modifier is",self.charisma,"\nYou speak",self.character_languages,"\nYou have proficiency in",self.proficiencies,"\nYour skills include",self.skills)
    



def race_elf():
    print("You have chosen to become a Elf\n")
    ###Loads character description from a file###
    f = open('elf_description.txt','r')
    description = f.read()
    print(description)
    f.close()
    ###Changes and adds self.skills and proficiencies###
    self.dexterity = 2
    self.speed = 30
    self.size = "Medium"
    self.character_languages.append("Common")
    self.character_languages.append("Elvish")
    self.skills.append("Dark Vision")
    self.skills.append("Trance")
    self.proficiencies.append("Perception")




    elf_type = str(input("\nThere are 3 subclasses of Elf to select from. They are High Elf, Wood Elf and the Drow.\nPlease select which subclass you would like to be: "))
    elf_type = elf_type.lower()

    if elf_type == "high elf" or elf_type == "he" or elf_type == "high":
        race_elf_high()
        
    elif elf_type == "wood elf" or elf_type == "we" or elf_type == "wood":
        race_elf_wood()
        
    elif elf_type == "drow" or elf_type == "dr":
        race_elf_drow()


def race_elf_high():
    print("You have chosen to become a High Elf\n")
    self.character_race = "High Elf"
    f = open('high_elf_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_elf_wood():
    print("You have chosen to become a Wood Elf\n")
    self.character_race = "Wood Elf"
    f = open('wood_elf_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_elf_drow():
    print("You have chosen to become a Drow\n")
    self.character_race = "Drow"
    f = open('drow_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_gnome():
    print("You have chosen to become a Gnome\n")
    self.character_race = "Gnome"
    f = open('gnome_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_half_elf():
    print("You have chosen to become a Half Elf\n")
    self.character_race = "Half Elf"
    f = open('half_elf_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_halfling():
    print("You have chosen to become a Halfling\n")
    self.character_race = "Halfling"
    f = open('halfling_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_half_orc():
    print("You have chosen to become a Half Orc\n")
    self.character_race = "Half Orc"
    f = open('half_orc_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_human():
    print("You have chosen to become a Human\n")
    self.character_race = "Human"
    f = open('human_description.txt','r')
    description = f.read()
    print(description)
    f.close()


def race_tiefling():
    print("You have chosen to become a Tiefling\n")
    self.character_race = "Tiefling"
    f = open('tiefling_description.txt','r')
    description = f.read()
    print(description)
    f.close()


###Runs the appropriate character race selection function###
def select_character_race():
    self.character_choice = input("What race would you like to be? \nDragonborn\nDwarf\nElf\nGnome\nHalf Elf\nHalfling\nHalf Orc\nHuman\nTiefling\nInput your choice here: ")


    self.character_choice = self.character_choice.lower()
    if self.character_choice == "dragonborn" or self.character_choice == "db":
        race_dragonborn()
        
    elif self.character_choice == "dwarf" or self.character_choice == "dw":
        race_dwarf()
        
    elif self.character_choice == "elf" or self.character_choice == "e":
        race_elf()
        
    elif self.character_choice == "Gnome" or self.character_choice == "gn":
        race_gnome()
        
    elif self.character_choice == "half elf" or self.character_choice == "he":
        race_half_elf()
        
        
    elif self.character_choice == "halfling" or self.character_choice == "ha":
        race_halfling()
        
        
    elif self.character_choice == "half orc" or self.character_choice == "ho":
        race_half_orc()
        
    elif self.character_choice == "human" or self.character_choice == "hu":
        race_human()
        
    elif self.character_choice == "tiefling" or self.character_choice == "ti":
        race_tiefling()
        

    


def class_barbarian():
    return


def class_bard():
    return


def class_cleric():
    return


def class_druid():
    return


def class_fighter():
    return


def class_monk():
    return


def class_paladin():
    return


def class_ranger():
    return


def class_rogue():
    return


def class_sorcerer():
    return


def class_warlock():
    return


def class_wizard():
    return


###Runs the appropriate character class selection function###
def select_character_class():
    return


# root = Tk()
# app = DnD(root)
# root.mainloop()
select_character_race()
    
    


    
    