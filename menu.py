
class Menu:

    def __init__(self):
        self.menu_items = {}

    def add(self, key, value):
        self.menu_items[key] = value

    def show(self):
        for key, value in self.menu_items.items():
            print(key, value)


if __name__ == "__main__":
    m = Menu()
    m.add("idly", 10)
    m.add("vada", 20)
    m.show()
