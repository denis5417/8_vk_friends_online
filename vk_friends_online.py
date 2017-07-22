import vk
import sys


def get_auth_session(app_id, login, password):
    session = vk.AuthSession(app_id=app_id, user_login=login, user_password=password, scope='friends')
    return session


def get_online_friends_ids(api):
    return api.friends.getOnline()


def get_names_by_ids(friend_id, api):
    return api.users.get(user_ids=friend_id)


def output_friends_to_console(friends_online_names):
    for friend_online_name in friends_online_names:
        print("{} {}".format(friend_online_name['first_name'], friend_online_name['last_name']))


def load_oauth_credentials_from_file(credentials_filepath):
    with open(credentials_filepath) as crfile:
        app_id, login, password = crfile.read().strip().split("\n")
    return app_id, login, password


def get_api(session):
    api = vk.API(session)
    return api


def main():
    if len(sys.argv) < 2:
        print("Использование: $ python3 vk_friends_online.py <path_to_file_with_credentials>")
        return None
    credentials_filepath = sys.argv[1]
    app_id, login, password = load_oauth_credentials_from_file(credentials_filepath)
    try:
        session = get_auth_session(app_id, login, password)
    except vk.exceptions.VkAuthError:
        print("Неправильный логин, пароль или app_id")
        return None
    api = get_api(session)
    friends_online_ids = get_online_friends_ids(api)
    friends_online_names = get_names_by_ids(friends_online_ids, api)
    output_friends_to_console(friends_online_names)


if __name__ == '__main__':
    main()
