'''
=================================================================================
Welcome to my solution to App Brewery's web design problem from an online Python 
course. I would like to thank them for their amazing course that teaches Python
from the ground up.
=================================================================================
'''

from flask import Flask, render_template
import requests
from post import Post

# This code creates a list of post objects.
response = requests.get("https://api.npoint.io/8b5c0fa5eb07a75f1e09")
all_posts_request = response.json()
all_post_objects = []

# Individually turn each post into an Object (OOP)
for post in all_posts_request:
    post_object = Post(post)
    all_post_objects.append(post_object) # Send them into a list

app = Flask(__name__)

@app.route('/')
def home():
    '''
    This method sends the index HTML file all the post objects so
    that it can generate the pages.
    '''
    return render_template("index.html", posts=all_post_objects)

@app.route('/post/<post_id>')
def get_blog_post(post_id):
    '''
    Method takes the ID (number) of the post from JINJA code in index.html.
    Then it scrapes through all posts to find the one with the matching ID.
    It then sends it to the post HTML page for display.
    '''
    # Method to get a JSON of the current post 
    current_post = None
    for post in all_post_objects:
        if int(post.id) == int(post_id):
            current_post = post
            break

    if current_post is None:
        return "Post not found", 404  # Handle the case where the post is not found
    
    return render_template("post.html", post=current_post)
    
if __name__ == "__main__":
    app.run(debug=True)
