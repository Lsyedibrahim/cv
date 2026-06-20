# SmartPick — Beginner ML Prep & Contribution Guide

**Audience:** Developers new to ML / XGBoost who want to contribute to `htzd-vehicle-smartpick-1`, build CV-worthy experience, and prepare for interviews.

**Related docs:** [Onboarding guide](./smartpick-databricks-onboarding-guide.md) · [README](../README.md)

---

## How to use this guide

Follow the **2-week prep plan** (Section 5) day by day. Use **Section 2** to choose your first PR. Use **Section 3** for CV bullets and **Section 4** for interview prep.

---

## 1. What ML this repo actually does (30-second pitch)

Vehicle SmartPick trains an **XGBoost click classifier** on historical search behavior, then at serving time blends click probability with **revenue (RPD)** to re-rank cars on hertz.com.

| Step | Module | What happens |
|------|--------|--------------|
| Labeled data | `src/transformer/choice_set.py` | Spark SQL: impressions × clicks × bookings |
| Features | `src/transformer/preprocess.py`, `features/` | ~20 tabular features |
| **Training** | **`src/transformer/training.py`** | XGBoost + IPW position-bias correction |
| **Evaluation** | **`src/transformer/evaluation.py`** | Hit@K, RPD, Shannon entropy |
| **Serving** | **`src/models/smartpick_v24.py`** | Scores per vehicle for BFF |
| Orchestration | `src/sipp_recommendation.py` | End-to-end job |
| Deploy | `src/loader/` | MLflow register + serving endpoint |

This is **tabular supervised ML** (not deep learning).

---

## 2. Beginner contributions (by tier)

### Tier A — Start here (low risk, no prod ML changes)

#### Developer experience & docs

| Gap in repo | Your contribution |
|-------------|-------------------|
| README mentions `make unit-test` but Makefile lacks it | Add `unit-test` target |
| Python version TODO in README | Pin version matching Databricks 16.4 ML runtime |
| No local synthetic dataset | Small fixture + script to exercise `training.py` without UC |
| Onboarding | Keep `docs/smartpick-databricks-onboarding-guide.md` updated |

**Suggested first PR:** Add `make unit-test` to Makefile + README fix.

```makefile
.PHONY: unit-test
unit-test: ## run pytest from src/
	cd src && python -m pytest ../tests/ -v
```

#### Tests (best way to learn ML code)

Run locally:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
brew install libomp   # macOS — required for XGBoost
cd src && python -m pytest ../tests/ -v
```

| Module | Beginner-friendly test ideas |
|--------|------------------------------|
| `training.py` | IPW edge cases: all clicks at position 0, clipping at max, empty data |
| `evaluation.py` | Hit@K when session has no clicks; single-vehicle session |
| `validation.py` | Schema errors with clearer messages |
| `extract.py` | Invalid CLI args, malformed table names |
| `smartpick_v24.py` | Invalid BFF payloads (bad `rate_type`, missing fields) |

**Pattern:** See `tests/test_training.py` — small pandas DataFrames, assert numbers.

#### Lint & format

```bash
make install-dev
make format
make lint
```

Fixing flake8/mypy in one file is a valid first PR.

---

### Tier B — After 2–4 weeks on the codebase

| Area | Contribution |
|------|--------------|
| **Notebooks** | “Amplitude 101” notebook — sample rows from `amplitude_from_s3_events_raw` with comments |
| **Notebooks** | Update `notebooks/smoke_test.py` for V2.4 (still references old curated table) |
| **Logging** | Clearer stage summaries in `sipp_recommendation.py` / `training.py` (row counts, IPW summary) |
| **Validation** | New checks in `validation.py` + tests in `test_validation.py` |
| **Deploy docs** | Document volume bind + `UnauthorizedError` troubleshooting (see onboarding guide) |

**Notebooks need:** datalab read access; always filter by `export_date` and use `LIMIT`.

---

### Tier C — With team pairing only

| Area | Why you need a mentor |
|------|------------------------|
| New features in `features/` | Offline metric impact; train-serve parity |
| `blend_alpha` / XGBoost params | Business and A/B implications |
| `choice_set.py` SQL changes | Silent training data corruption risk |
| `loader/` Champion promotion | Affects live traffic |
| Removing V2.3 paths | Rollback safety |

---

### What to avoid as first contributions

- Changing `choice_set.py` SQL without DS review
- Changing prod `databricks.yml` scoring defaults
- Promote/Champion logic without approval
- Large refactors across `sipp_recommendation.py`

---

## 3. CV & resume framing

### Modules to headline

**Primary (ML training story):**

- `src/transformer/training.py` — XGBoost, IPW, sample weights
- `src/transformer/evaluation.py` — Hit@K, RPD, business metrics

**Secondary (production ML story):**

- `src/models/smartpick_v24.py` — inference contract, score blending
- `src/sipp_recommendation.py` — one line for end-to-end pipeline

**Support (platform):**

- Databricks bundle deploy, MLflow, Model Serving — one bullet max

### Sample CV summary (adjust to your actual work)

> Contributed to **Vehicle SmartPick**, a production XGBoost ranking pipeline on Databricks: labeled training data from Amplitude events, click classifier with IPW debiasing, offline evaluation (Hit@K / RPD), and MLflow Model Serving for real-time vehicle re-ranking.

### Sample bullets (only claim what you did)

- Trained/validated XGBoost click model with inverse propensity weighting for position-bias correction (`training.py`)
- Added pytest coverage for IPW clipping and sample-weight edge cases
- Implemented offline ranking metrics (Hit@K, RPD) validation tests (`evaluation.py`)
- Improved developer onboarding: bundle deploy docs, local test target, troubleshooting runbook
- Deployed `labs-v24` Databricks bundle; diagnosed UC permission failures on scheduled jobs

### Keywords for ATS / recruiters

XGBoost · supervised learning · feature engineering · learning to rank · recommendation systems · MLflow · model serving · production ML · bias correction · offline evaluation · Databricks · PySpark · Python · pytest

---

## 4. Interview prep

### Questions if you cite `training.py`

1. **Why XGBoost?** — Tabular data, fast CPU training, strong baseline, interpretable vs neural nets.
2. **What is the label?** — `was_clicked` (binary); ranking = score all vehicles, sort by blended score.
3. **What is IPW?** — Position bias: top slots get more clicks; IPW reweights so model learns preference not layout.
4. **Train/test split?** — Temporal holdout (last 3 days), not random rows — avoids leakage.
5. **Features?** — ~20 in `src/constants.py`: price, position, SIPP encodings, trip context, OAG stats.
6. **Overfitting?** — Early stopping, holdout eval, subsample/colsample, train-only encodings.
7. **Metrics beyond AUC?** — Hit@K, RPD, Shannon entropy (diversity).

### Questions if you cite `evaluation.py`

8. **Hit@K?** — Was the clicked vehicle in the model’s top K for that session?
9. **Why blend clicks + revenue?** — Clicks alone ignore revenue; `blend_alpha × P(click) + (1-α) × RPD_norm`.
10. **Offline vs online?** — Offline = historical replay; online = real users, latency, fallback, A/B.

### Questions if you cite `smartpick_v24.py`

11. **Train-serve parity?** — Same feature logic, price type (PAYNOW), encodings baked in artifact.
12. **Timeout/failure?** — BFF returns original order (graceful degradation).
13. **Why MLflow pyfunc?** — Versioned deploy, standard `predict()` for Databricks Serving.

### Questions if you cite the full pipeline

14. **Walk through one training run.** — Events → choice set → features → XGBoost → eval → MLflow → endpoint.
15. **Where does data come from?** — Amplitude → S3 → UC Delta; this repo **consumes**, does not ingest.
16. **Real ops issue?** — Scheduled job `UnauthorizedError` → UC grants / `run_as` / bundle redeploy.

### Whiteboard exercise (practice daily in week 2)

Draw:

```text
Amplitude events → choice set (label: was_clicked)
       → 20 features → XGBoost → P(click)
       → blend with RPD → score → BFF sorts vehicles
```

---

## 5. Two-week prep plan

### Week 1 — Learn core ML + read training code

| Day | Focus | Tasks | Done |
|-----|-------|-------|------|
| **Mon** | ML basics | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) — supervised learning, loss, overfitting (2–3 hrs) | [ ] |
| **Tue** | XGBoost | StatQuest: Gradient Boost + ROC/AUC videos; read `src/constants.py` | [ ] |
| **Wed** | Training code | Read `src/transformer/training.py` line by line; trace `compute_ipw_weights` → `train_click_model` | [ ] |
| **Thu** | Local setup | `venv`, `pip install -r requirements-dev.txt`, `brew install libomp`, run `pytest ../tests/test_training.py -v` | [ ] |
| **Fri** | Features & labels | Read `choice_set.py` module docstring (first 35 lines only); skim `constants.py` FEATURE_COLUMNS | [ ] |
| **Sat** | First contribution | Add `make unit-test` to Makefile OR add 2 tests to `test_training.py` | [ ] |
| **Sun** | Review | Write 5-sentence summary: label, algorithm, bias fix, metrics, deploy path (from memory) | [ ] |

**Week 1 exit criteria:** You can explain IPW and `was_clicked` without opening the code.

---

### Week 2 — Evaluation, serving, contribute, interview prep

| Day | Focus | Tasks | Done |
|-----|-------|-------|------|
| **Mon** | Evaluation | Read `src/transformer/evaluation.py`; run `pytest ../tests/test_evaluation.py -v` | [ ] |
| **Tue** | Serving | Read `src/models/smartpick_v24.py` intro + `_score_vanilla`; run `pytest ../tests/test_smartpick_v24.py -v` | [ ] |
| **Wed** | Pipeline | Read `src/sipp_recommendation.py` — only the `run()` stage comments (steps 1–10) | [ ] |
| **Thu** | Databricks | Skim onboarding guide §7–8; if access: Catalog → preview `amplitude_from_s3_events_raw` with LIMIT | [ ] |
| **Thu** | Position bias | Skim [IPW explainer](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html) (30 min) | [ ] |
| **Fri** | Second contribution | PR: validation tests, logging improvement, or onboarding troubleshooting section | [ ] |
| **Sat** | Mock interview | Answer §4 questions out loud; whiteboard the pipeline | [ ] |
| **Sun** | CV draft | Write 3 bullets from §3; list 2 modules you can defend in depth | [ ] |

**Week 2 exit criteria:** 1–2 small PRs (or drafts); 10-minute verbal walkthrough of train → eval → serve.

---

## 6. Learning materials (reference)

Full links and tiers are in [smartpick-databricks-onboarding-guide.md](./smartpick-databricks-onboarding-guide.md) §14–19. Essentials:

| Tier | Top resources |
|------|----------------|
| **1 — Core ML** | Google ML Crash Course · StatQuest (XGBoost, AUC) · [XGBoost Python intro](https://xgboost.readthedocs.io/en/stable/python/python_intro.html) · pandas 10min guide |
| **2 — SmartPick** | IPW / position bias · MLflow docs · in-repo: `training.py`, `evaluation.py`, `smartpick_v24.py` |
| **3 — Platform** | Databricks UC, Jobs, Bundles, Model Serving — onboarding guide §6–8 |

### In-repo reading order

```text
src/constants.py
  → src/transformer/training.py
  → src/transformer/evaluation.py
  → src/models/smartpick_v24.py
  → src/sipp_recommendation.py
```

---

## 7. Contribution → CV mapping

| What you contribute | Interview / CV phrase |
|---------------------|------------------------|
| Tests for `training.py` | “Validated IPW position-bias correction with unit tests” |
| `make unit-test` + README | “Improved ML pipeline developer onboarding” |
| Validation improvements | “Added data-quality guards at pipeline stage boundaries” |
| Labs deploy debugging | “Deployed Databricks bundle; diagnosed UC permission failures” |
| Amplitude exploration notebook | “Documented Amplitude event schema for SmartPick training data” |

---

## 8. Quick reference — key files

| File | Lines (approx) | Beginner can… |
|------|----------------|---------------|
| `training.py` | ~183 | Read fully, add tests |
| `evaluation.py` | ~500 | Read Hit@K function, add tests |
| `constants.py` | ~60 | Read fully |
| `choice_set.py` | ~550 | Read docstring + ask questions; don’t edit SQL solo |
| `smartpick_v24.py` | ~900 | Read scoring path; add input validation tests |
| `sipp_recommendation.py` | ~348 | Read orchestration comments |

---

## 9. Checklist — end of 2 weeks

- [ ] Ran `pytest` locally on `test_training.py` and `test_evaluation.py`
- [ ] Can explain: label, IPW, Hit@K, blend_alpha in plain English
- [ ] Read `training.py`, `evaluation.py`, `constants.py` completely
- [ ] Skimmed `smartpick_v24.py` scoring path
- [ ] Opened or drafted 1–2 PRs (tests, Makefile, or docs)
- [ ] Drafted 3 CV bullets (honest to your actual work)
- [ ] Practiced 5-minute “walk through the training pipeline” talk

---

*Last updated: June 2026 · For questions on prod deploy, pair with the SmartPick / HDP team before merging scoring or data pipeline changes.*
