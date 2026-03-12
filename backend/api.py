"""
War Trivia - API layer (parallel to CLI).
"""

from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from war_trivia.questions import ALL_QUESTIONS
from war_trivia.logic import summary_message

app = FastAPI(
    title="War Trivia API",
    description="How bad is it, really? (Barely feeling it → worst time ever.)",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionOut(BaseModel):
    index: int
    text: str
    options: List[str]
    show_only_if_previous_choice_was_not: Optional[int]


class ResultIn(BaseModel):
    answers: List[int]


class ResultOut(BaseModel):
    answered_count: int
    average_level: float
    message: str


@app.get("/api/questions", response_model=List[QuestionOut])
def get_questions() -> list[QuestionOut]:
    """Return all questions with index and optional skip rule for the frontend."""
    return [
        QuestionOut(
            index=i,
            text=q.text,
            options=q.options,
            show_only_if_previous_choice_was_not=q.show_only_if_previous_choice_was_not,
        )
        for i, q in enumerate(ALL_QUESTIONS)
    ]


@app.post("/api/result", response_model=ResultOut)
def post_result(body: ResultIn) -> ResultOut:
    """Compute summary from answers. -1 = skipped question."""
    expected = len(ALL_QUESTIONS)
    if len(body.answers) != expected:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {expected} answers, got {len(body.answers)}",
        )
    answered = [a for a in body.answers if a >= 0]
    for i, a in enumerate(body.answers):
        if a < 0:
            continue
        q = ALL_QUESTIONS[i]
        if a >= len(q.options):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid option index {a} for question {i} (max {len(q.options) - 1})",
            )
    answered_count = len(answered)
    average_level = sum(answered) / answered_count if answered_count else 0.0
    return ResultOut(
        answered_count=answered_count,
        average_level=round(average_level, 2),
        message=summary_message(average_level),
    )
