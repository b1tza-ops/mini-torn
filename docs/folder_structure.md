# The Smoke — Planned Backend Folder Structure

The project is backend-first. Only create modules when they become useful; this document defines the intended long-term organization.

```text
the-smoke/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── auth/
│   ├── __init__.py
│   ├── login.py
│   ├── register.py
│   ├── password_reset.py
│   └── session.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── setup.py
│   ├── migrations.py
│   ├── users.py
│   ├── players.py
│   ├── player_stats.py
│   ├── player_status.py
│   ├── districts.py
│   ├── crimes.py
│   ├── jobs.py
│   ├── inventory.py
│   ├── properties.py
│   ├── vehicles.py
│   ├── gangs.py
│   └── factions.py
│
├── game/
│   ├── __init__.py
│   │
│   ├── player/
│   │   ├── __init__.py
│   │   ├── player.py
│   │   ├── progression.py
│   │   ├── regeneration.py
│   │   └── status.py
│   │
│   ├── crime/
│   │   ├── __init__.py
│   │   ├── crimes.py
│   │   ├── progression.py
│   │   ├── wanted.py
│   │   └── consequences.py
│   │
│   ├── combat/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── damage.py
│   │   ├── equipment.py
│   │   └── results.py
│   │
│   ├── gym/
│   │   ├── __init__.py
│   │   ├── gym.py
│   │   └── training.py
│   │
│   ├── jobs/
│   │   ├── __init__.py
│   │   ├── careers.py
│   │   ├── shifts.py
│   │   └── progression.py
│   │
│   ├── world/
│   │   ├── __init__.py
│   │   ├── districts.py
│   │   ├── travel.py
│   │   └── reputation.py
│   │
│   ├── economy/
│   │   ├── __init__.py
│   │   ├── banking.py
│   │   ├── shops.py
│   │   └── transactions.py
│   │
│   ├── inventory/
│   │   ├── __init__.py
│   │   ├── inventory.py
│   │   ├── items.py
│   │   └── equipment.py
│   │
│   ├── housing/
│   │   ├── __init__.py
│   │   ├── properties.py
│   │   ├── housing.py
│   │   └── upgrades.py
│   │
│   ├── vehicles/
│   │   ├── __init__.py
│   │   ├── vehicles.py
│   │   ├── driving.py
│   │   └── maintenance.py
│   │
│   ├── gangs/
│   │   ├── __init__.py
│   │   ├── gangs.py
│   │   ├── members.py
│   │   ├── operations.py
│   │   └── influence.py
│   │
│   ├── factions/
│   │   ├── __init__.py
│   │   ├── factions.py
│   │   └── reputation.py
│   │
│   └── businesses/
│       ├── __init__.py
│       ├── businesses.py
│       ├── employees.py
│       ├── upgrades.py
│       └── finances.py
│
├── data/
│   └── game.db
│
├── utils/
│   ├── __init__.py
│   ├── security.py
│   ├── time_utils.py
│   ├── validators.py
│   └── constants.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_player.py
│   ├── test_crimes.py
│   ├── test_gym.py
│   └── test_database.py
│
└── docs/
    ├── game_design.md
    ├── folder_structure.md
    ├── database_schema.md
    ├── progression.md
    └── roadmap.md
```

## Responsibilities

### `auth/`
Authentication-facing workflows such as register, login and password reset.

### `database/`
Only persistence concerns: connections, schema setup, migrations and repository-style data access functions.

### `game/`
Actual game rules. These modules should avoid depending directly on terminal `input()` / `print()` where practical so the same logic can later serve a browser frontend.

### `utils/`
Cross-cutting helpers such as security, validation and time calculations.

### `tests/`
Automated tests for game rules and persistence.

### `docs/`
The source of truth for design decisions, schema and roadmap.

## Immediate Structure

Do not create every implementation file immediately. The near-term backend should focus on:

```text
auth/
database/
game/player/
game/gym/
game/crime/
game/world/
game/housing/
utils/
tests/
docs/
```

Other modules are planned extensions and should be introduced when their milestone begins.
