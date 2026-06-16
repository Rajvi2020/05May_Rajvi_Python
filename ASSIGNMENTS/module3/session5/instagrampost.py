class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1


post1 = InstagramPost(
    "Enjoying the beautiful sunset!",
    100,
    ["Nice pic!", "Awesome view!"]
)
post1.add_comment("Wonderful photo!")


print("Caption:", post1.caption)
print("Likes:", post1.likes)
print("Comments:", post1.comments)