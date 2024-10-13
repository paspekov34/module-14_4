import sqlite3

def initiate_db():
  """Создает таблицу Products, если она еще не создана."""
  connection = sqlite3.connect('products.db')
  cursor = connection.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEST,
    price INTEGER NOT NULL
  )
  ''')

  for i in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)',
                   (f'title{i}', f'description{i}', 'price'))
  connection.commit()
  connection.close()


def get_all_products():
  """Возвращает все записи из таблицы Products."""
  connection = sqlite3.connect('products.db')
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM Products")
  products = cursor.fetchall()
  connection.close()
  return products
