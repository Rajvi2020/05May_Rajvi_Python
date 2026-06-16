class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("----- Food Order Details -----")
        print("Restaurant Name:", self.restaurant_name)
        print("Items Ordered:")
        for item in self.items:
            print("-", item)
        print("Total Price: ₹", self.total_price)



order1 = FoodOrder(
    "Domino's Pizza",
    ["Margherita Pizza", "Garlic Bread", "Coke"],
    599
)
order1.show_order()