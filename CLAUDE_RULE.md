# The rule to add to your CLAUDE.md

Copy this block into your project's `CLAUDE.md` (or your global `~/.claude/CLAUDE.md`). Change the path to wherever you keep `ask_local.py`.

```
## Local intern for long documents
When I ask you to read, summarize or search a document longer than about 3,000 words, do not read the whole file yourself.
First run: python "<path to>\ask_local.py" "<file>" "<my question>"
Work from its short answer. Open the original file only for the exact part you need to check.
The local model can miss things: if the answer looks thin or the question is important, say so and run it again with a bigger model (--model gemma4:e4b or another one I have installed).
```

Why: the intern (a small model on your computer) reads the stack for free, and Claude only reads the short notes.
This is a request, not a lock. Watch the first few jobs to make sure Claude follows it.
