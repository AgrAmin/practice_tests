# dictionnaries
# Data structure like associative array are named dictionnaries in python
# Basically : you are pairing key/value. A key mapped to a value

post = {"ID": 209,
        "Age":109,
        "gender": "Male"}
print(type(post))
print(post["gender"])

#check if a key exit or not
try:
    print(post['job'])
except KeyError:
    print("Not in this post")

#check for the method can applied on a dictionary type
print(dir(post))# display the directory
help(post.get)
