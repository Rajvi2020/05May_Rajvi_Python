class ZomatoOrder:
    def add_item(self, item, quantity=1):
        print("Item:", item)
        print("Quantity:", quantity)


# Creating object
order = ZomatoOrder()

# Calling with only item name
order.add_item("Pizza")

# Calling with item name and quantity
order.add_item("Burger", 3)