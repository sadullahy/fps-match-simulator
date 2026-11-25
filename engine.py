import random
from models import Weapon


class MatchEngine:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.score = {"Team A": 0, "Team B": 0}
        self.loss_streak = {"Team A": 0, "Team B": 0}
        self.rifle = Weapon("Vandal/AK-47", 2900, 100)

    def _buy_phase(self):
        for p in self.team_a + self.team_b:
            if getattr(p, "weapon", None) is None and p.money >= self.rifle.cost:
                p.buy_weapon(self.rifle)

    def simulate_round(self, round_num):
        self._buy_phase()

        winner = random.choice(["Team A", "Team B"])
        loser = "Team B" if winner == "Team A" else "Team A"

        self.score[winner] += 1
        self.loss_streak[winner] = 0
        self.loss_streak[loser] = min(self.loss_streak[loser] + 1, 3)

        loser_payout = 1900 + (self.loss_streak[loser] - 1) * 500
        for p in self.team_a + self.team_b:
            if p.team == winner:
                p.money = min(p.money + 3000, 9000)
            else:
                p.money = min(p.money + loser_payout, 9000)
                p.weapon = None

        return winner