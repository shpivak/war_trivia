"""
War Trivia - Game logic.
Theme: how bad you're experiencing it — from barely feeling it to worst time ever.
No right or wrong; we just rank where you're at.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TriviaQuestion:
    """
    One scenario — you pick how much you're feeling it.
    Options should be ordered from "barely / enjoying" (0) to "worst ever" (last).
    If show_only_if_previous_choice_was_not is set, this question is skipped when
    the previous question's answer was that index (e.g. 0 = skip when they picked option 0).
    """
    text: str
    options: list[str] = field(default_factory=list)
    show_only_if_previous_choice_was_not: Optional[int] = None


@dataclass
class GameState:
    """Tracks your choices: which option index you picked per question."""
    answers: list[int] = field(default_factory=list)
    current_question_index: int = 0


class TriviaGame:
    """One round: go through questions, pick your experience level for each."""

    def __init__(self, questions: Optional[list[TriviaQuestion]] = None):
        self.questions = questions or []
        self.state = GameState()

    @property
    def total_questions(self) -> int:
        return len(self.questions)

    @property
    def is_finished(self) -> bool:
        return self.state.current_question_index >= self.total_questions

    def get_current_question(self) -> Optional[TriviaQuestion]:
        if self.is_finished:
            return None
        idx = self.state.current_question_index
        if 0 <= idx < self.total_questions:
            return self.questions[idx]
        return None

    def should_skip_current_question(self) -> bool:
        """True if this question should be skipped based on previous answer (e.g. "if no kids, skip childcare")."""
        idx = self.state.current_question_index
        if idx <= 0:
            return False
        q = self.questions[idx]
        if q.show_only_if_previous_choice_was_not is None:
            return False
        prev_answer = self.state.answers[idx - 1]
        return prev_answer == q.show_only_if_previous_choice_was_not

    def skip_current_question(self) -> None:
        """Skip the current question (record -1) and advance."""
        self.state.answers.append(-1)
        self.state.current_question_index += 1

    def submit_answer(self, option_index: int) -> bool:
        """
        Record the option you chose (0-based). Returns True if index was valid.
        """
        q = self.get_current_question()
        if not q or option_index < 0 or option_index >= len(q.options):
            return False
        self.state.answers.append(option_index)
        self.state.current_question_index += 1
        return True

    def get_summary(self) -> dict:
        """
        Summary for end-of-round. Options are ordered: 0 = chill, last = worst.
        average_level: 0 = barely feeling it, higher = rougher.
        Only answered questions count (skipped ones are -1).
        """
        answers = self.state.answers
        answered = [a for a in answers if a >= 0]
        total_answered = len(answered)
        if total_answered == 0:
            average_level = 0.0
        else:
            average_level = sum(answered) / total_answered
        return {
            "total": self.total_questions,
            "answered_count": total_answered,
            "answers": list(answers),
            "average_level": average_level,
        }


def summary_message(average_level: float) -> str:
    """Same message logic as CLI for API result."""
    if average_level < 0.5:
        return "Barely feeling it — or actually enjoying the chaos. We see you."
    if average_level < 1.5:
        return "Mostly chill with occasional 'wait, what?' moments. Solid."
    if average_level < 2.5:
        return "Hanging in there. It's a vibe. Not a great vibe, but a vibe."
    if average_level < 3.5:
        return "Yeah, it's rough. You're allowed to say it. We're with you."
    return "Having a proper rough time. Sending virtual hugs and bad jokes. 💪"
