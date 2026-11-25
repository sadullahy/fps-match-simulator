from models import Player
from engine import MatchEngine

team_a = [Player("Sadullah", "Team A"), Player("Nathen", "Team A")]
team_b = [Player("Bot_1", "Team B"), Player("Bot_2", "Team B")]

match = MatchEngine(team_a, team_b)

print("=== MATCH START ===")
for r in range(1, 6):
    winner = match.simulate_round(r)
    p1 = team_a[0]
    weapon_name = p1.weapon.name if p1.weapon else "Unarmed"
    print(f"Round {r} | Winner: {winner} | Score: {match.score} | {p1.name}: ${p1.money} ({weapon_name})")