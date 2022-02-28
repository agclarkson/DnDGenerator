###https://online.anyflip.com/ofsj/cxmj/mobile/index.html#p=19###


from self import self
import webbrowser
webbrowser.open("https://online.anyflip.com/ofsj/cxmj/mobile/index.html#p=19")

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




###Changes stats in relation to race selection###
def race_dragonborn():
    print("You have chosen to become a Dragonborn")

def race_dwarf():
    print("You have chosen to become a Dwarf")
    
    
def race_elf():
    print("You have chosen to become a Elf\n")
    ###Loads character description from a file###
    f = open('elf_description.txt','r')
    elf_description = f.read()
    print(elf_description)
    f.close()
    ###Changes and adds skills and proficiencies###
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
    print("You have chosen to become a High Elf")
    

def race_elf_wood():
    print("You have chosen to become a Wood Elf")
    
    
def race_elf_drow():
    print("You have chosen to become a Drow")
    
    
def race_gnome():
    print("You have chosen to become a Gnome")
    
    
def race_half_elf():
    print("You have chosen to become a Half Elf")
    
    
def race_halfling():
    print("You have chosen to become a Halfling")
    
    
def race_half_orc():
    print("You have chosen to become a Half Orc")
    
    
def human():
    print("You have chosen to become a Human")


def tiefling():
    print("You have chosen to become a Tiefling")
    

###Runs the appropriate character race selection function###
def select_character_race():
    character_choice = str(input("What race would you like to be? \nDragonborn\nDwarf\nElf\nGnome\nHalf Elf\nHalfling\nHalf Orc\nHuman\nTiefling\nInput your choice here: "))
    character_choice = character_choice.lower()
    if character_choice == "dragonborn" or character_choice == "db":
        race_dragonborn()
        
    elif character_choice == "dwarf" or character_choice == "dw":
        race_dwarf()
        
    elif character_choice == "elf" or character_choice == "e":
        race_elf()
        
    elif character_choice == "Gnome" or character_choice == "gn":
        race_gnome()
        
    elif character_choice == "half elf" or character_choice == "he":
        race_half_elf()
        
        
    elif character_choice == "halfling" or character_choice == "ha":
        race_halfling()
        
        
    elif character_choice == "half orc" or character_choice == "ho":
        race_half_orc()
        
    elif character_choice == "human" or character_choice == "hu":
        race_human()
        
    elif character_choice == "tiefling" or character_choice == "ti":
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
    
select_character_race()
    
    


    
    