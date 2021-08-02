import sqlite3
import textwrap

from  datetime import date
from sqlite3 import Error

import batters
import pitchers 

player_daily_table= """ CREATE TABLE IF NOT EXISTS players_daily (
                                     iddate text PRIMARY KEY,
                                     id text NOT NULL,
                                     date text NOT NULL,
                                     zscore real NOT NULL,
                                     FOREIGN KEY (id) REFERENCES player_names(id)); """

player_names_table= """CREATE TABLE IF NOT EXISTS player_names (
                                    id text PRIMARY KEY,
                                    name text NOT NULL);"""

def parenthise(str):
    return "'" + str + "'"

def insert_players_daily(conn, players):
    c = conn.cursor()
    for batter in players:
        query = """INSERT OR REPLACE INTO players_daily 
                    (iddate, id, date, zscore) VALUES
                    (iddate_value, id_value, date_value, zscore_value)"""
        
        query = query.replace("iddate_value", parenthise(str(batter.id)+str(date.today())))
        query = query.replace("id_value", parenthise(str(batter.id)))
        query = query.replace("date_value", parenthise(str(date.today())))
        query = query.replace("zscore_value", str(batter.zscore))

        #print(query)

        c.execute(query)
        conn.commit()


def insert_player_names(conn, players):
    c = conn.cursor()
    for player in players:

        query = "INSERT OR REPLACE INTO player_names (id, name) VALUES(id_val, name_val)"
        query = query.replace("id_val", str(player.id))
        query = query.replace("name_val", player.name.replace("'","''"))
        
        #print(query)

        c.execute(query)
        conn.commit()


def create_date_index(conn):
    c = conn.cursor()
    c.execute("CREATE INDEX IF NOT EXISTS stat_date ON batters_daily(date)")
    # TODO same for pitchers

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