# Targeted understanding checks (adapt, do not dump the whole bank)

Ask one question after delivering a complete solution. Prefer multiple-choice or a single prediction when the learner is new; use a counterexample or transfer exercise in deep mode. Do not reveal answer before the learner responds unless requested.

## Regression / R

**Prompt:** In the *same* linear regression with the *same sample*, what usually changes when replacing conventional OLS standard errors with heteroskedasticity-robust standard errors: coefficient estimates, standard errors, or both?

**Expected:** Coefficient estimates stay the same; the variance/SE estimates may change. Explanations about sample differences or altered specification are separate cases.

**Prompt:** What does `y ~ z * x_centered` expand into in an R formula?

**Expected:** `z + x_centered + z:x_centered`; it permits slopes to differ by treatment status. With centered baseline covariates, `z` contrasts treatment vs control at `x_centered=0`.

## Causal inference

**Prompt:** If a covariate is measured after treatment and affected by treatment, can adding it to a treatment-effect regression create a problem? Why?

**Expected:** Yes: post-treatment adjustment can block mediated effects and/or introduce bias; whether it is justified depends on the estimand and causal graph.

## Inventory optimization

**Prompt:** With all else fixed, if the cost of understocking rises relative to overstocking, should the optimal newsvendor order quantity generally rise, fall, or stay constant?

**Expected:** The critical fractile rises and so does a nondecreasing optimal order quantile, potentially staying constant temporarily for discrete demand.

## Python literacy

**Prompt:** In `expected_profit = sum(prob[d] * profit(q, d) for d in demands)`, what is the difference between `profit(q,d)` and the surrounding `sum(...)`?

**Expected:** The function computes payoff for one demand outcome; multiplication by probability weights it; `sum` aggregates an expected value across possible outcomes.

## Feedback rule

On an incorrect answer, give a two-step repair: (1) point out the exact misconception, (2) show a very small numeric example and re-ask a narrower question. On a correct answer, give a brief reason and offer a slightly harder parameter-change question. Never mark a topic as permanently mastered from a single answer.
