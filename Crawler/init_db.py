import sqlite3
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


def initialize_database():
    # Connect to SQLite database (creates a new database if it doesn't exist)
    connection = sqlite3.connect(config["result"]['db'])

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_record (
            crawl_date DATETIME,
            keyword CHAR (10) NOT NULL,
            num_records INTEGER NOT NULL,
            filename CHAR NOT NULL
        )
    ''')
    # Commit the changes and close the connection
    connection.commit()
    connection.close()


if __name__ == '__main__':
    initialize_database()
