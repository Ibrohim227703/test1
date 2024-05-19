import psycopg2

db_name = 'n47'
password = '123'
host = 'localhost'
port = 5432
user = 'postgres'


def connect_to_db():
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn


def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            image VARCHAR(255),
            is_liked BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


def create_table_1():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User ()
        id: SERIAL PRIMARY KEY,
        firstName: VARCHAR(255) NOT NULL,
        familiya: VARCHAR(255) NOT NULL,
        maidenName: VARCHAR(255) NOT NULL,
        yosh: INT ,
        jins: VARCHAR(255) NOT NULL,
        elektron pochta: VARCHAR(255) NOT NULL,
        telefon: INT,
        username: VARCHAR(255) NOT NULL,
        password: VARCHAR(255) NOT NULL,
        tugilgan sana: VARCHAR(255) NOT NULL,
        rasm : VARCHAR(255) NOT NULL,
        bloodGroup: VARCHAR(255) NOT NULL,
        height: FLOAT NOT NULL,
        weight: FLOAT NOT NULL,
    }


    """)
    conn.commit()
    conn.close()


def insert_products_data_1(firstName=None, rasm=None):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO User (firstName,  rasm)
        VALUES (%s, %s)
    """, (firstName, rasm))
    conn.commit()
    conn.close()


def insert_products_data(name, image):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Products (name, image)
        VALUES (%s, %s)
    """, (name, image))
    conn.commit()
    conn.close()


def select_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_data(product_id, new_name, new_image):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Products
        SET name = %s, image = %s, updated_at = CURRENT_TIMESTAMP
        WHERE id = %s
    """, (new_name, new_image, product_id))
    conn.commit()
    conn.close()


def delete_data(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Products
        WHERE id = %s
    """, (product_id,))
    conn.commit()
    conn.close()


create_table()
insert_products_data("Product 1", "image1.jpg")
insert_products_data("Product 2", "image2.jpg")
print("Inserted data:")
print(select_data())
update_data(1, "Updated Product 1", "updated_image1.jpg")
print("After update:")
print(select_data())
delete_data(2)
print("After delete:")
print(select_data())
