class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price > 0, f"price '{price}' should be greater than 0"
        assert quantity >= 0, f"quantity should be greater than or equal to 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def total(self):
        return self.price * self.quantity


item1 = Item("phone", 150, 5)
item2 = Item("laptop", 400, 4)
item3 = Item("cable", 10, 15)
item4 = Item("mouse", 15, 10)
item4 = Item("keyboard", 100, 12)

print(Item.all)

for i in Item.all:
    print(i.name)
