import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from game.crimes import (
    CRIMES,
    CrimeResult,
    commit_crime,
    get_crime,
)


class CrimeDefinitionTests(unittest.TestCase):
    def test_starter_crimes_cover_each_planned_district(self):
        districts = {crime.district for crime in CRIMES}

        self.assertEqual(districts, {"Camden", "Brixton", "Soho"})
        self.assertEqual(len({crime.key for crime in CRIMES}), len(CRIMES))


class CrimeEngineTests(unittest.TestCase):
    def make_player(self, nerve=20):
        return SimpleNamespace(
            nerve=nerve,
            money=100,
            health=100,
            xp=0,
            level=1,
            crime_progress={},
            district_reputation={},
        )

    def test_success_returns_structured_result_and_progress(self):
        player = self.make_player()
        crime = get_crime("soho_pickpocket")
        rng = Mock()
        rng.randint.side_effect = [1, 75]

        result = commit_crime(player, crime, rng=rng)

        self.assertIsInstance(result, CrimeResult)
        self.assertTrue(result.attempted)
        self.assertTrue(result.success)
        self.assertEqual(result.cash_reward, 75)
        self.assertEqual(player.money, 175)
        self.assertEqual(player.xp, crime.xp_reward)
        self.assertEqual(player.nerve, 16)
        self.assertEqual(
            player.crime_progress[crime.key],
            {
                "xp": crime.crime_xp_reward,
                "attempts": 1,
                "successes": 1,
            },
        )
        self.assertEqual(
            player.district_reputation["Soho"],
            crime.reputation_reward,
        )

    def test_failure_grants_no_cash_xp_or_reputation(self):
        player = self.make_player()
        crime = get_crime("brixton_warehouse")
        rng = Mock()
        rng.randint.side_effect = [100, 8]

        result = commit_crime(player, crime, rng=rng)

        self.assertTrue(result.attempted)
        self.assertFalse(result.success)
        self.assertEqual(result.cash_reward, 0)
        self.assertEqual(player.money, 100)
        self.assertEqual(player.xp, 0)
        self.assertEqual(player.district_reputation, {})
        self.assertEqual(
            player.crime_progress[crime.key],
            {"xp": 0, "attempts": 1, "successes": 0},
        )

    def test_insufficient_nerve_does_not_attempt_or_change_player(self):
        player = self.make_player(nerve=1)
        crime = get_crime("soho_nightclub")
        rng = Mock()

        result = commit_crime(player, crime, rng=rng)

        self.assertFalse(result.attempted)
        self.assertEqual(result.reason, "not_enough_nerve")
        self.assertEqual(player.nerve, 1)
        self.assertEqual(player.money, 100)
        self.assertEqual(player.crime_progress, {})
        rng.randint.assert_not_called()


if __name__ == "__main__":
    unittest.main()
