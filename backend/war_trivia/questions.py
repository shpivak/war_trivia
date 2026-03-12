"""
War Trivia - Questions (EN for display).
Source order: better → worse (index 0 = least bad, last = roughest).
"""

from logic import TriviaQuestion

SHELTER = TriviaQuestion(
    text="What's your shelter situation?",
    options=[
        "Mamad — in the apartment",
        "Mamak — on the floor (shared)",
        "Shelter — in the building",
        "Public shelter",
    ],
)

LIVE_AT_HOME = TriviaQuestion(
    text="Do you live at your home right now?",
    options=["Yes", "No"],
)

WHERE_STAYING = TriviaQuestion(
    text="Where are you staying?",
    options=[
        "At my parents'",
        "At friends'",
        "Sublet",
        "Zimmer (temporary)",
        "Hotel",
    ],
    show_only_if_previous_choice_was_not=0,
)

KIDS_COUNT = TriviaQuestion(
    text="How many kids do you have?",
    options=[
        "Zero (peace and quiet, or existential dread — your call)",
        "1",
        "2",
        "3 or more",
    ],
)

KIDS_ARRANGEMENT = TriviaQuestion(
    text="If you have kids, what's the childcare setup?",
    options=[
        "Framework (gan / school) running",
        "Babysitter",
        "Grandparents",
        "No one — we're winging it",
    ],
    show_only_if_previous_choice_was_not=0,
)

WHERE_IN_ISRAEL = TriviaQuestion(
    text="Where do you live in the country?",
    options=[
        "Center (Gush Dan / Tel Aviv area)",
        "HaSharon (they barely get alarms)",
        "Jerusalem area",
        "North",
        "South",
        "Otef Aza",
    ],
)

ALERTS_LAST_NIGHT = TriviaQuestion(
    text="How many rocket alerts did you get last night?",
    options=[
        "Zero (slept like a baby, or didn't sleep for other reasons)",
        "1–2",
        "3–5",
        "6+ (what is sleep)",
    ],
)

SOMEONE_IN_RESERVES = TriviaQuestion(
    text="Is someone at home doing miluim (reserves)?",
    options=["No", "Yes"],
)

WORK = TriviaQuestion(
    text="How's work going?",
    options=[
        "Working from home",
        "Commuting as usual",
        "HALAT / not working right now",
        "I don't work / between jobs",
    ],
)

BIG_EVENT = TriviaQuestion(
    text="Any big event that got cancelled or might get messed up by the war?",
    options=[
        "Nope, no big plans",
        "Had something cancelled",
        "Something coming up that might get disrupted",
        "Multiple things already ruined or at risk",
    ],
)

ALL_QUESTIONS: list[TriviaQuestion] = [
    SHELTER,
    LIVE_AT_HOME,
    WHERE_STAYING,
    KIDS_COUNT,
    KIDS_ARRANGEMENT,
    WHERE_IN_ISRAEL,
    ALERTS_LAST_NIGHT,
    SOMEONE_IN_RESERVES,
    WORK,
    BIG_EVENT,
]
