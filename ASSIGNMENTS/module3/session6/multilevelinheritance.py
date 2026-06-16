class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

v = VerifiedInfluencer("rajvi123", "rajvi@gmail.com", 50000, "Blue Tick")

print(v.username)
print(v.email)
print(v.followers)
print(v.badge)