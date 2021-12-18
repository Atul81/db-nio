import sqlite3
# import names
import requests
import redis

db = sqlite3.connect(":memory:")
# db = sqlite3.connect("sqlite.db")
URL = 'https://api.namefake.com/'
cursor = db.cursor()

CREATE_DB = """
"""

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS projects(
        id integer PRIMARY KEY,
        name text NOT NULL);
"""
INSERT_STATEMENT = """
INSERT INTO projects (name) values ("{}");
""".format(requests.get(URL).json()['name'])


def main():
    cursor.execute(CREATE_TABLE)
    cursor.execute(INSERT_STATEMENT)
    db.commit()
    db.close()


if __name__ == '__main__':
    main()
