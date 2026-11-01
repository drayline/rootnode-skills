---
max_turns: 15
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Claude keeps ignoring the rules in my Project and I can't work out why. Sometimes it follows them and sometimes it acts like they aren't there. What's going on?

Custom Instructions (this is the whole thing, about 4,000 words, abridged here):
You are a legal research assistant. [1,200 words of research process.] [900 words on citation style.] [800 words on the tone to use with clients.] [700 words of contract review checklists.] Also please remember the client call last Tuesday where we agreed to stop citing state cases, as we discussed. Never give legal advice. Always give a clear recommendation on what the client should do.

Knowledge files:
- citation-style.md (repeats the 900 words on citation style)
- process.md (repeats the 1,200 words of research process)
- notes-from-2022.txt (nothing in the instructions mentions this file)
