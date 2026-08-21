import unittest
from types import SimpleNamespace
from unittest.mock import patch

from game.crimes import commit_crime
from game.gym import train


class GymTests(unittest.TestCase):
    def setUp(self):
        self.player = SimpleNamespace(
            energy=100,
            strength=10,
            defence=10,
            speed=10,
            dexterity=10,
        )

    def test_strength_training_updates_strength(self):
        train(self.player, "strength")

        self.assertEqual(self.player.strength, 12)
        self.assertEqual(self.player.energy, 90)

    def test_dexterity_training_updates_dexterity(self):
        train(self.player, "dexterity")

        self.assertEqual(self.player.dexterity, 12)
        self.assertEqual(self.player.energy, 90)


class CrimeTests(unittest.TestCase):
    @patch("game.crimes.random.randint", side_effect=[100, 10])
    def test_failed_crime_does_not_make_health_negative(self, _randint):
        player = SimpleNamespace(nerve=20, money=0, health=5)

        commit_crime(
            player,
            name="Test crime",
            nerve_cost=2,
            success_chance=0,
            min_reward=1,
            max_reward=1,
        )

        self.assertEqual(player.health, 0)
        self.assertEqual(player.nerve, 18)


if __name__ == "__main__":
    unittest.main()
