from datetime import datetime, timezone

from database.connection import get_connection
from game.regeneration import (
    ENERGY_POINTS_PER_TICK,
    ENERGY_TICK_SECONDS,
    NERVE_POINTS_PER_TICK,
    NERVE_TICK_SECONDS,
    regenerate_resource,
)


def create_player(user_id, name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO players (
            user_id,
            name,
            nerve,
            max_energy,
            max_nerve,
            last_energy_update,
            last_nerve_update
        )
        VALUES (?, ?, 20, 100, 20, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """,
        (user_id, name)
    )

    conn.commit()
    player_id = cursor.lastrowid
    conn.close()

    return player_id


def get_player_by_user_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            user_id,
            name,
            level,
            money,
            health,
            energy,
            strength,
            defence,
            speed,
            dexterity,
            nerve,
            max_energy,
            max_nerve,
            last_energy_update,
            last_nerve_update,
            xp
        FROM players
        WHERE user_id = ?
        """,
        (user_id,)
    )

    player_data = cursor.fetchone()

    if player_data is None:
        conn.close()
        return None

    player_data = list(player_data)
    now = datetime.now(timezone.utc)

    energy, energy_update = regenerate_resource(
        current_value=player_data[6],
        maximum_value=player_data[12],
        last_update=player_data[14],
        points_per_tick=ENERGY_POINTS_PER_TICK,
        tick_seconds=ENERGY_TICK_SECONDS,
        now=now
    )

    nerve, nerve_update = regenerate_resource(
        current_value=player_data[11],
        maximum_value=player_data[13],
        last_update=player_data[15],
        points_per_tick=NERVE_POINTS_PER_TICK,
        tick_seconds=NERVE_TICK_SECONDS,
        now=now
    )

    cursor.execute(
        """
        UPDATE players
        SET
            energy = ?,
            nerve = ?,
            last_energy_update = ?,
            last_nerve_update = ?
        WHERE id = ?
        """,
        (
            energy,
            nerve,
            energy_update,
            nerve_update,
            player_data[0]
        )
    )

    conn.commit()
    conn.close()

    player_data[6] = energy
    player_data[11] = nerve
    player_data[14] = energy_update
    player_data[15] = nerve_update

    return tuple(player_data)


def save_player(player):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE players
        SET
            name = ?,
            level = ?,
            money = ?,
            health = ?,
            energy = ?,
            strength = ?,
            defence = ?,
            speed = ?,
            dexterity = ?,
            nerve = ?,
            max_energy = ?,
            max_nerve = ?,
            last_energy_update = ?,
            last_nerve_update = ?,
            xp = ?
        WHERE id = ?
        """,
        (
            player.name,
            player.level,
            player.money,
            player.health,
            player.energy,
            player.strength,
            player.defence,
            player.speed,
            player.dexterity,
            player.nerve,
            player.max_energy,
            player.max_nerve,
            player.last_energy_update,
            player.last_nerve_update,
            player.xp,
            player.id
        )
    )

    conn.commit()
    conn.close()