import item

class Recipe:

    def __init__(self, name, items, amount_of_people):
        self.name = name
        self.items = items
        self.amount_of_people = amount_of_people

    def __str__(self):
        return ' '.join("The Recipe", self.name, "contains ingredients", *self.items, ". It is for", self.amount_of_people)

    def calculate_total_calories(self):
        total_calories = 0
        for item in self.items:
            total_calories += item.calories * item.quantity
        return total_calories

    def draw(self, frame):
        print('..')   


def save_item(items):
    prop_list = []
    for item in items:
        props = []
        props.append(item.name)
        props.append(item.calories)
        prop_list.append(props)