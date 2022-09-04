
                               
                                # """Day trip generator project - DevCodeCamp week 2 project"""

import os
import random

#list of mode of transportation.
type_of_transportation = ["airplane", "rail train", "rental car", "taxi", "boat", "walking", "biking", ]

#list of popular cities to visit
cities = ["New York", "Osaka", "Amsterdam", "Frankfurt", "Georgetwon",]

#list of Restaurant options in each city. 
new_york_restaurants = ["A&A Bakery", "Home town BBQ", "Kochi",]
osaka_restaurants = ["Awajishima Burger", "Byakuan", "Yonemasu",]
amsterdam_restaurants = ["Jansz", "Wilde Zwijnen", "Stork",]
frankfurt_restaurants = ["Emma Metzler", "Charirs", "No.16",]
georgetown_restaurants = ["New Thriving", "Island Express", "Hibiscus",]

#List of entertaining things to do per city. 
new_york_entertainment = ["MOMA", "Central Park Zoo", "Brooklyn Botanic Garden", ]
osaka_entertainmetnt = ["Osaka Aquarium Kaiyukan", "Kuromon Market", "Ramen cooking class"]
amsterdam_entertainment = ["Amsterdam Canal Cruise", "Van Gogh Museum", "ARTIS Amsterdam Royal Zoo"]
frankfurt_entertainmet = ["Palmengarten Botanical Garden", "Senckenberg Natural History Museum", "Neuschwanstein Castle"]
georgetown_entertainment = ["Stabroke market", "Guyana Botanical Gardens", "Georgetown Lighthouse"]



def greet_user():
    """function to greet users"""
    return print (f"\n\tHello and welcome to the day trip planner!\n\n\t  Lets plan a day trip for you.\n")

   
def user_destion_selection():
    """Randomly select a city destination for the user"""
while True:
    destination = random.choice(cities)
    user_destination_choice =input(f'\nWe have selected {destination} as a destination would you like to go on this trip? Enter Yes/No? ').capitalize()
    if user_destination_choice != "Yes":
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
    if user_transport_choice != "Yes":
        print (f"\nOk, lets try a different mode.") 
        continue

    elif user_transport_choice == "Yes":
        print(f"\n\tTraveling by {transportation} is a great way to explore {destination}.")
        break

def top_rated_restaurant_in_cities ():
    """Randomly suggest a restaurant from the destination to the user"""
    print (f"Let find a place a nice restaurant")
while True:
    if destination == "New York":
        restaurant = random.choice(new_york_restaurants)
        user_restaurant_choice = input (f"\nWould you like dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice != "Yes":
            print (f"Ok, lets try a different place")
            continue

        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
            
    if destination == "Osaka":
        restaurant = random.choice(osaka_restaurants)
        user_restaurant_choice = input (f"\nWould you dine at {restaurant}? Enter Yes/No ").capitalize()
        
        if user_restaurant_choice != "Yes":
            print (f"Ok, lets try a different place")
            continue

        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
   
    if destination == "Amsterdam":
        restaurant = random.choice(amsterdam_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice != "yes":
            print (f"Ok, lets try a different place")
            continue
       
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
    
    if destination == "Frankfurt":
        restaurant = random.choice(frankfurt_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice != "Yes":
            print (f"Ok, lets try a different place")
            continue
   
        else:
             user_restaurant_choice == "Yes"
             print (f"{restaurant} is a great place to eat in {destination}")
             break
  
    if destination == "Georgetwon":
        restaurant = random.choice(georgetown_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice != "Yes":
            print (f"Ok, lets try a different place")
            continue
  
        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break

def user_entertainment():
    """Randomly suggest things to do in the destination city """
while True:
    if destination == "New_York": 
        entertainment = random.choice(new_york_entertainment)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.")
        break

    elif destination == "Osaka":
        entertainment = random.choice(osaka_entertainmetnt)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.")
        break 
            
    elif destination == "Frankfurt":
        entertainment = random.choice(amsterdam_entertainment)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.")
        break
            
    else:
        entertainment = random.choice(georgetown_entertainment)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.")
        break

def run():
    """Master function to run all the above function"""
    greet_user()
    user_destion_selection()
    mode_of_transportation()
    top_rated_restaurant_in_cities()
    user_entertainment()
message = f"Your destination {destination}, your will traveing by {transportation} and the day's entertainment will be a {entertainment}\n\n"

run()
print (message)

            


    
        

       


    






    
        



# def run():
#     greet_user()
#     user_destination_choice
#     mode_of_transportation
#     top_rated_restaurant_in_cities
# run()





