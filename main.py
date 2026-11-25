from models import Player
from engine import MatchEngine

team_a = [Player("Sadullah", "Team A"), Player("Nathen", "Team A")]
team_b = [Player("Bot_1", "Team B"), Player("Bot_2", "Team B")]

match = MatchEngine(team_a, team_b)

print("=== MATCH START ===")
for r in range(1, 6):
    winner = match.simulate_round(r)
    status = " | ".join([f"{p.name}: ${p.money} ({p.weapon.name if p.weapon else 'Unarmed'})" for p in team_a])
    print(f"Round {r} | Winner: {winner} | Score: {match.score} | {status}")