
                               
                                # """Day trip generator project - DevCodeCamp week 2 project"""

import random

#list of popular cities to visit
cities = ["New York", "Osaka", "Amsterdam", "Frankfurt", "Georgetwon",]

#list of Restaurant options in each city. 
new_york_restaurants = ["A&A Bakery", "Home town BBQ", "Kochi",]
osaka_restaurants = ["Awajishima Burger", "Byakuan", "Yonemasu",]
amsterdam_restaurants = ["Jansz", "Wilde Zwijnen", "Stork",]
frankfurt_restaurants = ["Emma Metzler", "Charirs", "No.16",]
georgetown_restaurants = ["New Thriving", "Island Express", "Hibiscus",]

#list of mode of transportation.
type_of_transportation = ["airplane", "rail train", "rental car", "taxi", "boat", "walking", "biking", ]



def greet_user():
    """function to greet users"""
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
        print (f"\n\t{destination}, is a great place to visit.")
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
        print(f"\n\tTraveling by {transportation} is a great way to explore {destination}.")
        break

def top_rated_restaurant_in_cities ():
    """Randomly suggest a restaurant to the user"""
    print (f"Let find a place a nice restaurant")
while True:
    if destination == "New York":
        restaurant = random.choice(new_york_restaurants)
        user_restaurant_choice = input (f"\nWould you like to try {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice == "No":
            print (f"Ok, lets try a different place")
            continue
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
    if destination == "Osaka":
        restaurant = random.choice(osaka_restaurants)
        user_restaurant_choice = input (f"\nWould you like to try {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice == "No":
            print (f"Ok, lets try a different place")
            continue
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
    if destination == "Amsterdam":
        restaurant = random.choice(amsterdam_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice == "No":
            print (f"Ok, lets try a different place")
            continue
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
    if destination == "Frankfurt":
        restaurant = random.choice(frankfurt_restaurants)
        user_restaurant_choice = input (f"\nWould you like to try {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice == "No":
            print (f"Ok, lets try a different place")
            continue
        else:
             user_restaurant_choice == "Yes"
             print (f"{restaurant} is a great place to eat in {destination}")
             break
    if destination == "Georgetwon":
        restaurant = random.choice(georgetown_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice == "No":
            print (f"Ok, lets try a different place")
            continue
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break



    
        



# def run():
#     greet_user()
#     user_destination_choice
#     mode_of_transportation
#     top_rated_restaurant_in_cities
# run()





