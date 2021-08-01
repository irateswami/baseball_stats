import csv
import statistics

NAME = "Name"
PLAYERID = "playerid"
WHIP = "WHIP"
ERA = "ERA"
K = "K"
WINS = "WINS"

class Pitcher:
    def __init__(self, name, id, wins, sv, k, era, whip):
        self.name = name
        self.id = id
        self.wins = wins
        self.sv = sv
        self.k = k
        self.era = era
        self.whip = whip
        self.zscore = 0.0

    def __str__(self):
        return self.name + " | " + self.id+ " | " +self.wins+ " | " +self.sv+ " | " +self.k+ " | " +self.era+ " | " +self.whip

def parse_pitchers(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        total_wins= 0
        total_sv = 0
        total_k = 0
        total_era = 0
        total_whip = 0

        for row in reader:
            print(row[SB])