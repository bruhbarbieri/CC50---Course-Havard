import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python worldcup.py FILENAME")

    teams = []
    teams = [0 for i in range(16)]
    with open(f"{sys.argv[1]}","r") as data:
        data_dict = csv.DictReader(data, delimiter=",")
        i = 0
        for line in data_dict:
            teams[i] = line
            teams[i]['rating'] = int(teams[i]['rating'])
            i += 1

    counts = {}
    for i in range(len(teams)):
        counts[f'{teams[i]["team"]}'] = 0
    for i in range(N):
        winner = simulate_tournament(teams)
        counts[f"{winner}"] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    survivors = simulate_round(teams)
    if len(survivors) > 1:
        winner = simulate_tournament(survivors)
    else:
        winner = survivors
        return winner[0]["team"]
    return winner


if __name__ == "__main__":
    main()