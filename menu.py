
class Menu:

    def __init__(self):
        self.menu_items = {}

    def add(self, food_item, cost):
        self.menu_items[food_item] = cost

    def show(self):
        for food_item, cost in self.menu_items.items():
            print(food_item, cost)


if __name__ == "__main__":
    m = Menu()
    m.add("idly", 10)
    m.add("vada", 20)
    m.show()
