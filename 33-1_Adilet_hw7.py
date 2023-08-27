import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(connection, products):
    sql = '''INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_quantity(connection, products):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_price(connection, products):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limit(connection):
    sql = '''SELECT * FROM products 
    WHERE price <= 100 AND quantity > 5'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_product(connection, name):
    sql = '''SELECT * FROM products 
    WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + name + '%',))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection1 = create_connection('''hw.db''')
if connection1 is not None:
    print('Successfully connected!')
    # create_table(connection1, sql_to_create_products_table)
    # insert_products(connection1, ('Смартфон Xiaomi Redmi Note 10', 250, 12))
    # insert_products(connection1, ('Ноутбук HP Pavilion 15', 800, 3))
    # insert_products(connection1, ('Фотоаппарат Canon EOS 80D', 1000, 10))
    # insert_products(connection1, ('Телевизор Samsung 55" 4K Smart TV', 600, 25))
    # insert_products(connection1, ('Наушники Sony WH-1000XM4', 350, 128))
    # insert_products(connection1, ('Кофемашина DeLonghi Magnifica', 450, 50))
    # insert_products(connection1, ('Спортивные кроссовки Nike Air Max 270', 200, 56))
    # insert_products(connection1, ('Планшет Apple iPad Air', 780, 17))
    # insert_products(connection1, ('Камера GoPro Hero 9 Black', 800, 20))
    # insert_products(connection1, ('Блендер Vitamix E310', 350, 15))
    # insert_products(connection1, ('Смарт-часы Apple Watch Series 6', 400, 10))
    # insert_products(connection1, ('Геймпад Xbox Wireless Controller', 80, 41))
    # insert_products(connection1, ('Парфюм Chanel Coco Mademoiselle', 150, 27))
    # insert_products(connection1, ('Кастрюля Tefal Ingenio', 50, 4))
    # insert_products(connection1, ('Электрическая зубная щетка Oral-B Pro 1000', 40, 34))

    # update_products_quantity(connection1, (5, 1))
    # update_products_price(connection1, (200, 1))
    # delete_product(connection1, 14)
    # select_all_products(connection1)
    # select_products_by_limit(connection1)
    # search_product(connection1, 'Ноутбук')
    connection1.close()
