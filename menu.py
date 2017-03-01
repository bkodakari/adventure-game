#access the data

def get_menu_dictionary(menu_items):
    menu_dictionary = {}

    for item in menu_items:
        split_item = item.split(",")
        item_name = split_item[0]
        item_price = float(split_item[1])
        menu_dictionary[item_name] = item_price

    return menu_dictionary

menu = open("menu.txt")

menu_items = menu.readlines()

menu.close()

menu_dictionary = get_menu_dictionary(menu_items)

new_item_name = raw_input("What would you like to add to the menu? ").title()
new_item_price = raw_input("What is the price of the new item? ")

#check if the item is in the dictionary, if not, add the item to the dictionary
if new_item_name.lower() in menu_dictionary:
    print "Item is already on the menu. "
else:
    menu_dictionary[new_item_name] = float(new_item_price)


#write everything back to menu.txt

with open("menu.txt", mode = "w") as menu:
    for menu_item in menu_dictionary:
        menu_line = menu_item + "," + str(menu_dictionary[menu_item]) + "\n"
        menu.write(menu_line)

