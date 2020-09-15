def main():
    emails = {}
    email_name = input("Email: ")
    while email_name != "":
        name = get_name_from_email(email_name)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            email_name = input("Email: ")
        emails[email_name] = name
        email_name = input("Email: ")

    for email_name, name in emails.items():
        print("{} ({})".format(name, email_name))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()

#looked at solutions