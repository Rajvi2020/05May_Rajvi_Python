from insta import likes
from insta import comments
likes = 120
comments = 35
likes = likes.like_count(likes, 15)
comments = comments.comment_count(comments, 8)
print("Likes:", likes)
print("Comments:", comments)