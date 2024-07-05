user_data = []


def fill_form():
    print('Welcome to Anuj\'s flight club.\nWe find the best flight deals and email you.')
    firstname = input('What is your first name? ')
    lastname = input('What is your last name? ')
    email = input('What is your email? ')
    re_mail = input('Type your email again: ')
    if email == re_mail:
        print('You\'re in the club!')
        user_data.append(firstname)
        user_data.append(lastname)
        user_data.append(email)
        return user_data
    else:
        print('Emails do not match. Start over.')
        fill_form()
