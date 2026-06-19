class Content:
    def display(self, title):
        print("Title:", title)


class Movie(Content):
    def display(self, title, year):   # Overriding
        print("Title:", title)
        print("Year:", year)



m = Movie()


m.display("3 Idiots", 2009)