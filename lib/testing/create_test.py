import sqlite3
import os

# Determine the correct path to the SQL file
sql_file_path = os.path.join(os.path.dirname(__file__), 'lib', 'create.sql')

# Debug: Print the current working directory and the SQL file path
print(f"Current Working Directory: {os.getcwd()}")
print(f"SQL File Path: {sql_file_path}")

# Check if the file exists at the specified path
if not os.path.exists(sql_file_path):
    raise FileNotFoundError(f"File not found: {sql_file_path}")

# Initialize the SQLite in-memory database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Read and execute the SQL script
with open(sql_file_path, 'r') as sql_file:
    sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

class TestCreate:
    '''Statement in create.sql'''

    def test_creates_bears_with_name_column(self):
        '''creates a table "bears" with a column "name".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "name" in columns

    def test_creates_bears_with_age_column(self):
        '''creates a table "bears" with a column "age".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "age" in columns

    def test_creates_bears_with_sex_column(self):
        '''creates a table "bears" with a column "sex".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "sex" in columns

    def test_creates_bears_with_color_column(self):
        '''creates a table "bears" with a column "color".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "color" in columns

    def test_creates_bears_with_temperament_column(self):
        '''creates a table "bears" with a column "temperament".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "temperament" in columns

    def test_creates_bears_with_alive_column(self):
        '''creates a table "bears" with a column "alive".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert "alive" in columns

    def test_creates_bears_with_id_pk(self):
        '''creates a table "bears" with a primary key "id".'''
        columns = [column for column in cursor.execute("PRAGMA table_info(bears);")]
        primary_key_column = next((col for col in columns if col[5] == 1), None)
        assert primary_key_column is not None and primary_key_column[1] == "id"

print(os.getcwd())