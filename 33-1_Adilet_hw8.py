import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def display_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()
        for city in cities:
            print(f"{city[0]}. {city[1]}")
    except sqlite3.Error as e:
        print(e)


def display_employees(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area
            FROM employees
            JOIN cities ON employees.city_id = cities.id
            JOIN countries ON cities.country_id = countries.coun_id
            WHERE employees.city_id = ?
        """, (city_id,))
        employees = cursor.fetchall()
        for employee in employees:
            print(
                f"Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город: {employee[3]}, Площадь "
                f"города: {employee[4]}")
    except sqlite3.Error as e:
        print(e)


connection = create_connection('''HW_8.db''')
if connection is not None:
    print('Successfully connected!')

    while True:
        print(
            "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из "
            "программы введите 0:")
        display_cities(connection)
        user_input = input("Введите id города: ")

        if user_input == '0':
            break

        try:
            city_id = int(user_input)
            display_employees(connection, city_id)
        except ValueError:
            print("Введите корректный id города.")

    connection.close()