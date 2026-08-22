import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from game.crimes import commit_crime, get_crime
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
    def test_failed_crime_does_not_make_health_negative(self):
        player = SimpleNamespace(
            nerve=20,
            money=0,
            health=5,
            xp=0,
            level=1,
        )
        rng = Mock()
        rng.randint.side_effect = [100, 10]

        result = commit_crime(
            player,
            get_crime("camden_shoplift"),
            rng=rng,
        )

        self.assertEqual(player.health, 0)
        self.assertEqual(player.nerve, 18)
        self.assertFalse(result.success)
        self.assertEqual(result.damage, 10)

    def test_successful_crime_awards_money_xp_and_level(self):
        player = SimpleNamespace(
            nerve=20,
            money=0,
            health=100,
            xp=95,
            level=1,
        )
        rng = Mock()
        rng.randint.side_effect = [1, 40]

        result = commit_crime(
            player,
            get_crime("camden_shoplift"),
            rng=rng,
        )

        self.assertEqual(player.nerve, 18)
        self.assertEqual(player.money, 40)
        self.assertEqual(player.xp, 105)
        self.assertEqual(player.level, 2)
        self.assertTrue(result.success)
        self.assertEqual(result.cash_reward, 40)


if __name__ == "__main__":
    unittest.main()
