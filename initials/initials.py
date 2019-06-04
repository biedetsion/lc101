def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name = fullname
    name_list = name.split()

    initials = ""

    for name in name_list:
        initials += name[0].upper()
    return initials
