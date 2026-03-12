# Contributing

Thanks for wanting to help. Here's how.

---

## Getting started

1. Fork the repo and clone your fork.
2. Create a branch: `git checkout -b my-change`
3. Make your changes (see below for what's where).
4. Run the tests.
5. Open a PR against `main` with a short description of what and why.

---

## Running tests

### Backend

```bash
cd backend
pip install -r requirements.txt
python3 -m pytest
```

Tests live in `backend/tests/`. They cover the core game logic (skip rules, scoring, summary messages) and the API routes.

### Frontend

```bash
cd frontend
npm install
npm test
```

---

## What to contribute

- **New questions** — add to `backend/war_trivia/questions.py`. Keep options ordered from "least bad" (index 0) to "worst" (last) so the scoring stays consistent.
- **Summary messages** — tweak the thresholds or copy in `backend/war_trivia/logic.py` → `summary_message()`.
- **UI improvements** — `frontend/src/App.jsx` and `frontend/src/index.css`. Keep it simple and accessible.
- **Bug fixes** — please include a test that would have caught the bug.

---

## PR checklist

- [ ] Tests pass (`pytest` + `npm test`)
- [ ] New behaviour is covered by a test
- [ ] No unrelated changes snuck in

---

## Code style

- Python: no strict formatter required, just keep it readable. Type hints appreciated.
- JS/React: functional components, no class components. Keep logic in `App.jsx` unless it genuinely needs its own file.

---

That's it. PRs welcome, questions welcome, bad jokes about the war situation very welcome.
