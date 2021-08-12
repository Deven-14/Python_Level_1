
class Menu:

    def __init__(self):
        self.menu_items = {}

    def __setitem__(self, food_item, cost):
        self.menu_items[food_item] = cost

    def __str__(self):
        string = ""
        for food_item, cost in self.menu_items.items():
            string += (str(food_item) + ' ' + str(cost) + '\n')
        return string[:-1] #removing the last \n

def main():
    m = Menu()
    m["idly"] = 10
    m["vada"] = 20
    print(m)

if __name__ == "__main__":
    main()
