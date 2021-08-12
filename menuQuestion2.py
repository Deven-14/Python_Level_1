
class Menu:

    def __init__(self):
        self.menu_items = {}

    def __add__(self, item):
        new_menu = Menu()
        new_menu.menu_items = dict(self.menu_items)
        new_menu.menu_items[item[0]] = item[1]
        return new_menu

    def __str__(self):
        string = ""
        for food_item, cost in self.menu_items.items():
            string += (str(food_item) + ' ' + str(cost) + '\n')
        return string[:-1] #removing the last \n

if __name__ == "__main__":
    m = Menu()
    m = m + ("idly", 10) + ("vada", 20)
    print(m)
