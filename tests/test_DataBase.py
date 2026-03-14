



# Тест для проверки количества столбцов в таблице
def test_column_count(db_cursor):
    db_cursor.execute('SELECT table_info(users_test)')
    columns = db_cursor.fetchall()
    assert len(columns) == 3 # мы ожидаем три столбца: id, name, age



# Тест для проверки наличия таблицы в базе данных
def test_table_existence(db_cursor) :
    db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users_test';")
    result = db_cursor.fetchone()
    assert result is not None



# Тест для проверки типа данных в столбце
def test_column_type(db_cursor):
    db_cursor.execute('PRAGMA table_info(users_test)')
    columns = db_cursor.fetchall()
    for column in columns:
        if column [1] == 'name':
            assert column [2] == 'TEXT'
        elif column [1] == 'age':
            assert column [2] == 'INTEGER'