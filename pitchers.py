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
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        total_wins = []
        total_sv = []
        total_k = []
        total_era = []
        total_whip = []
        pitchers = []

        for row in reader:
            new_batter = Batter(row[NAME], row[PLAYERID], 
                int(row[WINS]), 
                int(row[SV]), 
                int(row[K]), 
                int(row[ERA]), 
                float(row[WHIP]))
            total_wins.append(int(row[WINS]))
            total_sv.append(int(row[SV]))
            total_k.append(int(row[K]))
            total_era.append(int(row[ERA]))
            total_whip.append(float(row[WHIP]))
            batters.append(new_batter)

        mean_wins = statistics.mean(total_wins)
        mean_sv = statistics.mean(total_sv)
        mean_k = statistics.mean(total_k)
        mean_era = statistics.mean(total_era)
        mean_whip = statistics.mean(total_whip)

        pstdev_wins = statistics.pstdev(total_wins)
        pstdev_sv = statistics.pstdev(total_sv)
        pstdev_k = statistics.pstdev(total_k)
        pstdev_era = statistics.pstdev(total_era)
        pstdev_whip = statistics.pstdev(total_whip)

        for batter in batters:
            batter.zscore += (batter.wins - mean_wins)/pstdev_wins
            batter.zscore += (batter.sv - mean_sv)/pstdev_sv
            batter.zscore += (batter.k - mean_k)/pstdev_k
            batter.zscore += (batter.era - mean_era)/pstdev_era
            batter.zscore += (batter.whip - mean_whip)/pstdev_whip
        
        return batters