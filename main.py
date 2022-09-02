
                               
                                # """Day trip generator project"""

import random
from re import U

#list of famous cities.
cities = ["Newy York, New York", "Osaka, Japan", "Amsterdam, Netherlands",  "Toronto, Canada", "Frankfurt, Germany", "Vienna, Austria",]

#list of  mode of transportation
mode_of_transportation = ["Airplane", "Rail train", "Rental car", "Taxi", "Boat"]


def greet_user():
    """function to geet users"""
    print (f"\tHello and welcome to the day trip planner!\n\n\t  Lets plan a day trip for you.\n")
greet_user()
   
def user_destion_selection():
    """Randomly select a city for the user"""
while True:
    destination = random.choice(cities)
    user_destination_choice =input(f'We have selected {destination} as a destination would you like to go on this trip? Enter Yes/No? ').capitalize()
    if user_destination_choice == "No":
        print (f"\nOk, lets try a different location.\n")      
        continue
    elif user_destination_choice == "Yes":
        print (f"{destination}, is a great place to visit.")
        print +=f"Let set up transportation."
        break 

user_destination_choice()








