# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # adding all the teams to the
    teams = []
    with open(sys.argv[1]) as file:
        data = csv.DictReader(file)
        for row in data:
            team = {"team": row["team"], "rating": int(row["rating"])}
            teams.append(team)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    counter = 0
    while counter < N:
        winner = simulate_tournament(teams)
        if winner not in counts:
            counts[winner] = 1
        else:
            counts[winner] += 1
        counter += 1

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
    i = 2
    team_number = len(teams) ** 2
    while i <= team_number:
        winners = simulate_round(teams)
        teams = winners
        i = i**2
    winner = winners[0]["team"]
    return winner


if __name__ == "__main__":
    main()
