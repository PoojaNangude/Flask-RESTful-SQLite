import sqlite3

def find_by_name(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * from items WHERE name = ?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.close()

    if row:
        return {'item': {'name': row[0], 'price': row[1]}}


def insert(item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO items VALUES (?,?)"
    cursor.execute(query, (item['name'], item['price']))

    connection.commit()
    connection.close()


def update(item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "UPDATE items SET price=? WHERE name=?"
    cursor.execute(query, (item['price'], item['name']))

    connection.commit()
    connection.close()
