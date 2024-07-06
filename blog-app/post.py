import requests

#response = requests.get("https://api.npoint.io/8b5c0fa5eb07a75f1e09")
#all_posts = response.json()

class Post:
    '''
    Python class that creates an object for all the posts.
    This makes handling them easier later in the code.
    '''
    def __init__(self, a_post):
        self.id = a_post['id']
        self.title = a_post['title']
        self.subtitle = a_post['subtitle']
        self.body = a_post['body']

