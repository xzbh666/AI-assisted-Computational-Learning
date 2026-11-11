# Code to Understanding · AI 辅助计算式学习

**AI writes routine code; humans learn to interpret, verify, and adapt it.**

This repository contains a portable Agent Skill and the source for a ChatGPT private plugin.

## Features

- Solve coursework questions **before** teaching from the actual solution.
- Distinguish **subject knowledge** (statistical/causal/optimization concepts) from **code literacy** (Python/R syntax and APIs).
- Offer three modes: **quick**, **learn** (default), **deep**.
- Support starting from a question, screenshot, PDF, dataset, code snippet, or intermediate attempt.
- Run and verify when the host provides an execution tool; otherwise explicitly label code **not executed**.
- Ask one focused comprehension question rather than force the learner to rewrite whole programs.

## Getting started

Open the private ChatGPT plugin: https://chatgpt.com/plugins/plugins_6af429e1f6888191b6b9dffb78cb991c

Suggested prompt:

> 用“解题并学习”模式完成这道题。先给结论与可复现的 Python/R 代码，再解释学科原理和必须看懂的关键语法，最后问我一个检验理解的问题。

For an Agent Skills compatible host, use `skills/code-to-understanding/SKILL.md`.

## Project files

- `plugin.json` – plugin manifest.
- `skills/code-to-understanding/SKILL.md` – primary learning workflow.
- `skills/code-to-understanding/references/` – teaching rules and assessment bank.
- `skills/code-to-understanding/scripts/newsvendor_demo.py` – executable synthetic newsvendor example.
- `tests/test_skill.py` – smoke tests.

## Run the example

```bash
python -m unittest discover -s tests -v
python skills/code-to-understanding/scripts/newsvendor_demo.py
```

The synthetic example uses demand values (10, 20, 30) with probabilities (0.2, 0.5, 0.3), sales price 10, purchase cost 4, and salvage 1. Critical fractile = 2/3. Expected profits for Q=10,20,30 are 60,102,99 respectively; the optimizer chooses Q=20.

## Limits

v0.1.0 is **skills-only**; it is not a new compute server and cannot run code when the host lacks an execution tool. It has no permanent learner-profile database or automatic GitHub synchronization. Saving a plugin release and committing GitHub are separate operations; this repo contains the source for release v0.1.0.

Never commit private course data, API tokens, or student records to this public repository.
