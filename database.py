import sqlite3

db_name = 'business.db'
conn = sqlite3.connect(db_name, check_same_thread=False)
cursor = conn.cursor()

# Ініціалізація таблиць
def initialize_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS web_orders(
                order_id INTEGER PRIMARY KEY,
                service_name TEXT,
                user_name TEXT,
                email TEXT,
                phone TEXT,
                details TEXT
            )
        ''')
    conn.commit()

# Збереження замовлення
def save_order(service_name, user_name, email, phone, details):
    print(f"Saving order: {service_name}, {user_name}, {email}, {phone}, {details}")
    cursor.execute('''
    INSERT INTO web_orders (service_name, user_name, email, phone, details)
    VALUES (?, ?, ?, ?, ?)
    ''', (service_name, user_name, email, phone, details))
    conn.commit()

# Виконання ініціалізації таблиць
initialize_tables()
