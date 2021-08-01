import sys
import pitchers
import batters

BATTER = "B"
PITCHER = "P"

def main():

    batters_list = []
    pitchers_list = []

    if sys.argv[1] == BATTER:
        batters_list = batters.parse_batters(sys.argv[2])
    elif sys.argv[1] == PITCHER:
        pitchers_list = pitchers.parse_pitchers(sys.argv[2])
    else:
        print("Player type invalid: ", sys.argv[1])

if __name__ == '__main__':
    main()
