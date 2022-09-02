
                               
                                # """Day trip generator project - DevCodeCamp week 2 project"""

import random


#list of famous cities.
cities = ["Newy York, New York", "Osaka, Japan", "Amsterdam, Netherlands",  "Toronto, Canada", "Frankfurt, Germany", "Vienna, Austria", "Georgetwon, Guyana",]

#list of  mode of transportation.
type_of_transportation = ["Airplane", "Rail train", "Rental car", "Taxi", "Boat", "Walking", "Biking", ]


def greet_user():
    """function to geet users"""
    print (f"\tHello and welcome to the day trip planner!\n\n\t  Lets plan a day trip for you.\n")

   
def user_destion_selection():
    """Randomly select a city for the user"""
while True:
    destination = random.choice(cities)
    user_destination_choice =input(f'\nWe have selected {destination} as a destination would you like to go on this trip? Enter Yes/No? ').capitalize()
    if user_destination_choice == "No":
        print (f"\nOk, lets try a different location.")      
        continue
    elif user_destination_choice == "Yes":
        print (f"\n{destination}, is a great place to visit.")
        print (f"\nLet's set you up with transportation.")
        break 

def mode_of_transportation():
    """Randomly suggest a mode of transportation for the user"""
while True:
    transportation = random.choice(type_of_transportation)
    user_transport_choice = input (f"\nWould traveling by {transportation} work for you? Enter Yes/No ").capitalize()
    if user_transport_choice == "No":
        print (f"\nOk, lets try a different mode.") 
        continue
    elif user_transport_choice == "Yes":
        print(f"\n{transportation} is a great way to explore {destination}")
        print (f"\nLet's fined some fun things to do in {destination}.")
        break
mode_of_transportation()









