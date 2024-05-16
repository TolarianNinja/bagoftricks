# Purpose:      Script to download images from Scryfall by set and use filenames
#               compatible with MagicAlbum
# Author:       TolarianNinja / Alex Hartshorn using Scrython
#               (Scryfall for Python lib)
# Scrython:     https://github.com/NandaScott/Scrython/
# MagicAlbum:   https://www.slightlymagic.net/wiki/Magic_Album

import scrython, time, shutil, requests, os


# Set Code
set_code = [ "unf",
             "clb",
             "snc",
             "ncc",
             "phed",
             "gdy",
             "pw22",
             "slx",
             "pl22",
             "nec",
             "cc2",
             "cc1",
             "dbl",
             "p22",
             "voc",
             "mic",
             "afc",
             "afr",
             "mh2",
             "c21",
             "khc",
             "znc",
             "zne",
             "slu",
             "sld",
             "cmr",
             "jgp",
             "stx",
             "ss3",
             "iko",
             "prw2",
             "prwk",
             "gdy",
             "gn2",
             "sta",
             "tsr",
             "cmb1",
             "2x2",
             "neo",
             "plist",
             "dmu",
             "dmc",
             "bro",
             "brc",
             "brr",
             "khm",
             "lea",
             "leb",
             "2ed",
             "fem",
             "bot",
             "arn",
             "atq",
             "leg",
             "drk",
             "ice",
             "hml",
             "all",
             "mb1",
             "one",
             "j22",
             "dmc",
             "dmr",
             "p30a",
             "uplist",
             "onc",
             "mh2",
             "h1r",
             "pw21",
             "pw22",
             "und",
             "war",
             "mom",
             "mat",
             "mul",
             "moc",
             "slc",
             "slx",
             "cmm",
             "woe",
             "woc",
             "wot",
             "ltr",
             "ltc",
             "rav",
             "psdc",
             "ps14",
             "ps15",
             "ps16",
             "ps17",
             "ps18",
             "ps19",
             "who",
             "lci",
             "lcc",
             "rvr",
             "rex",
             "3ed",
             "40k"
             ]

# Set Name
set_name = [ "Unfinity",
             "Commander Legends - Battle for Baldur's Gate",
             "Streets of New Capenna",
             "New Capenna Commander",
             "Heads I Win, Tails You Lose",
             "Game Day Promos",
             "Wizards Play Network 2022",
             "Universes Within",
             "Year of the Tiger 2022",
             "Kamigawa - Neon Dynasty Commander",
             "Commander Collection - Black",
             "Commander Collection - Green",
             "Innistrad - Double Feature",
             "Judge Gift Cards 2022",
             "Innistrad - Crimson Vow Commander",
             "Innistrad - Midnight Hunt Commander",
             "Forgotten Realms Commander",
             "Adventures in the Forgotten Realms",
             "Modern Horizons 2",
             "Commander 2021",
             "Kaldheim Commander",
             "Zendikar Rising Commander",
             "Zendikar Rising Expeditions",
             "Secret Lair - Ultimate Edition",
             "Secret Lair Drops",
             "Commander Legends",
             "Judge Gift Cards",
             "Strixhaven - School of Mages",
             "Signature Spellbook - Chandra",
             "Ikoria - Lair of Behemoths",
             "Ravnica Weekend",
             "Ravnica Weekend",
             "Game Day Promos",
             "Game Night 2019",
             "Strixhaven - Mystical Archive",
             "Time Spiral Remastered",
             "Mystery Booster",
             "Double Masters 2022",
             "Kamigawa - Neon Dynasty",
             "The List",
             "Dominaria United",
             "Dominaria United Commander",
             "The Brothers War",
             "The Brothers War Commander",
             "The Brothers War Retro Artifacts",
             "Kaldheim",
             "Limited Edition Alpha",
             "Limited Edition Beta",
             "Unlimited Edition",
             "Fallen Empires",
             "Transformers",
             "Arabian Nights",
             "Antiquities",
             "Legends",
             "The Dark",
             "Ice Age",
             "Homelands",
             "Alliances",
             "Mystery Booster",
             "Phyrexia All Will Be One",
             "Jumpstart 2022",
             "Dominaria United Commander",
             "Dominaria Remastered",
             "30th Anniversary Play Promos",
             "The List",
             "Phyrexia All Will Be One Commander",
             "Modern Horizons 2",
             "Modern Horizons Timeshifts",
             "Gateway",
             "Magic Game Day",
             "Unsanctioned",
             "War of the Spark",
             "March of the Machine",
             "March of the Machine The Aftermath",
             "Multiverse Legends",
             "March of the Machine Commander",
             "Secret Lair 30th Anniv Countdown Kit",
             "Universes Within",
             "Commander Masters",
             "Wilds of Eldraine",
             "Wilds of Eldraine Commander",
             "Enchanting Tales",
             "Lord of the Rings",
             "Lord of the Rings Commander",
             "Ravnica - City of Guilds",
             "Convention",
             "Convention",
             "Convention",
             "Convention",
             "Convention",
             "Convention",
             "Convention",
             "Doctor Who Commander",
             "The Lost Caverns of Ixalan",
             "The Lost Caverns of Ixalan Commander",
             "Ravnica Remastered",
             "Jurassic World Collection",
             "3rd Revised Edition",
             "Warhammer 40000 Commander"
             ]

# Boundaries and Versions
# Remove zeros when adding information for next set
boundaries = [ [ 245, 277, 287, 496, 528, 540 ], # Unfinity
               [ 362, 375, 471, 553, 646, 935, 940 ], # Commander Legends - Battle for Baldur's Gate
               [ 282, 296, 360, 361, 406, 441, 450, 461, 468, 600 ], # Streets of New Capenna
               [ 94, 186, 191, 448 ], # New Capenna Commander
               [ 0 ], # Heads I Win, Tails You Lose
               [ 0 ], # Game Day Promos
               [ 0 ], # Wizards Play Network 2022
               [ 0 ], # Universes Within
               [ 0 ], # Year of the Tiger 2022
               [ 39, 77, 79, 181  ], # Neon Dynasty Commander
               [ 0 ], # Commander Collection - Black
               [ 0 ], # Commander Collection - Green
               [ 171, 172, 199, 200, 261, 262, 455, 456, 486, 487, 530, 531, 536 ], # Innistrad - Double Feature
               [ 0 ], # Judge Gift Cards 2022
               [ 39, 77, 189 ], # Innistrad - Crimson Vow Commander
               [ 39, 77, 188 ], # Innistrad - Midnight Hunt Commander
               [ 274, 330, 332 ], # Forgotten Realms Commander
               [ 282, 299, 359, 396, 403 ], # Adventures in the Forgotten Realms
               [ 304, 327, 381, 442, 491, 493 ], # Modern Horizons 2
               [ 328, 408, 411 ], # Commander 2021
               [ 0, 140 ], # Kaldheim Commander
               [ 7, 9, 145 ], # Zendikar Rising Commander
               [ 0, 45 ], # Zendikar Rising Expeditions
               [ 0, 99 ], # Secret Lair - Ultimate Edition
               [ 0, 23599 ], # Secret Lair Drops
               [ 30,31,43,44,248,249,313,315,325,326,350,351,355,356,357,358,377,378,383,384,434,435,463,465,467,468,479,480,490,491,497,498,512,514,615,721,724 ], # Commander Legends
               [ 0 ], # Judge Gift Cards
               [ 276,285,376,383 ], # Strixhaven
               [ 0 ], # Signature Spellbook: Chandra
               [ 276, 314, 364, 365, 370, 389 ], # Ikoria
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 64,127 ],
               [ 0 ],
               [ 0 ],
               [ 333, 413, 573, 578, 580 ], # Double Masters 2022
               [ 303, 307, 309, 406, 417, 429, 430, 431, 432, 433, 506, 513 ], # Kamigawa - Neon Dynasty
               [ 0 ], # The List
               [ 287, 328, 369, 371, 372, 375, 376, 377, 383, 428, 435 ], # Dominaria United
               [  ], # Dominaria United Commander
               [ 293, 301, 378, 400 ], # Brother's War
               [ 41, 68, 900 ], # Brother's War Commander
               [ 64, 129 ], # Brother's War Retro Artifacts
               [ 287, 299, 334, 374, 400 ], # Kaldheim
               [ 0 ], # Alpha
               [ 0 ], # Beta
               [ 0 ], # Unlimited
               [ 0 ], # Fallen Empires
               [ 16, 30 ], # Transformers
               [ 0 ], # Arabian Nights
               [ 0 ], # Antiquities
               [ 0 ], # Legends
               [ 0 ], # The Dark
               [ 0 ], # Ice Age
               [ 0 ], # Homelands
               [ 0 ], # Alliances
               [ 0 ], # Mystery Booster
               [ 277, 285, 335, 345, 370, 375, 404, 417, 480 ], # Phyrexia All Will Be One
               [ 59, 60, 73, 75, 76, 77, 613, 614, 900 ], # Jumpstart 2022
               [ 51, 71, 97, 241 ], # Dominaria United Commander
               [ 262, 412, 457, 460 ], # Dominaria Remastered
               [ 33, 35 ], # 30th Anniversary Play Promos
               [ 0 ], # The List
               [ 29, 31, 59, 175 ], # Phyrexian All Will Be One Commander
               [ 262, 304, 327, 381, 442, 481 ], # Modern Horizons 2
               [ 0 ], # MH1 Timeshifts
               [ 0 ], # Wizards Play Network 2021
               [ 0 ], # Wizards Play Network 2022
               [ 0 ], # Unsanctioned
               [ 0 ], # War of the Spark
               [ 292, 320, 323, 338, 343, 381 ], # March of the Machine
               [ 51, 101, 151, 186, 229, 231 ], # March of the Machine: Aftermath
               [ 66, 131, 196 ], # Multiverse Legends
               [ 80, 134, 450 ], # MOM Commander
               [ 0 ], # Secret Lair 30th Anniversary Countdown Kit
               [ 0 ], # Universes Within
               [452, 622, 668, 692, 704, 744, 779, 1057, 1067, 1068], # Commander Masters
               [277, 297, 308, 323, 375, 0], # Wilds of Eldraine
               [29, 57, 59, 0], # Wilds of Eldraine Commander
               [64, 84, 110], # Enchanting Tales
               [302, 332, 340, 346, 405, 452, 713, 723, 731, 751, 824, 829, 0], # Lord of the Rings
               [81, 85, 161, 378, 411, 491, 535, 0], # Lord of the Rings Commander
               [ 0 ], # Ravnica: City of Guilds
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 0 ],
               [ 192, 206, 332, 535, 565, 606, 923, 1126, 1156, 0 ], # Doctor Who            
               [ 292, 320, 353, 410 ], # LCI
               [ 17, 21, 69, 104, 105, 0 ], # LCC
               [ 292, 302, 416, 446, 467 ], # RVR
               [ 27, 0 ],
               [ 0 ],
               [ 9, 322, 900 ]
               ]

card_versions = [ [ "", " [Showcase]", "", " [Galaxy Foil]", " [Showcase Galaxy]", " [Galaxy Foil]", " [Promo]" ], # 0 Unfinity
                  [ "", " [Alt Art]", " [Showcase]", " [Etched]", " [Ext Art]", "", " [Promo]", "" ], # 1 Commander Legends - Battle for Baldur's Gate
                  [ "", " [Alt Art]", " [Showcase]", " [Phyrexia]", " [Gilded]", " [Ext Art]", " [Etched]", " [Boxtopper]", " [Promo]", "" ], # 2 Streets of New Capenna
                  [ "", " [Ext Art]", " [Showcase]", "" ], # 3 New Capenna Commander
                  [ "" ], # 4 Heads I Win, Tails You Lose
                  [ "" ], # 5 Game Day Promos
                  [ "" ], # 6 Wizards Play Network 2022
                  [ "" ], # 7 Universes Within
                  [ "" ], # 8 Year of the Tiger 2022
                  [ "", " [Ext Art]", " [Showcase]", "" ], # 9 Neon Dynasty Commander
                  [ "" ], # 10 Commander Collection - Black
                  [ "" ], # 11 Commander Collection - Green
                  [ "", " MID", "", " MID", "", " MID", "", " MID", "", " VOW", "", " VOW", "", " VOW", "" ], # 12 Innistrad - Double Feature
                  [ "" ], # 13 Judge Gift Cards 2022
                  [ "", " [Ext Art]", "" ], # 14 Innistrad - Crimson Vow Commander
                  [ "", " [Ext Art]", "" ], # 15 Innistrad - Midnight Hunt Commander
                  [ "", " [Ext Art]", "" ], # 16 Forgotten Realms Commander
                  [ "", " [Alt Art]", " [Showcase]", " [Ext Art]", " [Promo]" ], # 17 Adventures in the Forgotten Realms
                  [ "", " [Alt Art]", " [Sketch]", " [Retro]", " [Ext Art]", " [Promo]" ], # 18 Modern Horizons 2
                  [ "", " [Ext Art]", "" ], # 19 Commander 2021
                  [ "", "" ], # 20 Kaldheim Commander
                  [ "", " [Ext Art", ""], # 21 Zendikar Rising Commander
                  [ "", "" ], # 22 Zendikar Rising Expeditions
                  [ "", "" ], # 23 Secret Lair - Ultimate Edition
                  [ "", "" ], # 24 Secret Lair Drops
                  [ ""," [1]",""," [1]",""," [1]",""," [1]",""," [1]",""," [1]",""," [1]",""," [1]",""," [2]",""," [2]",""," [2]",""," [2]",""," [2]",""," [2]",""," [2]",""," [2]",""," [Alt Art]"," [Etched]"," [Ext Art]",""], # 25 Commander Legends
                  [ "" ], # 26 Judge Gift Cards
                  [ ""," [Alt Art]"," [Ext Art]"," [Promo]" ], #27 Strixhaven
                  [ "" ], # 28 Signature Spellbook: Chandra
                  [ "", " [Showcase]", " [Ext Art]", " [Bundle]", " [Promo]", " [Alt Art]" ], # 29 Ikoria - Lair of Behemoths
                  [ "" ], # 30 Ravnica Weekend
                  [ "" ], # 31
                  [ "" ], # 32 Game Day Promos
                  [ "" ], # 33 Game Night 2019
                  [ " [Etched]"," [Alt Art Etched]"], # 34 Mystical Archive
                  [ "" ], # 35 Time Spiral Remastered
                  [ "" ], # 36 Mystery Booster Test Cards
                  [ "", " [Alt Art]", " [Etched]", " [Textured]", " [Promo]" ], # 37 Double Masters 2022
                  [ "", " [Alt Art]", " [Phyrexia]", " [Showcase]", " [Alt Art]", " [Etched]", " [Red]", " [Green]", " [Blue]", " [Yellow]", " [Ext Art]", " [Promo]" ],  # 38 Kamigawa - Neon Dynasty
                  [ "" ], # 39 The List
                  [ "", " [Showcase]", " [Textured]", " [Phyrexian]", " [Phy Art]", " [Alt Art]", " [Alt Art 1]", " [Alt Art 2]", " [Alt Art]", " [Ext Art]", " [Buy-a-Box]", " [Promo]" ], # 40 Dominaria United
                  [ "" ], # 41 Dominaria United Commander
                  [ "", " [Alt Art]", " [Ext Art]", " [Promo]" ], # 42 The Brother's War
                  [ "", " [Ext Art]", "" ], # 43 Brother's War Commander
                  [ "", " [Schematic]" ], # 44 Brother's War Retro Artifacts
                  [ "", " [Alt Art]", " [Showcase]", " [Ext Art]", "" ], # 45 Kaldheim
                  [ "" ], # 46 Alpha
                  [ "" ], # 47 Beta
                  [ "" ], # 48 Unlimited
                  [ "" ], # 49 Fallen Empires
                  [ "", " [Shattered]" ], # 50 Transformers
                  [ "" ], # 51 Arabian Nights
                  [ "" ], # 52 Antiquities
                  [ "" ], # 53 Legends
                  [ "" ], # 54 The Dark
                  [ "" ], # 55 Ice Age
                  [ "" ], # 56 Homelands
                  [ "" ], # 57 Alliances
                  [ "" ], # 58 Mystery Booster
                  [ "", " [Promo]", " [Showcase]", " [Alt Art]", " [Oil]", " [Alt Art]", " [Ext Art]", "", " [Compleat]" ], # 59 Phyrexia All Will Be One
                  [ "", " [Alt Art]","", " [Alt Art]","", " [Alt Art]","", " [Alt Art]", "" ], # 60 Jumpstart 2022
                  [ "", " [Etched]", " [Ext Art]", "" ], # 61 Dominaria United Commander
                  [ "", " [Retro]", " [Alt Art]", " [Promo]" ], # 62 Dominaria Remastered
                  [ "", " [Etched]" ], # 63 30th Anniversary Play Promos
                  [ "" ], # 64 The List Unfinity Edition
                  [ "", " [Display]", " [Ext Art]", "" ], # 65 Phyrexia: All Will Be One Commander
                  [ "", " [Etched]", " [Alt Art]", " [Sketch]", " [Retro Etched]", " [Ext Art]", "" ], # 66 Modern Horizons 2
                  [ " [Etched]" ], # 67 Modern Horizons 1 Timeshifts
                  [ "" ], # 68 Wizards Play Network 2021
                  [ "" ], # 69 WPN 2022
                  [ "" ], # 70 Unsanctioned
                  [ " [Alt]"], # 71 War of the Spark
                  [ "", " [Showcase]", " [Alt Art]", "", " [Alt Art]", " [Ext Art]" ], # 72 March of the Machine
                  [ "", " [Showcase]", " [Etched]", " [Ext Art]", " [Halo]", " [Promo]" ], # 73 March of the Machine: Aftermath
                  [ " [Showcase]", " [Etched]", " [Rainbow]" ], # 74 Multiverse Legends
                  [ "", " [Ext Art]", "" ], # 75 MOM Commander
                  [ "" ], # 76 Secret Lair 30th Anniversary Countdown Kit
                  [ "" ], # 77 Universes Within
                  ["", " [Etched]", " [Alt Art]", " [Profile]", " [Alt Art]", "", " [Ext Art]", "", " [Textured]", " [Promo]"], # 78 Commander Masters
                  ["", " [Showcase]", " [Alt Art]", "", " [Ext Art]", " [Promo]"], # 79 Wilds of Eldraine
                  ["", " [Ext Art]", " [Etched]", ""], # 80 Wilds of Eldraine Commander
                  [ "", " [Alt Art]", " [Confetti]" ], # 81 Enchanting Tales
                  ["", " [Ring]", "", " [Alt Art]", " [Ext Art]", " [Scene]", " [Showcase]", " [Surge ]", "", " [Alt Art]", " [Surge]", "", " [Ext Art]"], # 82 Lord of the Rings
                  ["", " [Etched]", " [Ext Art]", "", " [Surge]", " [Showcase]", "", " [Surge]"], # 83 Lord of the Rings Commander
                  [ "" ], # 84 Ravnica: City of Guilds
                  [ " [SDCC13]" ], # 85 SDCC13
                  [ " [SDCC14]" ], # 86 SDCC14
                  [ " [SDCC15]" ], # 87 SDCC15
                  [ " [SDCC16]" ], # 88 SDCC16
                  [ " [SDCC17]" ], # 89 SDCC17
                  [ " [SDCC18]" ], # 90 SDCC18
                  [ " [SDCC19]" ], # 91 SDCC19
                  [ "", " [Display]", "", " [Ext Art]", " [Showcase]", " [Promo]", " [Surge]", " [Surge Ext Art]", " []" ], # 92 Doctor Who
                  [ "", " [Showcase]", " [Alt Art]", " [Ext Art]", " [Neon]" ], # 93 Lost Caverns
                  [ "", " [Showcase]", " [Ext Art]", "", " [Alt Art]", "" ], # 94 Lost Caverns Commander
                  [ "", " [Alt Art]", " [Retro]", " [Alt Art]", "", " [Promo]" ], # 95 Ravnica Remastered
                  [ "", " [Embossed]"], # 96 Jurassic World Collection
                  [ "" ], # 97 Revised
                  [ " [Surge]", "", " [Promo]" ] # 98 Warhammer 40K
                  ]

c_set = 2
current_version = 0

# Query String
query = '++e:' + set_code[c_set]

# Basic Land Fixers
basics = [ "Forest", "Island", "Mountain", "Plains", "Swamp", "Wastes",
           "Snow-Covered Forest", "Snow-Covered Island", "Snow-Covered Mountain",
           "Snow-Covered Plains", "Snow-Covered Swamp", "Snow-Covered Wastes" ]
basic_counts = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]

# Images go here
image_path = "D:\Magic The Gathering\Image Downloader\\" + set_name[c_set] + "\\"

# Search for cards
def get_set_cards():
    card_list = []
    page_count = 1;
    card_count = 1;
    set_size = 1
    while(True):
        search = scrython.cards.Search(q=query, page=page_count, order="set")
        print("Processing cards " + str(card_count) + " to " + str(cards_remaining(search.total_cards(), page_count)) + "...")
        time.sleep(0.5)
        for card in search.data():
            card_list.append(card)
            card_count = card_count + 1
        if search.has_more():
            page_count = page_count + 1;
        if not search.has_more():
            return card_list

# Search for cards
def get_sets_cards(set_num):
    card_list = []
    page_count = 1;
    card_count = 1;
    set_size = 1
    query = '++e:' + set_code[set_num]
    while(True):
        search = scrython.cards.Search(q=query, page=page_count, order="set")
        print("Processing cards " + str(card_count) + " to " + str(cards_remaining(search.total_cards(), page_count)) + "...")
        time.sleep(0.5)
        for card in search.data():
            card_list.append(card)
            card_count = card_count + 1
        if search.has_more():
            page_count = page_count + 1;
        if not search.has_more():
            return card_list

# Search for cards skipping by collector IDs:
def get_set_cards_range(card_list, bottom, top):
    new_cards = card_list.copy()
    new_cards = get_set_cards_top(new_cards, top)
    new_cards = get_set_cards_bottom(new_cards, bottom)
    return new_cards

def get_set_cards_bottom(card_list, start):
    less_cards = card_list.copy()
    i = 1
    while(i < start):
        less_cards.pop(0)
        i = i+1
    print("Removed preceding values, list is now " + len(less_cards) + " cards.")

def get_set_cards_top(card_list, finish):
    less_cards = card_list.copy()
    i = finish
    while(i < len(card_list)):
        less_cards.pop(i)
    print("Removed proceding values, list is now " + len(less_cards) + " cards.")

def cards_remaining(set_size, page_count):
    if set_size > page_count * 175:
        return page_count * 175
    else:
        return set_size
    

# Get File Names
def get_filename(card):
    global current_version, c_set
    if card["name"][:2] == "A-":
        return card["name"]
    if card["name"] in basics:
        basic_index = basics.index(card["name"])
        current_file = current_file = str(card["name"]) + " [" + str(basic_counts[basic_index]) + "]"
        basic_counts[basic_index] = basic_counts[basic_index] + 1
    else:
        try: 
            if int(card["collector_number"]) == int(boundaries[c_set][current_version]):
                current_version = current_version + 1
                print("\nChanged to" + str(card_versions[c_set][current_version]))
        except ValueError:
            print("Collector number is not an int.")
        if "//" in card["name"]:
            current_file = str(card["name"]).replace(" // ", "_") + str(card_versions[c_set][current_version])
        elif "\"" in card["name"]:
            current_file = str(card["name"]).replace("\"", "") + str(card_versions[c_set][current_version])
        elif ":" in card["name"]:
            current_file = str(card["name"]).replace(":", "") + str(card_versions[c_set][current_version])
        elif "?" in card["name"]:
            current_file = str(card["name"]).replace("?", "") + str(card_versions[c_set][current_version])
        else:
            current_file = str(card["name"]) + str(card_versions[c_set][current_version])
    return current_file 

# Get filenames for either side of transform / MDFC cards
def get_filenames(card, collector_id):
    global current_version, c_set
    if int(collector_id) == boundaries[c_set][current_version]:
        current_version = current_version + 1
    current_file = str(card["name"]) + str(card_versions[c_set][current_version])
    return current_file

# List of Sets
def get_sets():
    sets = scrython.sets.Sets()
    sets = enumerate(sets.data())
    for i, set_id in sets:
        print(str(i) + ", " + str(set_id["code"].upper()) + "," + str(set_id["name"]))

def get_sets_raw():
    sets = scrython.sets.Sets()
    print(sets.data())

def get_sets_expanded():
    sets = scrython.sets.Sets()
    for i, set_id in enumerate(sets.data()):
        print(str(set_id["code"]) + ";" + str(set_id["name"]) + ';' + str(set_id["set_type"]) + ';' +
              str(set_id["released_at"]) + ';' + str(set_id["nonfoil_only"]) + ';' +
              str(set_id["foil_only"]) + ';0;""')

def get_sets_search():
    sets = scrython.sets.Sets()
    set_types = []
    for i, set_id in enumerate(sets.data()):
        if not set_id["set_type"] in set_types:
            set_types.append(set_id["set_type"])
    print(str(set_types))

# File Names to Download
# Uncomment the if block to download png instead of jpg files
# These have transparency on the corners which raises the size by an order of magnitude
# With all variants in png, average hard drive space is ~1GB per set vs ~70MB per set jpg
def get_images(cards):
    os.makedirs(image_path,511,True)
    current_lang = ""
    for card in cards:
        time.sleep(0.5)
        if card["lang"] not in current_lang:
            current_lang = card["lang"]
            lang_path = change_lang_dir(card, image_path) + "\\"
            lang_path_foil = change_lang_dir(card, image_path) + " FOIL\\"
            if "nonfoil" in card["finishes"]:
                os.makedirs(lang_path,511,True)
            else:
                os.makedirs(lang_path_foil,511,True)
        if card["digital"]:
            continue
 #       if card["highres_image"]:
 #           c_format = "png"
 #           ext = "png"
        else:
            c_format = "large"
            ext = "jpg"
        if "nonfoil" in card["finishes"]:
            os.chdir(lang_path)
        else:
            os.chdir(lang_path)
        if card["layout"] == "transform" or card["layout"] == "modal_dfc":
            for i in range(0, 2):
                file_name = get_filenames(card["card_faces"][i], card["collector_number"])
                file_url = card["card_faces"][i]["image_uris"][c_format]
                file_name = file_name + "." + ext
                image_data = requests.get(file_url).content
                with open(file_name, 'wb') as handler:
                    handler.write(image_data)
                print("Downloaded " + file_name + "...")
        else:
            file_name = get_filename(card)
            file_url = card["image_uris"][c_format]
            file_name = file_name + "." + ext
            image_data = requests.get(file_url).content
            with open(file_name, 'wb') as handler:
                handler.write(image_data)
                handler.close()
            print("Downloaded " + file_name + "...")
    print("Work complete.")

def fix_lang(card):
    lang = card["lang"]
    match lang:
        case "en":
            return "ENG"
        case "de":
            return "GER"
        case "fr":
            return "FRA"
        case "it":
            return "ITA"
        case "ja":
            return "JPN"
        case "ko":
            return "KOR"
        case "pt":
            return "POR"
        case "es":
            return "SPA"
        case "ru":
            return "RUS"
        case "zhs":
            return "ZHC"
        case "zht":
            return "ZHT"
        case "ph":
            return "PHY"
        case _:
            return "ENG"

def change_lang_dir(card, image_path):
    lang_prefix = fix_lang(card)
    lang_path = image_path + lang_prefix
    print("\nLanguage changed to " + lang_prefix + ".")
    return lang_path

def get_card(name):
    card = scrython.cards.Search(q=name)
    print(card.data())

def get_card_set(name, code):
    card = scrython.cards.Search(q=name, code=code)
    print(card.data())

def get_languages(cards):
    languages = []
    folders = []
    for card in cards:
        if not card["lang"] in languages:
            languages.append(card["lang"])
            if "nonfoil" in card["finishes"]:
                folders.append(card["lang"])
            else:
                folders.append(card["lang"] + " foil")
    print(languages)
    print(folders)

"""
Set Code;Set Name;Set Type;Release Date;Non-Foil Only;Foil Only;Versions,Separated,By,Commas;Boundaries,Separated,By,Commas
"""
def import_sets():
    path = "E:\\Programming Projects\\DeepHoursDB\\set_db.txt"
    file = open(path, 'r+')
    sets = []
    for line in file:
        read = file.readline()
        read = read.split(';')
        versions = read.pop(7).split(',')
        boundaries = read.pop(6).split(',')
        read.append(versions)
        read.append(boundaries)
        sets.append(read)
    file.close()
    sets.sort(key = lambda x: (x[2], x[3]))
    return sets

def print_sets(sets):
    for current_set in sets:
        print("\nSet Name: " + str(current_set[1]) + 
              "\nSet Code: " + str(current_set[0]).upper() + 
              "\nSet Type: " + str(current_set[2]) + 
              "\nRelease Date: " + str(current_set[3])) 
        #print("\nNon-Foil Only: " + str(current_set[4]) + "  Foil Only: " + str(current_set[5]))
        #print("\nVersions: " + str(current_set[6]) + "\nBoundaries: " + str(current_set[7]) + "\n\n")

def get_secret_lairs(cards):
    #names = []
    eng = image_path + "ENG\\"
    eng_foil = image_path + "ENG FOIL\\"
    os.makedirs(image_path,511,True)
    os.makedirs(eng,511,True)
    os.makedirs(eng_foil,511,True)
    os.makedirs(image_path,511,True)
    current_lang = ""
    for card in cards:
        file_name = ""
        time.sleep(0.5)
        col_num = ""
        if card["lang"] not in current_lang:
            current_lang = card["lang"]
            lang_path = change_lang_dir(card, image_path)
            os.makedirs(lang_path + "\\",511,True)
            os.makedirs(lang_path + " FOIL\\",511,True)
        if "//" in card["name"]:
            file_name = str(card["name"]).replace(" // ",'_')
        else:
            file_name = str(card["name"])
        file_name = file_name + " [" + str(col_num + card["collector_number"]) + "]"
        if card["highres_image"]:
            c_format = "png"
            ext = "png"
        else:
            c_format = "large"
            ext = "jpg"
        if "nonfoil" in card["finishes"]:
            os.chdir(eng)
        else:
            os.chdir(eng_foil)
        file_name = file_name + "." + ext
        try:
            file_url = card["image_uris"][c_format]
        except KeyError:
            print("Image_URI not found")
        else:
            image_data = requests.get(file_url).content
            with open(file_name, 'wb') as handler:
                handler.write(image_data)
                handler.close()
            print("Downloaded " + file_name + "...")
    print("Work complete.")



def get_set_raw(code):
    set_list = scrython.sets.Code(code=code)
    for c_set in enumerate(set_list):
        print(c_set)

def get_set_code(code):
    c_set = scrython.sets.Code(code)
    print("Name: " + c_set.name())
    print("Code: " + c_set.code())
    print("Cards in Set: " + str(c_set.card_count()))
    print("Released: " + c_set.released_at())
    print("Set Type: " + c_set.set_type())
    print("Icon: " + c_set.icon_svg_uri())

def get_svg_files():
    sets = scrython.sets.Sets()
    faults = []
    default_path = image_path + "icons\\"
    os.makedirs(default_path,511,True)
    os.chdir(default_path)
    for c_set in sets.data():
        time.sleep(0.5)
        set_type = str(c_set["set_type"])
        os.makedirs(set_type,511,True)
        type_dir = default_path + set_type
        os.chdir(type_dir)
        #print(str(c_set["code"]).upper() + "  " + str(c_set["icon_svg_uri"]))
        file_name = str(c_set["code"].upper()) + ".svg"
        file_url = c_set["icon_svg_uri"]
        image_data = requests.get(file_url).content
        try:
            with open(file_name, 'wb') as handler:
                handler.write(image_data)
                #handler.close()
        except OSError:
            print("Couldn't download " + file_name + " for some reason.")
            faults.append(file_name)
        else:
            print(str(file_name) + " downloaded.")
        os.chdir(default_path)
    print(faults)
    print("Work complete.")

def build_icons():
    icon_path = image_path + "editing svg\\"
    icon_name = "AFR.svg"
    icon_comm = "AFR_C.svg"
    icon_unco = "AFR_U.svg"
    icon_rare = "AFR_R.svg"
    icon_myth = "AFR_M.svg"
    icon_spec = "AFR_S.svg"
    icon_path_b = icon_path + icon_name
    icon_path_c = icon_path + icon_comm
    icon_path_u = icon_path + icon_unco
    icon_path_r = icon_path + icon_rare
    icon_path_m = icon_path + icon_myth
    icon_path_s = icon_path + icon_spec
    os.chdir(icon_path)
    hex_comm = "#000"
    hex_unco = "#718597"
    hex_rare = "#BFA575"
    hex_myth = "#C83217"
    hex_spec = "#755091"
    shutil.copy(icon_path_b,icon_path_c)
    shutil.copy(icon_path_b,icon_path_u)
    shutil.copy(icon_path_b,icon_path_r)
    shutil.copy(icon_path_b,icon_path_m)
    shutil.copy(icon_path_b,icon_path_s)
    f = open(icon_path_u, "a+")
    #print(f.readlines())

    icon_text = f.readlines()
    print(icon_text)
    icon_text = icon_text[0].replace("#000",hex_unco)
    f.write(icon_text)
    f.close()
    
    """
    f = open(icon_path_r, "w")
    f.replace("#000",hex_rare)
    f.close()
    f = open(icon_path_m, "w")
    f.replace("#000",hex_myth)
    f.close()
    f = open(icon_path_s, "w")
    f.replace("#000",hex_spec)
    f.close()
    """

# check set to find how many cards are png quality
def get_image_quality(cards):
    hi_res = 0
    lo_res = 0
    for card in cards:
        if card["highres_image"]:
            hi_res = hi_res + 1
        else:
            lo_res = lo_res + 1
    if lo_res == 0:
        print("All cards in this set have high res scans.")
    elif hi_res == 0:
        print("No cards in this set have high res scans.")
    else:
        print("There are " + str(hi_res) + " high-res images and " + str(lo_res) + " low-res images on Scryfall.")

def sets_by_type():
    sets = scrython.sets.Sets()
    sets = enumerate(sets.data())
    set_list = list()
    set_types = ['token', 'funny', 'draft_innovation', 'commander', 'expansion', 'memorabilia', 'promo', 'alchemy',
                 'masters', 'arsenal', 'box', 'masterpiece', 'starter', 'core', 'spellbook', 'planechase', 'duel_deck',
                 'from_the_vault', 'archenemy', 'treasure_chest', 'premium_deck', 'vanguard']
    for set_t in set_types:
        print("Set Type: " + set_t)
        for c_set in sets:
            print(c_set['set_type'])
            if c_set['set_type'].value() == set_t:
                set_list.append(c_set["name"])
        print("Sets:\n" + str(set_list))
        set_list.clear()


    
#build_icons()
#get_svg_files()
#get_set_code("tsr")
#get_set_raw("tsr")
#get_languages(get_set_cards())
#get_images(get_set_cards_range(get_set_cards(),262, 442))
get_images(get_set_cards())
#get_card("Far Out")
#get_sets()
#import_sets()
#get_secret_lairs(get_set_cards())
#get_card_set("Zndrsplt, Eye of Wisdom", "phed")
#get_sets_search()
#get_image_quality(get_set_cards())
#print_sets(import_sets())
#get_sets_expanded()
#get_sets_raw()
#sets_by_type()

#for i in [9, len(card_versions)]:
#    get_images(get_sets_cards(i))

