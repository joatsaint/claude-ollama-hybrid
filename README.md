# AI Intern Setup: let a free local AI do the reading for Claude Code

Claude is the manager. A small AI on your own computer is the intern.

When a big stack of paper lands on the desk, you do not want the expensive manager reading every page. You want the intern to read the whole stack and hand the manager one page of notes. That is all this repo does:

- The intern is **Ollama**, a free program that runs small AI models on your own computer.
- The handoff is one small Python file, `ask_local.py`. You give it a file and a question. It reads the whole file with the local model and prints a short answer. Claude reads the short answer, not the whole file.
- One rule in your `CLAUDE.md` tells Claude Code when to use it.

Nothing you give the intern leaves your computer. There is no account, no API key and no bill for the reading.

## Fastest way: let Claude Code do the setup

1. Install Claude Code (you probably already have it).
2. Download or clone this repo, open a terminal in the folder, and start Claude Code there.
3. Say: **Read SETUP_WITH_CLAUDE.md and set this up for me.**

Claude walks you through it and asks before it installs, downloads or edits anything. If you do not have Claude Code, you can paste `SETUP_WITH_CLAUDE.md` into any Claude chat and it will walk you through the same steps one at a time.

## Doing it by hand (five steps)

1. **Install Ollama.** Download it from ollama.com for Windows, or in PowerShell: `winget install --id Ollama.Ollama -e`. Check it with `ollama --version`.
2. **Give the intern a brain.** `ollama pull llama3.2:3b` (about 2 GB). Small and fast; it makes more mistakes.
3. **Test it.** `ollama run llama3.2:3b`, ask something, leave with `/bye`.
4. **Set up the handoff.** You need Python 3. Run `python ask_local.py --check` to confirm it can see Ollama. Then try it:
   `python ask_local.py sample\notes.txt "What are the action items and who owns each one?"`
5. **Teach Claude when to use it.** Add the rule in `CLAUDE_RULE.md` to your `CLAUDE.md`.

## The honest limits (please read)

- **A small intern can miss things.** In one test a small model read a thirty-thousand-word transcript and said a topic was not in it. It was. A bigger model found it. See `TESTED.md`.
- **Check the answer.** Even on the short sample, the small model got most action items right and one owner wrong. Treat the answer as a good first pass and look at the original for anything that matters. AI assists, humans approve.
- **It is slower than Claude.** A local model on a modest computer takes seconds to minutes. You are trading time for tokens.
- **The CLAUDE.md rule is a request, not a lock.** Watch the first few jobs to make sure Claude follows it.
- **Privacy.** The documents stay on your computer. The short answer is what Claude sees.

## What is in here

| File | What it is |
|---|---|
| `ask_local.py` | The handoff script (Python 3, no extra installs) |
| `SETUP_WITH_CLAUDE.md` | Step-by-step instructions that Claude follows to set everything up with you |
| `CLAUDE_RULE.md` | The rule to add to your `CLAUDE.md` |
| `sample/notes.txt` | A short made-up document to test with |
| `TESTED.md` | What was measured, on what computer |

## Prior art

Other open-source tools do a similar job, usually as an MCP server (for example mcp-local-llm and localthink-mcp). This repo is the simplest version: one short script and one rule, with no server to run.

Built with Claude Code. MIT license.
