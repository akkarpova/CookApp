class Item:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return self.name + " is " + str(self.calories) + " calories."





