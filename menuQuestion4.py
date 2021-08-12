
class ItemNotFound(KeyError):
    """Item Not Found In Menu Exception"""

class Menu(dict):

    def __missing__(self, key):
        raise ItemNotFound(f"ItemNotFound: {key} not present in menu")
        
    def __str__(self):
        string = ""
        for food_item, cost in self.items():
            string += (str(food_item) + ' ' + str(cost) + '\n')
        return string[:-1] #removing the last \n


class Order(dict):

    def __init__(self, menu):
        super().__init__()
        self.menu = menu
        self.total_amount = 0

    def __setitem__(self, food_item, quantity):
        cost = self.menu[food_item]
        super().__setitem__(food_item, quantity)
        self.total_amount += cost * quantity

    def __str__(self):
        string = ""
        for food_item, quantity in self.ordered_items.items():
            string += (str(food_item) + ' ' + str(quantity) + '\n')
        return string[:-1]

    def bill(self):
        string = "---bill---".center(75) + '\n'
        string += "Food Item".ljust(50) + "-  Quantity  -  Cost\n"
        
        for food_item, quantity in self.items():
            cost = self.menu[food_item] * quantity
            string += f"{food_item}".ljust(50) + "-" + f"{quantity}".center(12) + f"-  {cost}\n"
        string += "Total Amount".ljust(63) + f"-  {self.total_amount}\n"

        return string


class Bill:

    def __init__(self, menu, order):
        self.menu = menu
        self.order = order

    def __str__(self):
        string = "---bill---".center(75) + '\n'
        string += "Food Item".ljust(50) + "-  Quantity  -  Cost\n"
        
        for food_item, quantity in self.order.items():
            cost = self.menu[food_item] * quantity
            string += f"{food_item}".ljust(50) + "-" + f"{quantity}".center(12) + f"-  {cost}\n"
        string += "Total Amount".ljust(63) + f"-  {self.order.total_amount}\n"

        return string

def main():
    m = Menu()
    m["idly"] = 10
    m["vada"] = 20
    o = Order(m)
    try:
        o["vada"] = 2
        o["pongal"] = 2
    except ItemNotFound as e:
        print(e)
    b = Bill(m, o)
    print(b)
    print(o.bill())

if __name__ == "__main__":
    main()
