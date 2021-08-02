import sys
import pitchers
import batters
import db

BATTER = "B"
PITCHER = "P"

def main():

    batters_list = []
    pitchers_list = []
    player_names = []

    db_string = "./baseball.db"

    conn = db.create_connection(db_string)
    db.create_table(conn, db.player_names_table)
    db.create_table(conn, db.player_daily_table)

    if sys.argv[1] == BATTER:
        batters_list = batters.parse_batters(sys.argv[2])
        db.insert_players_daily(conn, batters_list)

    elif sys.argv[1] == PITCHER:
        pitchers_list = pitchers.parse_pitchers(sys.argv[2])
        db.insert_players_daily(conn, pitchers_list)


    else:
        print("Player type invalid: ", sys.argv[1])

if __name__ == '__main__':
    main()
