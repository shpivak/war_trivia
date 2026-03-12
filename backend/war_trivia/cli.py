"""
War Trivia - CLI.
Pick how bad you're experiencing it (no right/wrong). Light and funny.
"""

from .logic import TriviaGame, TriviaQuestion, summary_message
from .questions import ALL_QUESTIONS


def print_header() -> None:
    print()
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║   🏠 WAR TRIVIA: How Bad Is It, Really?         ║")
    print("  ║      (Barely feeling it → worst time ever.)      ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print()


def print_welcome() -> None:
    print("No wrong answers — just pick where you're at.")
    print("We'll see how you're doing on the scale of 'living my best life'")
    print("to 'send help and maybe chocolate.' 😄")
    print()


def print_no_questions() -> None:
    print("No questions in the deck yet — we're still writing them!")
    print("(Probably busy hiding in the mamad. We'll add them soon. 💪)")
    print()


def print_question(num: int, total: int, text: str, options: list[str]) -> None:
    print(f"  [{num}/{total}] {text}")
    print()
    for i, opt in enumerate(options, 1):
        print(f"    {i}. {opt}")
    print()


def print_choice_acknowledged() -> None:
    print("  Got it. We've all been there. (Wherever 'there' is.)")
    print()


def print_summary(total: int, average_level: float, num_options: int = 5) -> None:
    print()
    print("  ──────────── WHERE YOU'RE AT ────────────")
    if total == 0:
        print("  No questions = no verdict. You're off the hook.")
    else:
        print(f"  {summary_message(average_level)}")
    print("  ────────────────────────────────────────")
    print()
    print("Thanks for playing! Stay safe, stay silly.")
    print()


def run_interactive() -> None:
    """Run one round: pick your experience level for each question."""
    print_header()
    print_welcome()

    game = TriviaGame(ALL_QUESTIONS)

    if game.total_questions == 0:
        print_no_questions()
        print_summary(0, 0.0)
        return

    num_options = max((len(q.options) for q in game.questions), default=5)

    while not game.is_finished:
        while game.should_skip_current_question():
            game.skip_current_question()
            if game.is_finished:
                break
        if game.is_finished:
            break
        q = game.get_current_question()
        if not q:
            break
        n = game.state.current_question_index + 1
        t = game.total_questions
        print_question(n, t, q.text, q.options)
        while True:
            raw = input("  Your choice (number): ").strip()
            if not raw:
                print("  (Pick a number. We're not judging the number. Yet.)")
                continue
            try:
                choice = int(raw)
            except ValueError:
                print("  That's not a number. Try 1, 2, 3...")
                continue
            option_index = choice - 1
            if game.submit_answer(option_index):
                break
            print(f"  Pick between 1 and {len(q.options)}. You got this.")
        print_choice_acknowledged()

    summary = game.get_summary()
    print_summary(summary["answered_count"], summary["average_level"], num_options)


if __name__ == "__main__":
    run_interactive()
