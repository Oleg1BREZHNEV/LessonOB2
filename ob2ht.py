class User:
    def __init__(self, ID, name, access_level='user'):
        self.__ID = ID
        self.__name = name
        self.__access_level = access_level

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, ID, name, access_level='admin'):
        super().__init__(ID, name, access_level)
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
        else:
            print("User not found in the list.")

    def get_users(self):
        return self.__users


# Пример использования программы
# Создаем несколько пользователей
user1 = User(1, 'Олег')
user2 = User(2, 'Саша')
user3 = User(3, 'Варя')

# Создаем администратора
admin = Admin(0, 'Нина')

# Добавляем пользователей в список пользователей администратора
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Удаляем пользователя из списка пользователей администратора
admin.remove_user(user2)

# Выводим список пользователей
users = admin.get_users()
for user in users:
    print(user.get_name())