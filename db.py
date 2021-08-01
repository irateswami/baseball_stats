import sqlite3
from sqlite3 import Error

import batters
import pitchers 

batters_daily_table= """ CREATE TABLE IF NOT EXISTS batters_daily (
                                     iddate text PRIMARY KEY,
                                     id text NOT NULL,
                                     date text NOT NULL,
                                     zscore real NOT NULL,
                                     FOREIGN KEY (id) REFERENCES player_names(id)); """

player_names_table= """CREATE TABLE IF NOT EXISTS player_names (
                                    id text PRIMARY KEY,
                                    name text NOT NULL);"""

player_index="CREATE INDEX stat_date ON batters_daily(date)"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)