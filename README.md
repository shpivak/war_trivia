# War Trivia — How bad is it, really?

Casual quiz about life in Israel during tough times. You pick where you're at on each question (barely feeling it → worst time ever). No right or wrong; we just rank how you're doing and give a light, funny summary at the end.

---

## Structure

```
war_trivia/
├── README.md
├── backend/           ← Python: logic, CLI, API
│   ├── war_trivia/    ← game package
│   │   ├── logic.py   ← TriviaGame, TriviaQuestion, summary_message
│   │   ├── questions.py ← all questions (edit here to add/change)
│   │   ├── cli.py     ← interactive terminal game
│   │   └── __init__.py
│   ├── api.py         ← FastAPI app
│   └── requirements.txt
└── frontend/          ← React (Vite) UI
    └── src/
        ├── App.jsx    ← quiz flow + skip logic
        └── index.css
```

---

## Option A — CLI (no frontend needed)

```bash
cd backend
pip install -r requirements.txt
python3 -m war_trivia.cli
```

Runs interactively in your terminal.

---

## Option B — API + UI

### 1. Start the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn api:app --reload
```

Runs at http://localhost:8000. Docs: http://localhost:8000/docs.

### 2. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Runs at http://localhost:5173. Open that in your browser.

---

## API reference

- **GET `/api/questions`**
  Returns all questions: `index`, `text`, `options`, and optionally `show_only_if_previous_choice_was_not` (skip this question if the previous answer was that option index).

- **POST `/api/result`**
  Body: `{"answers": [0, 1, -1, 2, ...]}` — one value per question, in order. Use `-1` for skipped questions.
  Response: `answered_count`, `average_level`, `message` (summary line).

---

## Where to edit

- **Questions and options:** `backend/war_trivia/questions.py`
- **Summary messages:** `backend/war_trivia/logic.py` → `summary_message()`
- **CLI copy:** `backend/war_trivia/cli.py`
- **API routes / CORS:** `backend/api.py`
- **UI:** `frontend/src/App.jsx`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

Stay safe, stay silly.
