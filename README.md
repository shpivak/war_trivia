# War Trivia — How bad is it, really?

Casual quiz about life in Israel during tough times. You pick where you're at on each question (barely feeling it → worst time ever). No right or wrong; we just rank how you're doing and give a light, funny summary at the end.

---

## Structure

```
war_trivia/
├── README.md          ← you are here
├── backend/           ← Python: logic, CLI, API
│   ├── war_trivia/    ← game package
│   │   ├── logic.py   ← TriviaGame, TriviaQuestion, summary_message
│   │   ├── questions.py ← all questions (edit here to add/change)
│   │   ├── cli.py     ← interactive terminal game
│   │   └── __init__.py
│   ├── api.py         ← FastAPI app
│   └── requirements.txt
└── frontend/          ← empty; add React (or other) UI when ready
    └── README.md
```

---

## Run the backend

From this repo (e.g. `development/` or wherever `war_trivia` lives):

```bash
cd war_trivia/backend
pip install -r requirements.txt
```

**CLI (interactive in terminal):**
```bash
python3 -m war_trivia.cli
```

**API server (for a future frontend):**
```bash
uvicorn api:app --reload
```
Runs at http://localhost:8000. Docs: http://localhost:8000/docs.

---

## API (for when you build the frontend)

- **GET `/api/questions`**  
  Returns a list of questions. Each has: `index`, `text`, `options`, and optionally `show_only_if_previous_choice_was_not` (skip this question if the *previous* answer was that option index).

- **POST `/api/result`**  
  Body: `{"answers": [0, 1, -1, 2, ...]}` — one value per question, in order. Use `-1` for skipped questions (e.g. “Where are you staying?” when they said “Yes” to “Do you live at home?”, or childcare when they have zero kids).  
  Response: `answered_count`, `average_level`, `message` (the summary line).

Skip logic is the same as the CLI: frontend should hide “Where are you staying?” when “Do you live at home?” = Yes, and hide “Childcare setup?” when “How many kids?” = Zero. Send `-1` for those so the backend has a full-length `answers` array.

---

## Where to edit

- **Questions and options:** `backend/war_trivia/questions.py`
- **Summary messages (the “where you’re at” line):** `backend/war_trivia/logic.py` → `summary_message()`
- **CLI copy:** `backend/war_trivia/cli.py`
- **API routes / CORS:** `backend/api.py`

---

## Continue later

- **Frontend:** Put a React (or other) app in `frontend/`. Call `GET /api/questions`, run through the quiz (apply skip logic), then `POST /api/result` with the `answers` array and show `message`.
- **Hebrew:** Questions are in English in code; you can add Hebrew text or i18n when you’re ready.
- **More questions / ranking:** Add to `questions.py`; keep options ordered from “least bad” (index 0) to “worst” (last) so `average_level` and `summary_message` still make sense.

Stay safe, stay silly.
