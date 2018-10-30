import datetime

# ddate.py      Prints the current date of the Discordian Calendar and any
#               Holydays/Whollydays of that date to the console.
#               Date can be edited by changing current_date variable
#               Written by Alex Hartshorn

current_date = datetime.datetime.now()              # Today
#current_date = datetime.datetime(2005, 3, 19)       # Mojoday
#current_date = datetime.datetime(2005, 1, 10)       # Backwards Day
#current_date = datetime.datetime(2018, 12, 16)      # St. Melvin's Day
#current_date = datetime.datetime(2018, 12, 31)      # End of Year/Last day of Aftermath

# Return the day name
def day_name(num):
    day_names = {
        1: "Sweetmorn",
        2: "Boomtime",
        3: "Pungenday",
        4: "Prickle-Prickle",
        0: "Setting Orange"
    }
    return day_names.get(num, "NaD")

# Return the season name
def season_name(num):
    season_names = {
        1: "Chaos",
        2: "Discord",
        3: "Confusion",
        4: "Bureaucracy",
        5: "The Aftermath"
    }
    return season_names.get(num, "NaS")

# Return the post-number based on date
def num_post(num):
    if num < 13:
        num_p = num % 13
    else:
        num_p = num % 10
    num_posts = {
        1: "st",
        2: "nd",
        3: "rd"
    }
    return num_posts.get(num_p, "th")

# Return the name of the current Holyday, or False if it isn't one
def get_holyday(season_num, season_day):
    if season_num == 1:
        chao_days = {
            5: "Mungday",
            50: "Chaoflux",
        }
        return chao_days.get(season_day, False)
    elif season_num == 2:
        discord_days = {
            5: "Mojoday",
            50: "Discoflux",
        }
        return discord_days.get(season_day, False)
    elif season_num == 3:
        confusion_days = {
            5: "Syaday",
            50: "Confuflux",
        }
        return confusion_days.get(season_day, False)
    elif season_num == 4:
        bureaucracy_days = {
            5: "Zaraday",
            50: "Bureflux",
        }
        return bureaucracy_days.get(season_day, False)
    elif season_num == 5:
        aftermath_days = {
            5: "Maladay",
            50: "Afflux",
        }
        return aftermath_days.get(season_day, False)    
    else:
        return False

# Return the name of the current Whollyday, or False if it isn't one
# Whollyday list found at http://discordia.wikia.com/wiki/Whollyday
#   with additions by the Honorable Pope Akavien
def get_whollyday(season_num, season_day):
    if season_num == 1:
        chao_days = {
            1: "Nude Year's Day",
            10: "demrofeR, yaD sdrawkcaB",
            18: "Pat Pineapple Day",
            21: "Hug Day",
            26: "lanoitidarT, yaD sdrawkcaB",
            46: "Springfield Day",
            49: "The Mary Day",
            51: "Pet Loving Day",
            69: "Head Chicken Day"
        }
        return chao_days.get(season_day, False)
    elif season_num == 2:
        discord_days = {
            11: "Discordians for Jesus/Love Your Neighbor Day",
            18: "Amateur's Day",
            19: "St. John the Blasphemist's Day",
            23: "Jake Day",
            32: "Universal Ordination Day",
            70: "Jake Day Jr.",
            72: "Towel Day"
        }
        return discord_days.get(season_day, False)
    elif season_num == 3:
        confusion_days = {
            11: "537 Day",
            15: "Mad Hatter Day",
            20: "Doomed TV Seriews Rememberance Day",
            26: "Captain Tuttle Day",
            28: "St. George's Day",
            37: "Mid Year's Day",
            55: "Mal-2 Day",
            57: "John Dillinger Day"
        }
        return confusion_days.get(season_day, False)
    elif season_num == 4:
        bureaucracy_days = {
            3: "Multiversal Underwear Day",
            18: "Festival of Hanky-Panky Spankies",
            33: "Pussyfoot Day",
            37: "Mass of Planet Eris",
            55: "Feats of St. John the Blasphemist",
            57: "Shamlicht Kids Club Day",
            59: "Gonkulator Day",
            60: "Mad Hatter Day",
            66: "Habeas Corpus Rememberance Day"
        }
        return bureaucracy_days.get(season_day, False)
    elif season_num == 5:
        aftermath_days = {
            28: "Ek-sen-triks CluborGuild Day",
            36: "Spanking Fest",
            37: "537 Day",
            46: "Hug Day II",
            58: "St. Melvin's Day",
            67: "Giftmas",
            72: "New Year's Eve Eve"
        }
        return aftermath_days.get(season_day, False)    
    else:
        return False

def ddate(current_date):
    date_num = int(current_date.strftime("%j"))

    # Account for February 29
    if current_date.year % 400 == 0 or (current_date.year % 4 == 0 and current_date.year % 100 != 0):
        if current_date.month > 2:
            date_num = int(current_date.strftime("%j")) - 1

    season_num = (date_num / 74) + 1                    # Each season is 73 days long (offset for 1-5)
    season_day = date_num % 73                          # Which day of the season it is
    date_day = (date_num % 5)                           # Which day of the week it is
    year_num = int(current_date.strftime("%Y")) + 1166  # Current year in YOLD format

    # Account for the last day of each season
    if season_day == 0:
        season_day = 73

    dday_name = day_name(date_day)
    dd_season_name = season_name(season_num)
    season_post = num_post(season_day)

    holyday = get_holyday(season_num, season_day)
    whollyday = get_whollyday(season_num, season_day)

    # Check if it is St Tib's Day, else print in standard format
    if current_date.month == 2 and current_date.day == 29:
        print("Today is {}, St Tib's Day, {} YOLD.".format(dday_name, year_num))
    else:
        print("Today is {}, the {}{} day of {}, YOLD {}.".format(
            dday_name, season_day, season_post, dd_season_name, year_num))

    # If it is a holyday or whollyday, print which day it is.
    if holyday != False:
        print("Today is the holyday of {}!".format(holyday))
    if whollyday != False:
        print("Today is the whollyday of {}!".format(whollyday))

ddate(current_date)
