from database.connection import get_connection


def create_player(user_id, name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO players (user_id, name)
        VALUES (?, ?)
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
            nerve
        FROM players
        WHERE user_id = ?
        """,
        (user_id,)
    )

    player = cursor.fetchone()

    conn.close()

    return player

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
            nerve = ?
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
            player.id
        )
    )

    conn.commit()
    conn.close()