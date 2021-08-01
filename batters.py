import csv
import statistics

NAME = "Name"
PLAYERID = "playerid"
HOMERUNS = "HR"
RUNS = "R"
RBI = "RBI"
SB = "SB"
AVG = "AVG"

class Batter:
    def __init__(self, name, id, homeruns, runs, rbi, sb, avg):
        self.name = name
        self.id = id
        self.homeruns = homeruns
        self.runs = runs
        self.rbi = rbi
        self.sb = sb
        self.avg = avg 
        self.zscore = 0.0

    def __str__(self):
        return self.name + " | " + self.id+ " | " +self.homeruns+ " | " +self.runs+ " | " +self.rbi+ " | " +self.sb+ " | " +self.avg

def parse_batters(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        total_homeruns = []
        total_runs = []
        total_rbi = []
        total_sb = []
        total_avg = []
        batters = []

        for row in reader:
            new_batter = Batter(row[NAME], row[PLAYERID], 
                int(row[HOMERUNS]), 
                int(row[RUNS]), 
                int(row[RBI]), 
                int(row[SB]), 
                float(row[AVG]))
            total_homeruns.append(int(row[HOMERUNS]))
            total_runs.append(int(row[RUNS]))
            total_rbi.append(int(row[RBI]))
            total_sb.append(int(row[SB]))
            total_avg.append(float(row[AVG]))
            batters.append(new_batter)

        mean_homeruns = statistics.mean(total_homeruns)
        mean_runs = statistics.mean(total_runs)
        mean_rbi = statistics.mean(total_rbi)
        mean_sb = statistics.mean(total_sb)
        mean_avg = statistics.mean(total_avg)

        pstdev_homeruns = statistics.pstdev(total_homeruns)
        pstdev_runs = statistics.pstdev(total_runs)
        pstdev_rbi = statistics.pstdev(total_rbi)
        pstdev_sb = statistics.pstdev(total_sb)
        pstdev_avg = statistics.pstdev(total_avg)

        for batter in batters:
            batter.zscore += (batter.homeruns - mean_homeruns)/pstdev_homeruns
            batter.zscore += (batter.runs - mean_runs)/pstdev_runs
            batter.zscore += (batter.rbi - mean_rbi)/pstdev_rbi
            batter.zscore += (batter.sb - mean_sb)/pstdev_sb
            batter.zscore += (batter.avg - mean_avg)/pstdev_avg
        
        return batters