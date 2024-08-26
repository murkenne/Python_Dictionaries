'''
1. Real-World Python Dictionary Applications

Objective: The aim of this assignment is to reinforce your understanding and application of Python
dictionaries, nested collections, and dictionary methods.

Task 1: Restaurant Menu update, You are given an initial struture of a restaurant menu stored in a nested
dictionary. Your task is to update this menu based on given instuctions

**Instructions**

1. Add a new category called "Beverages" with at least two items.    
2. Update the price of "Steak"  to 17.99
3. Remove "Bruschetta" from "Starters".  


'''

def add_new_category(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category '{category}' added to menu.")
    else:
        print(f"Category '{category}' already exist.")
        
def add_item(menu, category, item):
    if category in menu:
        if item not in menu[category]:
            menu[category].append(item)
            print(f"Item '{item}' added to '{category}.")
        else:
            print(f"Item '{item}' already on the menu.")
    else:
        print(f"Category '{category}' does not exist.")
        
def update_menu(menu, category, price):
    menu.update({category: price})
    print(f"Category {category}: ${price} updated.")
    
def display_menu(menu):
    for category, item in menu.items():
        print(f"{category}: {item}")



restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_new_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Diet coke")
add_item(restaurant_menu, "Beverages", "Sprite")
# Update the price of "Steak" and remove "Bruschetta"
# restaurant_menu["Main Course"]["Steak"] = 17.99
update_menu(restaurant_menu, "Steak", 17.99)
restaurant_menu["Starters"].pop("Bruschetta", None)
display_menu(restaurant_menu)
print(restaurant_menu)
