Awesome—here’s a complete scaffold and an “AI‑coder instruction pack” to kickstart your term paper on **Financial modeling & prediction using econometrics + machine learning**.

---

## 🎁 Download the ready‑to‑use project

* **Project zip:** [Download the scaffold](sandbox:/mnt/data/fin-ml-term-paper.zip)

It contains:

* End‑to‑end pipeline (`data → features → models → evaluation → optional backtest`)
* Baselines: **Naïve** & **ARIMA**
* ML models: **Random Forest** & **XGBoost**
* **Expanding‑window cross‑validation** + **Diebold–Mariano** tests
* A clean **paper outline** and an **AI‑coder prompt pack**
* Reproducible configuration via `config.yaml`

> After unzipping, run:
>
> ```bash
> pip install -r requirements.txt
> python -m src.pipeline.train --config config.yaml
> ```
>
> Results land in `artifacts/` (metrics, predictions, DM tests, and optional backtest).

---

## 🧭 Recommended study path (fast & focused)

1. **Choose a topic** (keep it simple):

   * *Predict 1‑day‑ahead S\&P 500 return* (`^GSPC`)
   * *Forecast daily volatility* (compare GARCH vs ML)
   * *Predict 1‑day change in 10Y UST yield* (`^TNX`) with macro + technicals

2. **Define the target** clearly

   * *Return target:* use log or percent return; set `target.transform: "return"`.
   * *Horizon:* 1 trading day (`target.horizon_days: 1`).

3. **Pick baseline and ML models**

   * Econometrics: **Naïve**, **ARIMA**
   * ML: **RandomForestRegressor**, **XGBRegressor**

4. **Design evaluation**

   * Metrics: **RMSE**, **MAE**, **MAPE**, **Directional Accuracy**
   * Statistical test: **Diebold–Mariano** for pairwise model comparisons
   * CV: **Expanding window** (provided)

5. **Report economic value** (optional)

   * Simple long/flat backtest on predicted returns
   * Apply realistic transaction costs in basis points

---

## 🧩 What’s inside the scaffold

```
fin-ml-term-paper/
├── config.yaml                # edit here: ticker, dates, models, CV, backtest
├── requirements.txt
├── Makefile
├── README.md
├── reports/
│   └── paper_outline.md       # drop-in structure for your write-up
├── prompts/
│   └── ai_coder_prompts.md    # guardrails + tasks for your AI coding assistant
├── src/
│   ├── data/download.py       # yfinance + FRED download
│   ├── features/technical.py  # returns, SMA, RSI, MACD, vol, lags
│   ├── evaluation/            # metrics, expanding-window CV, DM test
│   ├── models/                # Naive, ARIMA, RF, XGB
│   └── pipeline/train.py      # orchestrates the whole workflow
├── tests/                     # quick unit tests for CV & DM
└── artifacts/                 # output folder (created at runtime)
```

### Key defaults in `config.yaml`

* `data.target_ticker: "^GSPC"`
* Technical features: SMA(20/50), RSI(14), MACD(12/26/9), rolling volatility(21), z-score(21), lagged returns
* Models: `["Naive","ARIMA","RF","XGB"]`
* CV: 5 folds, expanding window, 90‑day test steps
* Backtest: long/flat with threshold; costs in bps

> You can change the ticker (e.g., `SPY`, `^TNX`) and dates without touching the code.

---

## 🛠️ AI‑Coder Instruction Pack (drop‑in)

Use this when prompting your coding assistant (also saved at `prompts/ai_coder_prompts.md`):

**Role & constraints**

* You are a careful senior ML engineer building a **time‑series forecasting** pipeline for a term paper.
* Avoid **look‑ahead leakage**; all features must use *past* info only (use `shift` where needed).
* Use **expanding‑window** CV; report **RMSE**, **MAE**, **MAPE**, **Directional Accuracy**.
* Provide **Diebold–Mariano** tests for model comparisons.
* Save tidy CSVs in `artifacts/`. Keep code readable and minimal.

**Definition of Done**

* `python -m src.pipeline.train --config config.yaml` runs end‑to‑end:

  * Downloads data → builds features → trains & evaluates → writes artifacts
  * Creates `metrics_summary.csv`, `predictions_{model}.csv`, `dm_test.csv`, optional `backtest_{model}.csv`
* Unit tests in `tests/` pass quickly.

**Tasks**

1. *Data ingestion:* `yfinance` for prices; `fredapi` (fallback to `pandas_datareader`) for macro. Save raw CSVs.
2. *Features:* returns, SMA, RSI, MACD, rolling volatility, z-score, lagged returns. No leakage.
3. *Econometrics:* `Naive`, `ARIMA` (params from config).
4. *ML:* `RandomForestRegressor`, `XGBRegressor` (with `StandardScaler` pipeline where needed).
5. *Evaluation:* expanding‑window CV, metrics, **DM test** (Newey–West variance).
6. *Backtest (optional):* simple long/flat on predicted *returns*, apply costs.
7. *Orchestration:* glue everything in `src/pipeline/train.py`.

**Guardrails**

* No seaborn; if plotting, use **matplotlib** only.
* Be explicit about NA handling and data alignment.
* Keep runtime modest; prefer clarity over micro‑optimizations.

**Extensions (if time permits)**

* Add Lasso/ElasticNet for feature selection.
* Try Model Confidence Set (MCS) for multiple comparisons.
* Add a regime‑split analysis (pre/post a chosen date).

---

## 📝 Paper outline you can fill in

A structured draft is ready at `reports/paper_outline.md`. It guides you through:

* Intro & motivation
* Data description (target, features, sources)
* Methods (ARIMA vs ML), CV design, metrics
* Results (tables + DM significance)
* Discussion (statistical vs economic significance)
* Limitations & ethics
* Conclusion & future work

---

## 🔍 Tips for a strong term paper (economics‑friendly)

* **Explain intuition**: why might technical indicators or macro variables help?
* **Show your splits**: a small diagram/table of expanding‑window folds helps examiners trust the process.
* **Report both**: statistical gains (RMSE) *and* economic value (simple backtest net of costs).
* **Be honest about limits**: non‑stationarity, snooping, fragile hyperparameters, and costs.

---

If you want, tell me your **exact topic choice** (e.g., ticker + horizon) and I’ll pre‑configure `config.yaml` and suggest a short list of **hypotheses** and **robustness checks** tailored to it.
