import random
from dataclasses import dataclass

from game.progression import award_xp


@dataclass(frozen=True)
class CrimeDefinition:
    key: str
    name: str
    district: str
    nerve_cost: int
    success_chance: int
    min_reward: int
    max_reward: int
    xp_reward: int
    crime_xp_reward: int
    reputation_reward: int
    min_damage: int = 5
    max_damage: int = 15


@dataclass(frozen=True)
class CrimeResult:
    attempted: bool
    crime_key: str
    crime_name: str
    district: str
    success: bool
    reason: str | None = None
    nerve_spent: int = 0
    cash_reward: int = 0
    xp_reward: int = 0
    crime_xp_reward: int = 0
    reputation_reward: int = 0
    damage: int = 0
    levels_gained: int = 0


CRIMES = (
    CrimeDefinition(
        key="camden_shoplift",
        name="Shoplift on Camden High Street",
        district="Camden",
        nerve_cost=2,
        success_chance=80,
        min_reward=20,
        max_reward=60,
        xp_reward=10,
        crime_xp_reward=10,
        reputation_reward=2,
    ),
    CrimeDefinition(
        key="camden_market_stall",
        name="Rob a Camden market stall",
        district="Camden",
        nerve_cost=4,
        success_chance=65,
        min_reward=60,
        max_reward=140,
        xp_reward=25,
        crime_xp_reward=18,
        reputation_reward=4,
    ),
    CrimeDefinition(
        key="brixton_phone_snatch",
        name="Snatch a phone in Brixton",
        district="Brixton",
        nerve_cost=3,
        success_chance=72,
        min_reward=40,
        max_reward=100,
        xp_reward=15,
        crime_xp_reward=12,
        reputation_reward=3,
    ),
    CrimeDefinition(
        key="brixton_warehouse",
        name="Break into a Brixton warehouse",
        district="Brixton",
        nerve_cost=7,
        success_chance=42,
        min_reward=180,
        max_reward=480,
        xp_reward=55,
        crime_xp_reward=30,
        reputation_reward=7,
    ),
    CrimeDefinition(
        key="soho_pickpocket",
        name="Pickpocket in Soho",
        district="Soho",
        nerve_cost=4,
        success_chance=65,
        min_reward=50,
        max_reward=150,
        xp_reward=25,
        crime_xp_reward=18,
        reputation_reward=4,
    ),
    CrimeDefinition(
        key="soho_nightclub",
        name="Raid a Soho nightclub office",
        district="Soho",
        nerve_cost=8,
        success_chance=38,
        min_reward=250,
        max_reward=650,
        xp_reward=65,
        crime_xp_reward=35,
        reputation_reward=8,
    ),
)

CRIMES_BY_KEY = {crime.key: crime for crime in CRIMES}


def get_crime(crime_key):
    return CRIMES_BY_KEY[crime_key]


def commit_crime(player, crime, rng=None):
    if rng is None:
        rng = random

    if player.nerve < crime.nerve_cost:
        return CrimeResult(
            attempted=False,
            crime_key=crime.key,
            crime_name=crime.name,
            district=crime.district,
            success=False,
            reason="not_enough_nerve",
        )

    player.nerve -= crime.nerve_cost
    progress = _crime_progress_for(player, crime.key)
    progress["attempts"] += 1

    if rng.randint(1, 100) <= crime.success_chance:
        reward = rng.randint(crime.min_reward, crime.max_reward)
        player.money += reward
        levels_gained = award_xp(player, crime.xp_reward)

        progress["xp"] += crime.crime_xp_reward
        progress["successes"] += 1

        reputation = _district_reputation_for(player)
        reputation[crime.district] = (
            reputation.get(crime.district, 0)
            + crime.reputation_reward
        )

        return CrimeResult(
            attempted=True,
            crime_key=crime.key,
            crime_name=crime.name,
            district=crime.district,
            success=True,
            nerve_spent=crime.nerve_cost,
            cash_reward=reward,
            xp_reward=crime.xp_reward,
            crime_xp_reward=crime.crime_xp_reward,
            reputation_reward=crime.reputation_reward,
            levels_gained=levels_gained,
        )

    damage = rng.randint(crime.min_damage, crime.max_damage)
    player.health = max(0, player.health - damage)

    return CrimeResult(
        attempted=True,
        crime_key=crime.key,
        crime_name=crime.name,
        district=crime.district,
        success=False,
        nerve_spent=crime.nerve_cost,
        damage=damage,
    )


def crimes_menu(player):
    while True:
        print("\n===== CRIMES =====")
        print("Nerve:", player.nerve)

        for number, crime in enumerate(CRIMES, start=1):
            print(
                f"{number}. [{crime.district}] {crime.name} "
                f"({crime.nerve_cost} nerve)"
            )

        back_option = len(CRIMES) + 1
        print(f"{back_option}. Back")

        choice = input("Choose: ").strip()

        if choice == str(back_option):
            break

        try:
            selected_index = int(choice) - 1
        except ValueError:
            print("Invalid option.")
            continue

        if not 0 <= selected_index < len(CRIMES):
            print("Invalid option.")
            continue

        crime = CRIMES[selected_index]

        result = commit_crime(player, crime)
        display_crime_result(player, result)


def display_crime_result(player, result):
    if result.reason == "not_enough_nerve":
        print("\nNot enough nerve.")
        return

    print("\nAttempting:", result.crime_name)

    if result.success:
        print("Crime successful!")
        print("You made £", result.cash_reward)
        print("XP +", result.xp_reward)
        print("Crime XP +", result.crime_xp_reward)
        print(
            f"{result.district} reputation +",
            result.reputation_reward,
        )

        if result.levels_gained > 0:
            print(f"Level up! You are now level {player.level}.")
    else:
        print("Crime failed!")
        print("You lost", result.damage, "health")


def _crime_progress_for(player, crime_key):
    if not hasattr(player, "crime_progress"):
        player.crime_progress = {}

    return player.crime_progress.setdefault(
        crime_key,
        {"xp": 0, "attempts": 0, "successes": 0},
    )


def _district_reputation_for(player):
    if not hasattr(player, "district_reputation"):
        player.district_reputation = {}

    return player.district_reputation
