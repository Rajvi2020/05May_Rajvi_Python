8from insta import likes
from insta import comments
current_likes = 120
current_comments = 35
current_likes = likes.like_count(current_likes, 15)
current_comments = comments.comment_count(current_comments, 8)
print("Likes:", current_likes)
print("Comments:", current_comments)