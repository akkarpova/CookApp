import tkinter as tk
import wunderpy2
import recipe

class CookApp:

    def __init__(self, title):
        self.tk = tk.Tk()
        self.title = title

    def draw(self):
        root = self.tk
        root.title(self.title)

        tk.Button(root, text='New Recipe', command=self.new_recipe).grid()

        root.mainloop()

    def new_recipe(self):
        recipe_window = tk.Toplevel()
        recipe_window.wm_title("New Recipe")
        tk.Label(recipe_window, text='Name:').grid(row=0, column=0)
        tk.Label(recipe_window, text='Ingredients:').grid(row=1, column=0)
        tk.Label(recipe_window, text='Servings:').grid(row=2, column=0)
        name = tk.Entry(recipe_window)
        #ingredients = Need to be able to add stuff from a list
        servings = tk.Entry(recipe_window)
        exit = tk.Button(recipe_window, text='Okay', command=recipe_window.destroy)

        name.grid(row=0, column=1)
        servings.grid(row=2, column=1)
        exit.grid(row=3, column=0)


def write_shopping_list(recipe):
    api = wunderpy2.WunderApi()
    client = api.get_client('231223', '3213123')
    for item in recipe.items:
        client.create_task('list_id', item.name)

def write_shopping_list_item(item):
    api = wunderpy2.WunderApi()
    client = api.get_client('20810582', '3203123')
    client.create_task('list_id', item.name)

if __name__ == '__main__':
    cook_app = CookApp('Durstinka Cooking App!')
    cook_app.draw()