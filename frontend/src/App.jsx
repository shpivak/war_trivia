import { useEffect, useState } from "react";

const API = "http://localhost:8000";

export default function App() {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const [current, setCurrent] = useState(0);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API}/api/questions`)
      .then((r) => r.json())
      .then(setQuestions)
      .catch(() => setError("Could not reach the backend. Is it running?"));
  }, []);

  function isSkipped(index) {
    const q = questions[index];
    if (!q || q.show_only_if_previous_choice_was_not == null) return false;
    return answers[index - 1] === q.show_only_if_previous_choice_was_not;
  }

  function nextVisible(from) {
    let i = from;
    while (i < questions.length && isSkipped(i)) {
      i++;
    }
    return i;
  }

  function pick(optionIndex) {
    const newAnswers = [...answers];
    // fill any skipped questions between current and picked with -1
    for (let i = answers.length; i < current; i++) newAnswers[i] = -1;
    newAnswers[current] = optionIndex;
    setAnswers(newAnswers);

    const next = nextVisible(current + 1);
    if (next >= questions.length) {
      // fill remaining skipped
      const full = [...newAnswers];
      for (let i = full.length; i < questions.length; i++) full[i] = -1;
      submit(full);
    } else {
      setCurrent(next);
    }
  }

  function submit(finalAnswers) {
    fetch(`${API}/api/result`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers: finalAnswers }),
    })
      .then((r) => r.json())
      .then(setResult)
      .catch(() => setError("Failed to get result."));
  }

  function restart() {
    setAnswers([]);
    setCurrent(0);
    setResult(null);
  }

  if (error) return <Screen><p className="error">{error}</p></Screen>;
  if (!questions.length) return <Screen><p className="muted">Loading…</p></Screen>;

  if (result) {
    return (
      <Screen>
        <div className="result-box">
          <h2>Your result</h2>
          <p className="result-msg">{result.message}</p>
          <p className="muted">
            {result.answered_count} questions answered · avg level{" "}
            {result.average_level.toFixed(1)}
          </p>
          <button onClick={restart}>Start over</button>
        </div>
      </Screen>
    );
  }

  const q = questions[current];
  const progress = Math.round((current / questions.length) * 100);

  return (
    <Screen>
      <div className="progress-bar">
        <div className="progress-fill" style={{ width: `${progress}%` }} />
      </div>
      <p className="counter">{current + 1} / {questions.length}</p>
      <h2 className="question">{q.text}</h2>
      <div className="options">
        {q.options.map((opt, i) => (
          <button key={i} className="option" onClick={() => pick(i)}>
            {opt}
          </button>
        ))}
      </div>
    </Screen>
  );
}

function Screen({ children }) {
  return (
    <div className="screen">
      <header>
        <h1>War Trivia</h1>
        <p className="tagline">How bad is it, really?</p>
      </header>
      <main>{children}</main>
    </div>
  );
}
