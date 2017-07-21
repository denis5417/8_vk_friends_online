import vk
import sys


def get_app_id():
    return sys.argv[1]


def get_user_login():
    return sys.argv[2]


def get_user_password():
    return sys.argv[3]


def get_auth_session(app_id, login, password):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
    )
    return session


def get_online_friends(session):
    api = vk.API(session)
    return api.friends.get(fields="first_name, last_name, online")


def output_friends_to_console(friends_online):
    for friend in friends_online:
        if friend['online']:
            print("{} {}".format(friend['first_name'], friend['last_name']))


def main():
    if len(sys.argv) < 4:
        print("Использование: $ python3 vk_friends_online.py <app_id> <login> <password>")
        return None
    app_id = get_app_id()
    login = get_user_login()
    password = get_user_password()
    try:
        session = get_auth_session(app_id, login, password)
    except vk.exceptions.VkAuthError:
        print("Неправильный логин, пароль или app_id")
        return None
    friends_online = get_online_friends(session)
    output_friends_to_console(friends_online)


if __name__ == '__main__':
    main()
