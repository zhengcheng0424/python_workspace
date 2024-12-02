import sqlite3


def create_table(db_table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {db_table_name} 
                        (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price DOUBLE)''')
    cursor.execute(f"INSERT INTO {db_table_name} values (?, ?, ?, ?)", (1, 'test_1', 'desc_demo_1', 1.2))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table('item')
