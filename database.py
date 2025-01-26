import sqlite3

db_name = 'business.db'
conn = sqlite3.connect(db_name, check_same_thread=False)
cursor = conn.cursor()

# Ініціалізація таблиць
def initialize_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS web_orders(
                order_id INTEGER PRIMARY KEY,
                telegram_id INTEGER,
                service_name TEXT,
                details TEXT,
                order_date TEXT,
                FOREIGN KEY(telegramId) REFERENCES users(telegramId)
            )
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
                telegramId INTEGER PRIMARY KEY,
                user_name TEXT,
                email TEXT,
                phone TEXT,
                tgFullname TEXT,
                tgUsername TEXT
                   
            )
        ''')
    conn.commit()

# Збереження замовлення
def save_order(telegram_id,service_name, details,order_date):
    print(f"Saving order:{telegram_id}, {service_name},{details},{order_date}")
    cursor.execute('''
    INSERT INTO web_orders (telegram_id,service_name, details, order_date)
    VALUES (?, ?, ?, ?)
    ''',( telegram_id,service_name, details, order_date))
def save_user(telegram_id,user_name, email, phone, tgFullname,tgUsername):
    cursor.execute('''INSERT OR REPLACE INTO users (telegram_id,user_name,tgUsername,tgFullname, phone, email)
            VALUES(?, ?, ?, ?, ?)''', ( telegram_id,user_name,email,phone,tgFullname,tgUsername))
    conn.commit()

# Виконання ініціалізації таблиць
initialize_tables()
