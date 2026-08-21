import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from database.players import (
    create_player,
    get_player_by_user_id,
    save_player,
)
from database.setup import create_tables
from database.users import create_user
from game.player import Player
from game.progression import award_xp


class PlayerPersistenceTests(unittest.TestCase):
    def test_xp_and_level_persist_across_sessions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            database_path = Path(temp_dir) / "data" / "game.db"

            with patch("database.connection.DB_PATH", database_path):
                create_tables()

                user_id = create_user(
                    username="test_player",
                    email="test@example.com",
                    password_hash="test_hash"
                )

                create_player(user_id, "Test Character")

                player_data = get_player_by_user_id(user_id)
                player = Player(*player_data)

                levels_gained = award_xp(player, 650)
                save_player(player)

                reloaded_data = get_player_by_user_id(user_id)
                reloaded_player = Player(*reloaded_data)

                self.assertEqual(levels_gained, 3)
                self.assertEqual(reloaded_player.xp, 650)
                self.assertEqual(reloaded_player.level, 4)

                self.assertEqual(reloaded_player.strength, 10)
                self.assertEqual(reloaded_player.defence, 10)
                self.assertEqual(reloaded_player.speed, 10)
                self.assertEqual(reloaded_player.dexterity, 10)


if __name__ == "__main__":
    unittest.main()
