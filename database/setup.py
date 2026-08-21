from database.connection import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            name TEXT NOT NULL,
            level INTEGER DEFAULT 1,
            money INTEGER DEFAULT 500,
            health INTEGER DEFAULT 100,
            energy INTEGER DEFAULT 100,
            strength INTEGER DEFAULT 10,
            defence INTEGER DEFAULT 10,
            speed INTEGER DEFAULT 10,
            dexterity INTEGER DEFAULT 10,
            nerve INTEGER DEFAULT 20,
            max_energy INTEGER NOT NULL DEFAULT 100,
            max_nerve INTEGER NOT NULL DEFAULT 20,
            last_energy_update TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_nerve_update TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id)
                REFERENCES users(id)
                ON DELETE CASCADE
        )
    """)

    
    conn.commit()
    conn.close()