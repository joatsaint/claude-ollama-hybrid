# Instructions for Claude: set up the AI intern with the user

You are helping a beginner set up a local "intern": Ollama plus `ask_local.py`, so you (Claude) can hand long documents to a free local model and read only its short answer. Go slowly, use plain words, and do one step at a time.

## Ground rules (follow all of them)
- **Ask before you install, download or change anything.** Before every command that installs, downloads, or edits a file, say what it does in one plain sentence, show the exact command, and wait for a clear yes.
- Never run anything as administrator unless the user says yes and you explain why.
- Never delete files. Never edit a file the user did not agree to. When you add text to `CLAUDE.md`, append only; do not rewrite or reorder the file.
- Do not send the user's documents anywhere. Everything here runs on their own computer.
- If a step fails, stop, say what happened in plain words, and offer one fix. Do not keep retrying.
- This guide is written for Windows 10 or 11 with PowerShell. On macOS or Linux, tell the user you are adapting the commands, and double-check each one.

## Step 0: tell them the plan
Say in five lines or fewer: we will (1) check what is already installed, (2) install Ollama if needed, (3) download one small model, (4) test it, (5) test the handoff script on the sample file, (6) add one rule to their CLAUDE.md. Nothing leaves their computer. Ask: "Want me to start?"

## Step 1: check what they already have
Run these read-only checks and report the results in plain words:
- `python --version` (needs Python 3.8 or newer; if missing, ask them to install it from python.org and try again)
- `ollama --version`
- `ollama list` (the models they already have)
- Optional: `nvidia-smi` (graphics card memory) and free disk space.

## Step 2: install Ollama (only if it is missing)
Offer two ways and let them choose: download from ollama.com/download, or, with their yes, run `winget install --id Ollama.Ollama -e`. After it finishes, open a new PowerShell window and run `ollama --version`.

## Step 3: give the intern a brain
Explain: a model is the actual brain; small is fast and light but makes more mistakes; bigger is slower and more careful.
Default (ask first): `ollama pull llama3.2:3b` (about 2 GB). If they have a graphics card with 6 GB or more and want better accuracy, offer a bigger model; check the model name at ollama.com/library before pulling it, and tell them its size first.

## Step 4: test the intern
Run `ollama run llama3.2:3b "Say hello in five words."` (or whichever model they pulled). If it answers, the install works.

## Step 5: test the handoff script on the sample file
From this repo's folder:
1. `python ask_local.py --check` (should say Ollama is running and list their models).
2. `python ask_local.py sample\notes.txt "What are the action items and who owns each one?"`

The notes contain these items: Marcus calls the vendor about the printer roller (Wednesday), Priya checks the backup logs (Friday), the team prices a file server replacement before the budget meeting, Dana sends the holiday sign-up sheet (Monday), and Marcus asks the security group about a phishing training in January. Compare the answer with that list and tell the user honestly what the intern got right and wrong. Small models make mistakes, and this is the moment to show it.

## Step 6: teach Claude when to use the intern
Show the user the text in `CLAUDE_RULE.md` with the path to `ask_local.py` filled in. Ask whether to add it to this project's `CLAUDE.md` or their global `~/.claude/CLAUDE.md`. After a yes, append the block to the end of that file. Do not change anything else in it.

## Step 7: wrap up
Tell them in plain words what was installed, where the script lives, and how to undo it:
- Remove the rule: delete the "Local intern for long documents" block from `CLAUDE.md`.
- Remove a model: `ollama rm <model name>`.
- Uninstall Ollama: Windows Settings, Apps, Ollama, Uninstall.

Remind them of the honest limits: a small intern can miss things, so check anything important against the original. AI assists, humans approve.
