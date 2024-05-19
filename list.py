import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description = "Users List App")
    parser.add_argument("-a", "--add_user", action="store_true", help="Add a new user")
    parser.add_argument("-lu", "--list_users", action="store_true", help="List all users")
    parser.add_argument("-le", "--list_emails", action="store_true", help="List all emails")
    parser.add_argument("-li", "--list_ids", action="store_true", help="List all IDs")
    parser.add_argument("-r", "--remove_user", metavar="", help="Remove a user by index")
    parser.add_argument("-n", "--username", metavar="", help="Username")
    parser.add_argument("-i", "--user_id", metavar="", help="User ID")
    parser.add_argument("-e", "--user_email", metavar="", help="User Email")
    parser.add_argument("-ed", "--edit_user", action="store_true", help="Edit a user by index")
    return parser


def add_user(username, user_id, user_email):
    with open("users.txt", "a") as file:
        file.write(username + "\n")
    with open("emails.txt", "a") as file:
        file.write(user_email + "\n")
    with open("ids.txt", "a") as file:
        file.write(user_id + "\n")


def list_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("No users found.")


def list_emails():
    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("No emails found.")


def list_ids():
    if os.path.exists("ids.txt"):
        with open("ids.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("No ids found.")


def remove_user(index):
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
        with open("users.txt", "w") as file:
            for i, user in enumerate(users, start=1):
                if i != index:
                    file.write(user)

    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as file:
            emails = file.readlines()
        with open("emails.txt", "w") as file:
            for i, email in enumerate(emails, start=1):
                if i != index:
                    file.write(email)

    if os.path.exists("ids.txt"):
        with open("ids.txt", "r") as file:
            ids = file.readlines()
        with open("ids.txt", "w") as file:
            for i, id in enumerate(ids, start=1):
                if i != index:
                    file.write(id)
        print("User removed successfully.")
    else:
        print("No users found.")


def edit_user(index, username, user_id, user_email):
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
        with open("users.txt", "w") as file:
            for i, user in enumerate(users, start=1):
                if i != index:
                    file.write(user)
                else:
                    file.write(username + "\n")

    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as file:
            emails = file.readlines()
        with open("emails.txt", "w") as file:
            for i, email in enumerate(emails, start=1):
                if i != index:
                    file.write(email)
                else:
                    file.write(user_email + "\n")

    if os.path.exists("ids.txt"):
        with open("ids.txt", "r") as file:
            ids = file.readlines()
        with open("ids.txt", "w") as file:
            for i, id in enumerate(ids, start=1):
                if i != index:
                    file.write(id)
                else:
                    file.write(user_id + "\n")
        print("User edited successfully.")
    else:
        print("No users found.")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add_user:
        add_user(args.username, args.user_id, args.user_email)
    elif args.list_users:
        list_users()
    elif args.list_emails:
        list_emails()
    elif args.list_ids:
        list_ids()
    elif args.remove_user:
        remove_user(int(args.remove_user))
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 