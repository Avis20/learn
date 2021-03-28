from collections import namedtuple

UserInfo = namedtuple("UserInfo", ["user_name", "email", "age", "gender"])
print(UserInfo)


def get_user_data(data) -> UserInfo:
    user_name = "test name"
    age = 25
    email = "test@test.com"
    gender = "M"
    user_info = UserInfo(user_name=user_name, age=age,
                         email=email, gender=gender)
    return user_info


def fetch_and_save_user():
    data = {}
    user_info = get_user_data(data)
    print(user_info)
    print(user_info[0])
    name, age, email, gender = user_info
    print(name, age, email, gender)
    print("name =", user_info.user_name, "age =", user_info.age)

if __name__ == "__main__":
    fetch_and_save_user()
