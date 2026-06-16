class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)
bp = BrandPartner("rajvi123", 50000, "Nike")
print("Username:", bp.username)
print("Followers:", bp.followers)
print("Brand Name:", bp.brand_name)