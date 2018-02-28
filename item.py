import json
list_of_raw_items = []
list_of_items = []


class Item:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


    def __str__(self):
        return self.name + " is " + str(self.calories) + " calories."


def save_json(list_of_items):
    with open("items.json", "w") as f:
        json.dump(list_of_items, f)

def save_list(list_of_raw_items):
    for item in list_of_raw_items:
        properties = []
        properties.append(item.name)
        properties.append(item.calories)
        list_of_items.append(properties)


carrot = Item("carrot", 45)
list_of_raw_items.append(carrot)
lemon = Item("lemon", 15)
list_of_raw_items.append(lemon)
save_list(list_of_raw_items)
save_json(list_of_items)
print(list_of_items)