---
type: llm
weight: 1
---

PASS if the response contains a Python function that removes duplicates and keeps first-seen order, such as one using dict.fromkeys or a seen set, and shows an example call.
FAIL if the function loses the original order, for example by returning list(set(items)), or if no example call is shown.
