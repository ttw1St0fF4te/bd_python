from Admin import AdminDB
from Client import ClientsDB
from Employee import EmployeesDB
from Products import ProductsDB
from User import UsersDB

def main():
    users_db = UsersDB()
    admin_db = AdminDB()

    while True:
        print("1. Вход")
        print("2. Регистрация")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")

            user = users_db.login_user(username, password)
            if user:
                print("Вход успешен!")
                user_id, username, _, role = user
                if role == "client":
                    client_actions(user_id)
                elif role == "employee":
                    employee_actions(user_id)
                elif role == "admin":
                    admin_actions()
            else:
                print("Неверное имя пользователя или пароль.")

        elif choice == "2":
            username = input("Введите новое имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (client, employee, admin): ")

            users_db.register_user(username, password, role)
            print("Пользователь зарегистрирован!")

        elif choice == "3":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    users_db.close_connection()
    admin_db.close_connection()

def client_actions(user_id):
    clients_db = ClientsDB()
    products_db = ProductsDB()

    while True:
        print("\n1. Просмотреть заказы")
        print("2. Изменить профиль")
        print("3. Заказать продукт")
        print("4. Выйти")
        client_choice = input("Выберите действие: ")

        if client_choice == "1":
            orders = clients_db.get_client_orders(user_id)
            print("Ваши заказы:")
            for order in orders:
                print(f"{order[0]} - ${order[1]}")

        elif client_choice == "2":
            full_name = input("Введите новое полное имя: ")
            email = input("Введите новый email: ")
            phone_number = input("Введите новый номер телефона: ")
            clients_db.update_client_profile(user_id, full_name, email, phone_number)
            print("Профиль обновлен!")

        elif client_choice == "3":
            print("Доступные продукты:")
            products = products_db.get_all_products()
            for product in products:
                print(f"{product[0]}. {product[1]} - ${product[2]}")

            product_id = int(input("Введите ID продукта для заказа: "))
            clients_db.add_order_to_client(user_id, product_id)
            print("Продукт добавлен в заказ!")

        elif client_choice == "4":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    clients_db.close_connection()

def employee_actions(user_id):
    employees_db = EmployeesDB()
    products_db = ProductsDB()

    while True:
        print("\n1. Просмотреть все продукты")
        print("2. Добавить новый продукт")
        print("3. Выйти")
        employee_choice = input("Выберите действие: ")

        if employee_choice == "1":
            products = products_db.get_all_products()
            print("Все продукты:")
            for product in products:
                print(f"{product[0]}. {product[1]} - ${product[2]}")

        elif employee_choice == "2":
            name = input("Введите название продукта: ")
            price = float(input("Введите цену продукта: "))
            products_db.add_product(name, price)
            print("Продукт добавлен!")

        elif employee_choice == "3":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    employees_db.close_connection()

def admin_actions():
    admin_db = AdminDB()
    users_db = UsersDB()

    while True:
        print("\n1. Удалить пользователя")
        print("2. Изменить данные пользователя")
        print("3. Выйти")
        admin_choice = input("Выберите действие: ")

        if admin_choice == "1":
            user_id = int(input("Введите ID пользователя для удаления: "))
            admin_db.delete_user(user_id)
            print("Пользователь удален!")

        elif admin_choice == "2":
            user_id = int(input("Введите ID пользователя для изменения данных: "))
            username = input("Введите новое имя пользователя: ")
            password = input("Введите новый пароль: ")
            role = input("Введите новую роль: ")
            admin_db.update_user(user_id, username, password, role)
            print("Данные пользователя обновлены!")

        elif admin_choice == "3":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

    admin_db.close_connection()

if __name__ == "__main__":
    main()