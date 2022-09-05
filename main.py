
#                                 ~Day trip generator project - DevCodeCamp week 2 project 1~



import random



def greet_user():
    """function to greet users"""
    print (f"\n\n\tHello and welcome to the day trip planner!\n\n\t\tLets plan a day for you.\n")
greet_user()

   
def user_destion_selection():
    """Randomly select a city destination for the user from the below list"""

#list of popular cities to visit
cities = ["New York", "Osaka", "Amsterdam", "Frankfurt", "Georgetwon",]

while True:
    destination = random.choice(cities)
    user_destination_choice =input(f'\nWe have selected {destination} as a destination would you like to go on this trip? Enter Yes/No? ').capitalize()
    if user_destination_choice != "Yes":
        print (f"\n\t{destination}, is off the list try a different location.")
        
    elif user_destination_choice == "Yes":
        print (f"\n\t{destination}, is a great place to visit.")
        print (f"\nLet's set you up with transportation.")
        break 


def mode_of_transportation():
    """Randomly suggest a mode of transportation for the user from the below lists of options"""

#list of mode of transportation.
type_of_transportation = ["airplane", "train", "rental car", "taxi", "boat", "walking", "bike", ]

while True:
    transportation = random.choice(type_of_transportation)
    user_transport_choice = input (f"\nWould traveling by {transportation} work for you? Enter Yes/No ").capitalize()
    if user_transport_choice != "Yes":
        print (f"\nOk, lets try a different mode.") 
        continue

    elif user_transport_choice == "Yes":
        print(f"\n\tTraveling by {transportation} is a great way to explore {destination}.")
        break

def top_rated_restaurant_in_cities (destination):
    """Randomly suggest a restaurant from the destination to the user"""

#list of Restaurant options in each city. 
new_york_restaurants = ["A&A Bakery", "Home town BBQ", "Kochi",]
osaka_restaurants = ["Awajishima Burger", "Byakuan", "Yonemasu",]
amsterdam_restaurants = ["Jansz", "Wilde Zwijnen", "Stork",]
frankfurt_restaurants = ["Emma Metzler", "Charirs", "No.16",]
georgetown_restaurants = ["New Thriving", "Island Express", "Hibiscus",]

print (f"Let find a place a nice restaurant")

while True:
    if destination == "New York":
        restaurant = random.choice(new_york_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        if user_restaurant_choice != "Yes":
            print (f"Ok, lets try a different place")
            continue

        else:
             user_restaurant_choice == "Yes"
             print (f"\n\t{restaurant} is a great place to eat in {destination}")
             break
            
    if destination == "Osaka":
        restaurant = random.choice(osaka_restaurants)
        user_restaurant_choice = input (f"\nWould you like to dine at {restaurant}? Enter Yes/No ").capitalize()
        
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
        if user_restaurant_choice != "Yes":
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

#List of entertaining things to do per city. 
new_york_entertainment = ["MOMA", "Central Park Zoo", "Brooklyn Botanic Garden", ]
osaka_entertainmetnt = ["Osaka Aquarium Kaiyukan", "Kuromon Market", "Ramen cooking class"]
amsterdam_entertainment = ["Amsterdam Canal Cruise", "Van Gogh Museum", "ARTIS Amsterdam Royal Zoo"]
frankfurt_entertainmet = ["Palmengarten Botanical Garden", "Senckenberg Natural History Museum", "Neuschwanstein Castle"]
georgetown_entertainment = ["Stabroke market", "Guyana Botanical Gardens", "Georgetown Lighthouse"]

while True:
    if destination == "New York": 
        entertainment = random.choice(new_york_entertainment)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.\n")
        break

    elif destination == "Osaka":
        entertainment = random.choice(osaka_entertainmetnt)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.\n")
        break 
            
    elif destination == "Frankfurt":
        entertainment = random.choice(frankfurt_entertainmet)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.\n")
        break

    elif destination == "Amsterdam":
        entertainment = random.choice(amsterdam_entertainment)
        print (f"\nThe day's entertainment will include a visit to {entertainment}.\n")
        break
            
    else:
        entertainment = random.choice(georgetown_entertainment)
        print (f"\nThe days entertainment will include a visit to {entertainment}.\n")
        break

def trip_confirmation():
    """function to confirm day trip"""
    confirm = True
    while confirm == True:
        message = f"\tTo review your destination is: {destination}.\n\tYou will be traveing by: {transportation.capitalize()}.\n\tEentertainment will be a visit to: {entertainment}.\n"
        print (message)
        user_confirmation = input ("To confirm this trip enter 'Yes' - Enter 'No' to start over: ").capitalize()
        if user_confirmation == "Yes":
            print ("\nYour trip is confirmed, have an amazing time.\n\n")
            confirm = False
        else:
            if message != "Yes":
                return


trip_confirmation()


  


#                                         """" ~ Notes~ """" 

# bug1 - NY entertainment outputs else statement randomly selecting from georgetown_entertainment. 
# fixed "New_York" changed to "New York".

# bug2 - mode of transport Osk.
# fixed " train" to "train.

# bug3 Frankfurt's entertainment outputs from Amsterdam's list.
# fixed - updated variable to match.

# bug4 Amsterdam's entertainmet values defaults to else statement.
# fixed - elif statement added for Amsterdam


# Project questions:
# why didn't "if destination in cities:"" didn't work - line 67 & 131. 
# Why does the program work with only the first and last function call; currently unable to run a master function. 
    
 





    


