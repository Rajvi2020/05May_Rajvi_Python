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

    def format_followers(self):
        if self.followers >= 1000000:
            return str(self.followers / 1000000) + "M"
        elif self.followers >= 1000:
            return str(self.followers / 1000) + "K"
        else:
            return str(self.followers)

    def display_profile(self):
        print("Instagram Profile")
        print("Username:", self.username)
        print("Followers:", self.format_followers())
        print("Badge Status:", self.badge)

v = VerifiedInfluencer(
    "rajvi123",
    "rajvi@gmail.com",
    1500,
    "Blue Tick"
)

v.display_profile()