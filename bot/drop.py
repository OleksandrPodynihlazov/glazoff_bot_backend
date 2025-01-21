import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('business.db')
cursor = conn.cursor()

# Видалення таблиці
table_name = "pages"
cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
conn.commit()

print(f"Таблиця '{table_name}' була успішно видалена.")

# Закриття з'єднання
conn.close()
