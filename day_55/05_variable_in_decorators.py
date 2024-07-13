class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True


def is_authenticated(func):
    def wrapper(*args):
        if args[0].is_logged_in:
            func(args[0])

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f'This is {user.name}\'s new blog post')


new_user = User('Anuj')
create_blog_post(new_user)
